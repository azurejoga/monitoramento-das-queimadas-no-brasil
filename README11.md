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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e69a7d1a-7c2d-3756-a982-6a9559a01da8 | -9.2077 | -49.03177 | 2025-07-02 04:27:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c415620d-3405-3eeb-950b-602c329f88df | -9.23175 | -50.03043 | 2025-07-02 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9fe8ab34-637a-3731-b61b-5d19a4aa1ebb | -9.99434 | -46.18965 | 2025-07-02 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8a84a4f9-0312-308f-8b00-feb0519dbfe4 | -14.90266 | -45.14337 | 2025-07-02 04:27:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 269907f8-9b2c-394f-81f6-b6de6e16c047 | -10.30447 | -57.13424 | 2025-07-02 04:27:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1270932c-0550-36e9-a2f8-0d69f3cbd99d | -9.24044 | -50.04451 | 2025-07-02 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1323303-778c-31e3-8757-6a318f92fe44 | -8.82085 | -49.12065 | 2025-07-02 04:27:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 03d01e10-9aa5-38da-ba12-f7e9d0dd056c | -11.33168 | -51.44417 | 2025-07-02 04:27:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 207d68c4-f202-342c-a4e4-aec69e6973ea | -10.93154 | -57.12968 | 2025-07-02 04:27:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4fc95b4f-aea3-325f-96a6-e0e6719bd4be | -8.31591 | -46.3153 | 2025-07-02 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 000f4b04-5251-3cbc-8a36-13939a705dba | -9.82262 | -48.37406 | 2025-07-02 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 75be3552-a3d4-35cc-a149-ee8013d04f18 | -9.20778 | -49.03149 | 2025-07-02 04:27:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3f21c9c9-beb1-37d7-85f8-4cdb76da9973 | -14.38054 | -50.32734 | 2025-07-02 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55fe4408-b2c3-33c3-a614-01870c60b902 | -14.14506 | -46.34665 | 2025-07-02 04:27:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 72f08643-4b8a-3fa3-ad0b-c47225698fd4 | -15.00548 | -48.32727 | 2025-07-02 04:27:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 42d56fc4-8197-3c6a-ad49-e769662e3d40 | -10.8904 | -56.45016 | 2025-07-02 04:27:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 30488f45-edd7-3204-b723-2fbcff55e24f | -13.42832 | -47.84352 | 2025-07-02 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2ee696b1-fc4b-3378-bdfb-031ce9ab4fa0 | -11.84129 | -43.80236 | 2025-07-02 04:27:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a78a2dac-3ef2-3fa7-aca8-d6997d4e1c5d | -10.89381 | -56.46067 | 2025-07-02 04:27:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| af880f6d-8c45-3d27-b698-ddd2d5fd2ab7 | -10.29899 | -57.13313 | 2025-07-02 04:27:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 20cf19cc-b17c-3f13-95d2-8a34ce385f7c | -10.8892 | -56.45652 | 2025-07-02 04:27:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a0c006dc-c764-3aef-b576-a016e6568c53 | -13.42169 | -47.81738 | 2025-07-02 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9716c4fa-adb0-39dc-925f-4a17cce4a6a6 | -10.87782 | -53.75615 | 2025-07-02 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dff56ffa-68f9-3a73-a5c8-f59b0f0fa23e | -15.89906 | -43.45921 | 2025-07-02 04:27:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 4a3983d5-c171-32c8-9199-6c6d5ca2e6b2 | -9.23754 | -50.03981 | 2025-07-02 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e1765106-b643-31f8-b591-ed60220b2266 | -8.35525 | -48.45842 | 2025-07-02 04:27:00 | NOAA-21 | BRASILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1703602 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 542ae323-8537-30b8-9de0-413bae6c1d95 | -9.81928 | -48.37353 | 2025-07-02 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 72969b87-87a2-3af3-9b10-f9816b39434d | -15.92509 | -43.52078 | 2025-07-02 04:27:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5a49c570-6f3a-3de0-ba8d-4db315271ee1 | -10.29765 | -57.14039 | 2025-07-02 04:27:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5ba89aa7-6ec7-3672-ae7d-a337f76eadb5 | -15.57101 | -47.85729 | 2025-07-02 04:27:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6c3b853a-7ebf-34b9-a7e9-ae014395b543 | -13.36233 | -46.19323 | 2025-07-02 04:27:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e253ae65-bb77-36f4-8459-1a13d1bb4f0e | -9.23398 | -50.03922 | 2025-07-02 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71e46ef1-6fa4-3881-b004-1abda37b6ae5 | -11.57507 | -54.56744 | 2025-07-02 04:27:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9d691110-7c1e-3fc7-82ea-edd4fe01d20b | -14.38396 | -50.32794 | 2025-07-02 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ccf19117-279a-335d-9915-93b88499a44e | -13.41124 | -47.81929 | 2025-07-02 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d605da0b-fe66-3e5c-8b12-b76bdb04ca5e | -10.29905 | -57.1332 | 2025-07-02 04:27:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d071b99a-b507-34b2-8804-9b811f9c1c70 | -10.50873 | -53.58437 | 2025-07-02 04:27:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49ec13c1-24dd-3db6-ae93-46650d577b44 | -13.36288 | -46.1895 | 2025-07-02 04:27:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8299da64-a8ba-37f6-94c8-4a1a0b8e7f4b | -10.88 | -56.44817 | 2025-07-02 04:27:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d3c8532a-8680-3ba9-aa33-cfb29cd04cc8 | -13.23767 | -49.83894 | 2025-07-02 04:27:00 | NOAA-21 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 88afe217-be62-38e5-b740-ded095254df2 | -12.11332 | -50.28291 | 2025-07-02 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1b362a03-e4c5-300d-ad0e-b6e374873668 | -9.70472 | -56.18267 | 2025-07-02 04:27:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2652885a-43f5-34d4-8e73-174499eadc61 | -9.33791 | -48.48687 | 2025-07-02 04:27:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aa67902f-e9e7-3fec-977f-b59c8b2ccc14 | -10.89724 | -54.05467 | 2025-07-02 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e704bb0f-854d-3a08-a2e1-03ba9a572e0b | -9.57519 | -49.10619 | 2025-07-02 04:27:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a5897548-3fbe-399b-b34b-c9f71c7245d2 | -20.66567 | -48.439 | 2025-07-02 04:29:00 | NOAA-21 | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c9257a2b-0377-3cef-a5c2-2ae235ad4eb9 | -18.66369 | -55.75545 | 2025-07-02 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 83273c41-9bb5-3000-b5f6-4b342279b7de | -16.62136 | -44.06272 | 2025-07-02 04:29:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0dbb55cf-25a8-3964-94db-2eae0b93a528 | -18.43137 | -54.56019 | 2025-07-02 04:29:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6445c564-195a-31d0-af75-1f7cd3acba3a | -20.47757 | -53.67783 | 2025-07-02 04:29:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c24659f2-3a6e-3347-8601-d9493cc61147 | -18.0881 | -54.27781 | 2025-07-02 04:29:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4242e146-4528-3d7f-8429-f3d818aa24fb | -16.42847 | -44.523 | 2025-07-02 04:29:00 | NOAA-21 | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f328867-2a99-3c3a-8d81-b5d3d801d46c | -16.51029 | -49.71447 | 2025-07-02 04:29:00 | NOAA-21 | AVELINÓPOLIS | GOIÁS | Brasil | 5202809 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 09f8b421-4bc7-35ee-9a5e-cd87c1c56047 | -16.3838 | -54.5774 | 2025-07-02 04:29:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8f3045f6-4ad0-3d46-9ac5-6e19e99382ff | -20.76387 | -46.76731 | 2025-07-02 04:29:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4a56efff-5403-3e75-ad31-82401e03258a | -17.09507 | -43.80302 | 2025-07-02 04:29:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e75a5dc-56c8-3d92-a5cf-f73b2a6e9f0d | -16.42532 | -44.51759 | 2025-07-02 04:29:00 | NOAA-21 | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 853ba9c6-a1dc-3b9e-9bd4-e52f412d6a12 | -15.94329 | -50.06206 | 2025-07-02 04:29:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3c000cae-bc2a-3666-87f4-a9f8ec60291d | -21.18123 | -43.98027 | 2025-07-02 04:29:00 | NOAA-21 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 53732dd6-ddfc-357a-8b65-18c64358937a | -19.78887 | -47.46864 | 2025-07-02 04:29:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 61045152-4005-304f-9d97-def361e05bf1 | -19.52402 | -43.60183 | 2025-07-02 04:29:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e5b1e857-d411-37c4-85c7-0e683920cff5 | -16.29835 | -45.10109 | 2025-07-02 04:29:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 48498daa-8d40-3a30-8f1f-a5ecd69b00d9 | -19.3154 | -46.02916 | 2025-07-02 04:29:00 | NOAA-21 | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 316ee00c-89b1-3e7e-a2d8-b728a14eee2f | -17.22025 | -44.80492 | 2025-07-02 04:29:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 588be269-be47-3d35-aff3-7076e8004838 | -16.07041 | -51.5619 | 2025-07-02 04:29:00 | NOAA-21 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3dda2d15-d14d-33f9-9e95-69d0be07a988 | -16.07395 | -51.56251 | 2025-07-02 04:29:00 | NOAA-21 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 38aa8be2-2dcf-3ac7-ae68-8d86600e3fdd | -19.16397 | -54.843 | 2025-07-02 04:29:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 37a17f60-1007-37cd-b427-89720655db51 | -18.66021 | -55.7502 | 2025-07-02 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 17798ead-730c-3962-adb3-c4c24ca9d54e | -20.47743 | -54.3919 | 2025-07-02 04:29:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a28ef248-a0f1-3d71-ba4f-e11782d0864c | -18.3748 | -49.2678 | 2025-07-02 04:29:00 | NOAA-21 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4531d226-0561-3fe3-97c5-a195145a0646 | -20.5414 | -48.75003 | 2025-07-02 04:29:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 40fce89a-6266-3c24-a7f8-041f09b35a23 | -16.42256 | -46.55186 | 2025-07-02 04:29:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e280f9df-934f-3cdd-ba8b-3886082a92ce | -19.43672 | -48.55246 | 2025-07-02 04:29:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b599ffbc-5b8a-3f42-9be2-a232904cb26e | -19.22137 | -55.37612 | 2025-07-02 04:29:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 0c84813a-7be3-3c71-9fee-6d5f1d39d21e | -19.05586 | -50.93492 | 2025-07-02 04:29:00 | NOAA-21 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8b7a7a5c-e8b4-3f2a-93c8-8355faead125 | -16.50697 | -49.71389 | 2025-07-02 04:29:00 | NOAA-21 | AVELINÓPOLIS | GOIÁS | Brasil | 5202809 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 7b66b189-a385-37fd-a8b0-a7ec53fce47f | -16.44537 | -51.06382 | 2025-07-02 04:29:00 | NOAA-21 | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ebc56ab3-a1af-3f20-9875-955ce7fdf180 | -18.03329 | -46.05412 | 2025-07-02 04:29:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 107a4562-ec01-374c-a338-6e7f0414cec8 | -18.66105 | -55.74585 | 2025-07-02 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 3f99e308-d21d-3601-bf39-232bba5fdffa | -16.06972 | -51.56597 | 2025-07-02 04:29:00 | NOAA-21 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 27bbcd98-520f-3b16-aa79-49ec734567a1 | -16.2874 | -48.01768 | 2025-07-02 04:29:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4567e3cc-6269-3fee-b82a-c7420499f81c | -18.66452 | -55.75111 | 2025-07-02 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 416a2cc1-8c43-3d24-b5b3-ad103df2ff5c | -19.16062 | -54.83844 | 2025-07-02 04:29:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6191755-59d1-3f4e-92c1-484e2f43ae04 | -18.08745 | -54.28135 | 2025-07-02 04:29:00 | NOAA-21 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0e5c6f6a-ce0d-3db1-b2dd-d1962ac6633b | -19.52354 | -43.60571 | 2025-07-02 04:29:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9b5d4ca6-be72-3740-9f31-a0b49bbea7c6 | -17.65899 | -46.83228 | 2025-07-02 04:29:00 | NOAA-21 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6fe23687-6469-37f3-a589-4bf351b21246 | -17.92195 | -45.55592 | 2025-07-02 04:29:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7ce1512a-1329-31c8-b3b5-1ada910adc32 | -19.44005 | -48.55301 | 2025-07-02 04:29:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| beb681d7-e231-300f-b53f-20af00b509f3 | -16.60729 | -44.51669 | 2025-07-02 04:29:00 | NOAA-21 | SÃO JOÃO DO PACUÍ | MINAS GERAIS | Brasil | 3162658 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 537bacc3-765c-31da-89ca-abf00c34c2d4 | -19.43727 | -48.54876 | 2025-07-02 04:29:00 | NOAA-21 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4d4c1684-69d0-39fd-a11e-42a78407db8b | -21.85876 | -46.69575 | 2025-07-02 04:29:00 | NOAA-21 | ÁGUAS DA PRATA | SÃO PAULO | Brasil | 3500402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 4699f2a0-4588-3633-82e5-820b0b1ebb56 | -17.49033 | -46.74272 | 2025-07-02 04:29:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a55a9139-65ca-3528-b747-67cf7d693659 | -16.42467 | -44.52245 | 2025-07-02 04:29:00 | NOAA-21 | BRASÍLIA DE MINAS | MINAS GERAIS | Brasil | 3108602 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd5c9bb6-c3b9-3c80-bfae-56d73763cedc | -20.53807 | -48.74947 | 2025-07-02 04:29:00 | NOAA-21 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5b364a81-d3d2-33f3-926c-996427baccfe | -20.32969 | -53.04936 | 2025-07-02 04:29:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3b18c61d-17bf-3c34-9b88-ad22876e26bb | -20.23608 | -41.88944 | 2025-07-02 04:29:00 | NOAA-21 | MARTINS SOARES | MINAS GERAIS | Brasil | 3140530 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| ba85e3ec-a108-3fff-adf5-3f05e123e208 | -18.14729 | -47.7999 | 2025-07-02 04:29:00 | NOAA-21 | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ef75c29b-d2f3-3c80-b871-50c25a498daf | -18.03408 | -46.05556 | 2025-07-02 04:29:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b4cc6520-95a5-3d45-92e9-69498015452f | -20.66231 | -48.43845 | 2025-07-02 04:29:00 | NOAA-21 | JABORANDI | SÃO PAULO | Brasil | 3524204 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f4df4cab-96ea-3ee1-8060-ea138263298f | -21.85941 | -46.69085 | 2025-07-02 04:29:00 | NOAA-21 | ÁGUAS DA PRATA | SÃO PAULO | Brasil | 3500402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |


[Clique aqui para ver as próximas entradas](README12.md)
