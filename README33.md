# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 61ac7f2e-37d4-304a-affc-a6e319caf410 | -17.98466 | -44.33644 | 2026-09-15 04:17:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 70acdd3e-601d-3fa8-a887-7a53fd18f735 | -13.26029 | -51.28652 | 2026-09-15 04:17:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e67475ed-a67a-39c2-ba2e-2c7a8e114289 | -14.20805 | -47.42907 | 2026-09-15 04:17:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a27a5a69-79ce-3ac3-a001-ac46d8754064 | -15.53773 | -48.80162 | 2026-09-15 04:17:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc4409f3-fd05-3608-a0fe-adf2eeb867a3 | -18.16563 | -51.77017 | 2026-09-15 04:17:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fbbc7552-10d6-36cc-a7fe-a6118fb31e19 | -13.57566 | -47.89192 | 2026-09-15 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cc67fe93-ba69-3681-8d83-702e7e8713ba | -17.3116 | -49.22831 | 2026-09-15 04:17:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 768a975c-2316-3d5a-ab4e-a2b57308bc3d | -14.68657 | -48.00912 | 2026-09-15 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8cfdd5fe-a535-33f5-b017-21f451ce121b | -17.9444 | -42.31994 | 2026-09-15 04:17:00 | NPP-375D | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 1e8f6b5e-7696-38d2-b9e9-23d5dfa8dde8 | -17.30864 | -49.22879 | 2026-09-15 04:17:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 301ab6a5-bbbc-3592-881e-5656b304097e | -17.94907 | -44.25605 | 2026-09-15 04:17:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ed57fc0b-e798-3b15-8339-1f9d8b8e6cf9 | -13.59927 | -47.91008 | 2026-09-15 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 16318204-448c-3d40-942f-82bc7ae19e2c | -15.27821 | -42.78932 | 2026-09-15 04:17:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0cc565e3-ef69-391a-bf55-bade09ae4d52 | -18.95913 | -47.29599 | 2026-09-15 04:17:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d09aefd2-af37-3273-8adc-ecbadc4978d5 | -15.04657 | -48.55392 | 2026-09-15 04:17:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c6f65cd9-bf6f-3539-8911-64bfc5f851f0 | -15.5384 | -48.80831 | 2026-09-15 04:17:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80c1dea5-f878-344d-b293-758d933bc696 | -14.6781 | -48.00689 | 2026-09-15 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d4bf9233-188b-34fd-985c-68dae3de0770 | -15.53328 | -48.80072 | 2026-09-15 04:17:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9073781c-4da5-3329-b86d-d702fca0555f | -15.05525 | -48.54998 | 2026-09-15 04:17:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f3352601-76e5-342d-adfc-e58a649a0af7 | -13.27118 | -51.28881 | 2026-09-15 04:17:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b392cd0a-9b3a-36a1-917c-0dd526ab9793 | -15.52854 | -40.85134 | 2026-09-15 04:17:00 | NPP-375D | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 05bb13e2-337c-37b9-b21b-28d023002132 | -15.53668 | -41.78222 | 2026-09-15 04:17:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| fc05fded-4631-36c8-9932-da173859b252 | -14.19836 | -47.43484 | 2026-09-15 04:17:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 15c314ac-e9fc-3338-9251-2fd92706cd07 | -14.03961 | -43.29272 | 2026-09-15 04:17:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 17ee640b-3135-3af2-b1d1-0ac042733e4a | -13.26645 | -51.28408 | 2026-09-15 04:17:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 23a51302-ef72-3d18-9118-b7b72eca529f | -13.3005 | -51.28389 | 2026-09-15 04:17:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c0968b1a-1834-31dd-adca-fd93de345742 | -16.47921 | -43.4193 | 2026-09-15 04:17:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f7e5fba8-ebc7-3691-94a4-71b6a1fce7ab | -15.58378 | -48.78832 | 2026-09-15 04:17:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bf10a3dc-117e-3a09-ad1d-f83dc2fcc4e2 | -16.7986 | -47.61409 | 2026-09-15 04:17:00 | NPP-375D | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0649c9c4-9268-3046-9089-db9ddd2bc7b9 | -15.58668 | -42.5709 | 2026-09-15 04:17:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0f42736e-0134-3935-9c29-9bd623374eaa | -15.92183 | -47.36539 | 2026-09-15 04:17:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f7c65450-a8dd-372d-b6fe-ad771b9e4193 | -15.98662 | -43.27421 | 2026-09-15 04:17:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 157d9cee-7543-3f07-95fb-d01883e1fe4c | -15.54012 | -48.79945 | 2026-09-15 04:17:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1b9f0477-7453-3adf-95c1-0feb9d0e8309 | -14.69007 | -48.0143 | 2026-09-15 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 56e421db-6705-37d0-9d3e-227ef16f0cde | -15.26877 | -42.78395 | 2026-09-15 04:17:00 | NPP-375D | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 77cecdc1-eb0d-341c-89b6-263e981a8f2e | -15.29154 | -42.79187 | 2026-09-15 04:17:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 89b0ec83-22a0-3b66-9945-d392aa5a0e35 | -15.57753 | -48.79687 | 2026-09-15 04:17:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 08848b3d-190c-3a5a-970a-3f6da8d981f0 | -15.98998 | -43.27479 | 2026-09-15 04:17:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d5e03637-2336-3372-b149-ba43561650b4 | -15.28821 | -42.79119 | 2026-09-15 04:17:00 | NPP-375D | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4666dfe7-ef6c-340d-b39e-f91bf2e6a34e | -18.8651 | -42.00655 | 2026-09-15 04:17:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| f26057fb-4aa3-3248-930c-a197d76e344f | -15.36241 | -52.99627 | 2026-09-15 04:17:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a5b6867f-eac4-3cec-b591-4829087bd4e6 | -14.67031 | -48.00096 | 2026-09-15 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1bf2314f-3ce1-3093-b159-3a6c773bb2fd | -14.67857 | -42.84882 | 2026-09-15 04:17:00 | NPP-375D | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| db4c6a1c-5457-30f7-ba84-876778731560 | -15.58201 | -48.79755 | 2026-09-15 04:17:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3de690a-4104-3f5c-b1e1-1489c42478e4 | -17.40459 | -41.0018 | 2026-09-15 04:17:00 | NPP-375D | PAVÃO | MINAS GERAIS | Brasil | 3148509 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 82acd559-0038-3151-ae7f-26f7e1ad8c58 | -13.87132 | -49.42496 | 2026-09-15 04:17:00 | NPP-375D | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8978319c-67a4-3e9a-b88c-f612a3495bd3 | -16.9682 | -43.35939 | 2026-09-15 04:17:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9cf00d56-6639-397e-b254-a3643d4ea709 | -15.1704 | -43.84908 | 2026-09-15 04:17:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f96737b9-5e31-3378-a472-7ca1eb77fe25 | -14.66872 | -48.00958 | 2026-09-15 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b704a9f-1269-3f94-9efe-d20ea08be9de | -15.26543 | -42.78341 | 2026-09-15 04:17:00 | NPP-375D | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0501f2d7-ca76-3d4e-bf34-c0627d23a09e | -16.48939 | -47.82331 | 2026-09-15 04:17:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5a1848ab-a4de-33a2-9a03-e4fb9104db72 | -18.16121 | -51.76564 | 2026-09-15 04:17:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e0cf09e9-aede-3686-9d4a-a184fdd12afe | -17.4604 | -43.6422 | 2026-09-15 04:17:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 132b99d6-888d-31a9-b37e-a5aa70c8274e | -16.05393 | -52.27901 | 2026-09-15 04:17:00 | NPP-375D | ARAGARÇAS | GOIÁS | Brasil | 5201702 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e22ef3ee-39ed-3d8d-9803-d655e76e5b40 | -16.51721 | -47.80085 | 2026-09-15 04:17:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6e8bf3d3-cb16-3670-9b69-2d249536aff9 | -16.96881 | -43.35571 | 2026-09-15 04:17:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 1bff1206-7118-3f6f-b80d-595975d79d5a | -15.05182 | -48.55032 | 2026-09-15 04:17:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2227865f-1bbd-3f97-b636-21b745d5d88d | -14.17083 | -47.41551 | 2026-09-15 04:17:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a9954fef-8c41-341f-b563-bf28c40e39ba | -13.57045 | -47.89575 | 2026-09-15 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ab1a495a-657f-3504-a5b7-952840d2b842 | -16.08156 | -43.6908 | 2026-09-15 04:17:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8431dc5d-1368-371a-bc8b-02778d353128 | -13.29838 | -51.29464 | 2026-09-15 04:17:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| bef20b83-99d0-3e78-ac6e-b93b4b0c8afe | -18.52334 | -42.85194 | 2026-09-15 04:17:00 | NPP-375D | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b3046fe1-84c3-3cf9-a35b-5885c21deec1 | -15.04551 | -48.55298 | 2026-09-15 04:17:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 57e70732-e89f-3b32-b329-fa6740257d70 | -15.57476 | -48.7873 | 2026-09-15 04:17:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e56e88b6-f5e9-32d1-ba5c-91263dbd0f93 | -14.17609 | -47.41541 | 2026-09-15 04:17:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 39741754-d4c8-3201-9cf1-bdf8386939a1 | -15.53612 | -41.78582 | 2026-09-15 04:17:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 0442038f-e9d6-31b0-86a5-c3b4534013fa | -14.68309 | -48.00394 | 2026-09-15 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e0352bb5-02d9-3f73-aef4-4930bd9f5680 | -13.30312 | -51.29937 | 2026-09-15 04:17:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9bcad59a-acbc-3307-b3de-949394cd5304 | -17.4769 | -43.66803 | 2026-09-15 04:17:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c84568d0-8b89-3c2a-930d-43ddf8c1298b | -14.95687 | -47.52951 | 2026-09-15 04:17:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ba272336-a361-3b15-a051-e342aa49b25d | -14.86021 | -48.14584 | 2026-09-15 04:17:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3af9b831-37f1-3087-8155-96e464422cd1 | -14.68928 | -48.01856 | 2026-09-15 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 57324655-599e-3a42-a46f-7065bd3adca0 | -14.68271 | -48.03012 | 2026-09-15 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e3f318e1-1e99-3d72-afd5-30fc06f79a12 | -14.85177 | -48.14316 | 2026-09-15 04:17:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d2a36568-bd6e-32e3-a676-99cf7d7571fd | -15.54059 | -48.81102 | 2026-09-15 04:17:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 377274b5-3d74-3cd0-9c83-891ca27baa18 | -15.02619 | -41.45906 | 2026-09-15 04:17:00 | NPP-375D | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fd1ed61a-7a72-315a-9b31-1857e7f5d638 | -14.23047 | -41.14551 | 2026-09-15 04:17:00 | NPP-375D | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b9197283-4994-3de7-b501-bf05d8b284b9 | -18.86845 | -42.00713 | 2026-09-15 04:17:00 | NPP-375D | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 7dbf5a9f-83bd-3520-91f0-3e2b076d24ea | -13.9011 | -42.51303 | 2026-09-15 04:17:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a3ec2606-fba7-341c-b8d2-5a73a188230d | -15.16761 | -43.84466 | 2026-09-15 04:17:00 | NPP-375D | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1d8b9b92-d78f-35cf-afe8-b538c1cad0b9 | -14.17567 | -47.4125 | 2026-09-15 04:17:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8feeb5e6-03aa-3bf0-85f5-f14200b9dbcc | -17.44645 | -41.9121 | 2026-09-15 04:17:00 | NPP-375D | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| bbc097e8-c693-34dd-97e6-0e51468b4e37 | -16.22305 | -39.14283 | 2026-09-15 04:17:00 | NPP-375D | SANTA CRUZ CABRÁLIA | BAHIA | Brasil | 2927705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| eddd323f-df0d-3a15-b133-6a8a43268a3a | -14.22193 | -47.42386 | 2026-09-15 04:17:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 91c89c84-3c6d-3d0a-a52a-32fc132f715b | -15.58018 | -48.83133 | 2026-09-15 04:17:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dcddfeb7-e205-3de9-a2c2-e1c28010a96e | -13.25552 | -47.08581 | 2026-09-15 04:17:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1079ea29-0a75-30fa-9c65-6641bcc51ffb | -15.58465 | -48.83208 | 2026-09-15 04:17:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c28bfa4c-cd5f-3b0f-b20e-58719063b567 | -14.67581 | -42.84461 | 2026-09-15 04:17:00 | NPP-375D | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1446fc4c-a6f7-339b-aebe-8f2b98f00382 | -14.20945 | -47.42147 | 2026-09-15 04:17:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| baa9e2f7-baee-3b65-ad89-026ada4d41f8 | -13.72502 | -48.97742 | 2026-09-15 04:17:00 | NPP-375D | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 408abe6e-5163-3dcd-b485-a61c5e415039 | -17.9806 | -44.33971 | 2026-09-15 04:17:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 64d06e16-6b81-34cc-a3ca-61f2d0cbe872 | -16.96699 | -43.36679 | 2026-09-15 04:17:00 | NPP-375D | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c6782d7b-6e2d-3e6b-9e92-d3e9dc49fdca | -15.54297 | -48.8086 | 2026-09-15 04:17:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d3383207-10b3-354b-8cd8-daa5e7090163 | -13.30524 | -51.28862 | 2026-09-15 04:17:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d374811d-5a43-3bd0-8762-1aa69074fb01 | -15.92198 | -47.36502 | 2026-09-15 04:17:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a7805300-d76d-3ef9-9c96-df3174aed46d | -18.21581 | -43.68164 | 2026-09-15 04:17:00 | NPP-375D | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9ac4e11-e9e4-3576-9b05-332e41331556 | -17.47141 | -43.65934 | 2026-09-15 04:17:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| af6f0cb5-9431-309d-96e5-09144a6fde56 | -15.05628 | -48.55089 | 2026-09-15 04:17:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c289e704-8c2b-3604-8b13-e302684f2fdf | -13.35544 | -51.71353 | 2026-09-15 04:17:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0579c900-d4d8-3e55-80af-a931cb8c68cd | -17.20827 | -41.48992 | 2026-09-15 04:17:00 | NPP-375D | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |


[Clique aqui para ver as próximas entradas](README34.md)
