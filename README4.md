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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c8d74460-05d7-3631-b54a-f4569f4a6fb9 | -21.532499 | -47.749001 | 2024-10-07 00:24:54 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d4b8354d-9b66-31a6-824d-58f585e88bde | -21.5189 | -47.7309 | 2024-10-07 00:24:54 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| b46cdeb7-8b38-3367-b0dd-795c9cffb5f2 | -21.5208 | -47.741001 | 2024-10-07 00:24:54 | METOP-B | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c6260ffa-1ead-34e0-9ca2-bf3f2c898b96 | -20.658899 | -44.019798 | 2024-10-07 00:24:56 | METOP-B | ENTRE RIOS DE MINAS | MINAS GERAIS | Brasil | 3123908 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b8d3b955-1e28-3ae8-9126-6b2803e1a21b | -20.6605 | -44.0271 | 2024-10-07 00:24:56 | METOP-B | ENTRE RIOS DE MINAS | MINAS GERAIS | Brasil | 3123908 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 43461b95-c2a3-3df5-a111-429cf930b55a | -20.446501 | -43.086399 | 2024-10-07 00:24:56 | METOP-B | DIOGO DE VASCONCELOS | MINAS GERAIS | Brasil | 3121704 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a6244fd8-42a3-3d37-9983-03bd459ebb78 | -20.448099 | -43.0937 | 2024-10-07 00:24:56 | METOP-B | DIOGO DE VASCONCELOS | MINAS GERAIS | Brasil | 3121704 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b4a3997c-c94f-362f-b2ed-a57ef2e5e0a0 | -21.2953 | -47.200001 | 2024-10-07 00:24:56 | METOP-B | CÁSSIA DOS COQUEIROS | SÃO PAULO | Brasil | 3510906 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ffbf428f-2399-3b85-95d3-8874bcb9d91e | -21.6791 | -49.598499 | 2024-10-07 00:24:57 | METOP-B | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 50589a06-14ee-3b2a-93ae-365465aee41a | -21.681499 | -49.611698 | 2024-10-07 00:24:57 | METOP-B | LINS | SÃO PAULO | Brasil | 3527108 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a8339967-df9a-3d85-957b-1b35ffb08c1a | -20.4844 | -43.638302 | 2024-10-07 00:24:57 | METOP-B | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a1e4633f-22ea-3b30-bcf4-b642399243a5 | -20.486 | -43.645599 | 2024-10-07 00:24:57 | METOP-B | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 841054de-0781-3f71-8165-00911d969216 | -21.2892 | -47.379902 | 2024-10-07 00:24:57 | METOP-B | SANTA CRUZ DA ESPERANÇA | SÃO PAULO | Brasil | 3546256 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 82008018-0e04-3296-a54d-1090504993f6 | -21.277599 | -47.372299 | 2024-10-07 00:24:57 | METOP-B | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 296e4d5b-bdcb-3775-a45e-5782c66fee77 | -21.2794 | -47.381901 | 2024-10-07 00:24:57 | METOP-B | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 2410cc1e-7ee3-3e74-9b08-9a6b419e9846 | -21.2813 | -47.391602 | 2024-10-07 00:24:57 | METOP-B | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c9f9bcab-2454-3373-bb54-889218c9b684 | -21.269699 | -47.383999 | 2024-10-07 00:24:57 | METOP-B | SANTA CRUZ DA ESPERANÇA | SÃO PAULO | Brasil | 3546256 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 185a3d65-5f73-31cf-a72f-ad27208e47c4 | -20.991301 | -46.070499 | 2024-10-07 00:24:57 | METOP-B | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 84321ccb-4618-31f1-acf1-53f4e09aebc5 | -20.993 | -46.0788 | 2024-10-07 00:24:57 | METOP-B | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4ad54a08-9b2d-38ad-833f-a99d24183bf7 | -20.9799 | -46.0644 | 2024-10-07 00:24:57 | METOP-B | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 523e1d02-54f2-3290-8287-cd3fece4c4e3 | -20.981501 | -46.072701 | 2024-10-07 00:24:57 | METOP-B | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c9f73366-b5e1-328b-9824-ac738e699643 | -20.9832 | -46.081001 | 2024-10-07 00:24:57 | METOP-B | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| acafb51a-3c71-3e7f-930a-e228bd8783a0 | -20.9849 | -46.089298 | 2024-10-07 00:24:57 | METOP-B | CARMO DO RIO CLARO | MINAS GERAIS | Brasil | 3114402 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0b1be006-ce1f-35fa-8825-07b4172db7a9 | -20.253099 | -42.910198 | 2024-10-07 00:24:58 | METOP-B | RIO DOCE | MINAS GERAIS | Brasil | 3155009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 30a26348-33a5-3951-b335-41dcb5353bff | -20.2547 | -42.9175 | 2024-10-07 00:24:58 | METOP-B | RIO DOCE | MINAS GERAIS | Brasil | 3155009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 07a0b1a4-1de3-39a5-97f7-99301d0b7aed | -21.0863 | -47.2258 | 2024-10-07 00:24:59 | METOP-B | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0173ce56-813c-3881-8145-77f307fff688 | -20.413799 | -43.739799 | 2024-10-07 00:24:59 | METOP-B | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1ec2b37e-48ef-3a41-9696-f87e53b23d61 | -20.4153 | -43.747101 | 2024-10-07 00:24:59 | METOP-B | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cac48f83-4cc0-3b5d-9347-32175b676c8b | -21.084499 | -47.2164 | 2024-10-07 00:24:59 | METOP-B | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| f62dc1df-1a93-3909-a5c0-82bb60879e25 | -20.3008 | -43.598301 | 2024-10-07 00:25:00 | METOP-B | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a5541c3f-0a3f-333e-84f5-0394dece579c | -20.302401 | -43.605598 | 2024-10-07 00:25:00 | METOP-B | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a994039c-9d3f-3653-896f-fc0c1a17b3e6 | -21.072901 | -47.209099 | 2024-10-07 00:25:00 | METOP-B | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| c1362fb8-e0a5-3a49-908f-c2eb980dc2a2 | -21.0748 | -47.218498 | 2024-10-07 00:25:00 | METOP-B | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 5f8bea6c-8373-39a8-8078-847172350c01 | -21.076599 | -47.227901 | 2024-10-07 00:25:00 | METOP-B | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| d474c74a-a3ed-3123-b5f2-e8e4069e3ba6 | -21.0784 | -47.237301 | 2024-10-07 00:25:00 | METOP-B | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 0aaae013-7bff-3202-897c-a0e8c9a2d19f | -21.063101 | -47.2113 | 2024-10-07 00:25:00 | METOP-B | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 722c6be7-d007-3f6a-b218-ed9f351d935a | -21.065001 | -47.2206 | 2024-10-07 00:25:00 | METOP-B | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ba42f302-b8ce-31ad-af9c-77166ab5dfee | -21.066799 | -47.23 | 2024-10-07 00:25:00 | METOP-B | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 822880b9-02a3-3100-a261-08f0809ce83d | -21.0686 | -47.239399 | 2024-10-07 00:25:00 | METOP-B | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ecc66165-a843-30e5-8442-dde065023575 | -18.0282 | -42.057598 | 2024-10-07 00:25:00 | METOP-B | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b1919c3d-d5da-3024-8746-650f700f157d | -18.030001 | -42.0653 | 2024-10-07 00:25:00 | METOP-B | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| dbbc2ecf-516e-3598-a337-29db18de9a4d | -18.0203 | -42.067799 | 2024-10-07 00:25:00 | METOP-B | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 50753d42-9270-3a9e-8e3f-640546239524 | -19.9638 | -42.4445 | 2024-10-07 00:25:01 | METOP-B | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3d7774da-a4df-3117-8690-a80d3071cc35 | -19.9655 | -42.452 | 2024-10-07 00:25:01 | METOP-B | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b545638d-36eb-30df-8d60-e91108fb4cad | -18.007799 | -42.1035 | 2024-10-07 00:25:01 | METOP-B | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4e46e984-b9a5-32a8-983d-9da644812793 | -18.009501 | -42.111198 | 2024-10-07 00:25:01 | METOP-B | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 020bc7dc-74dc-3451-9ed6-619c1367792b | -18.011299 | -42.1189 | 2024-10-07 00:25:01 | METOP-B | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 34184cf0-f88e-344f-9e5b-9d3a23300d3a | -17.9981 | -42.105999 | 2024-10-07 00:25:01 | METOP-B | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 98dac953-9c86-3004-a30f-5de43f17e2b3 | -17.9998 | -42.113701 | 2024-10-07 00:25:01 | METOP-B | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 484a43e4-547a-3982-b9ce-7be2ae9b74a6 | -18.0016 | -42.1213 | 2024-10-07 00:25:01 | METOP-B | FRANCISCÓPOLIS | MINAS GERAIS | Brasil | 3126752 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 41445502-5c69-3d3f-8bbc-23e77195b1f6 | -19.642599 | -41.441502 | 2024-10-07 00:25:03 | METOP-B | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 34197084-c5de-34f1-84e6-e3669c048391 | -19.644501 | -41.449402 | 2024-10-07 00:25:03 | METOP-B | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1e21bb90-d86a-341b-858e-13388fda9461 | -19.767099 | -41.984798 | 2024-10-07 00:25:03 | METOP-B | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bd12e229-0c5f-3621-97a3-b6d2428cb8c1 | -19.768801 | -41.9925 | 2024-10-07 00:25:03 | METOP-B | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0f107874-6fb6-3da4-9348-7ec1ecdbb406 | -19.842699 | -42.364498 | 2024-10-07 00:25:03 | METOP-B | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5936b3c2-bc91-3a9e-819a-3209202588bf | -19.844299 | -42.372002 | 2024-10-07 00:25:03 | METOP-B | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b4b8f70f-fdf8-3a96-822c-d47454a505f1 | -19.4478 | -40.694698 | 2024-10-07 00:25:03 | METOP-B | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 543356d4-e581-39d7-afd3-dab9dc8e8874 | -19.832899 | -42.367001 | 2024-10-07 00:25:03 | METOP-B | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 03985cd0-070d-34ae-a3f7-2e8872ac1541 | -19.839701 | -42.3969 | 2024-10-07 00:25:03 | METOP-B | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e3827185-74fc-33bb-affe-6fff4d7698fb | -19.8913 | -42.627102 | 2024-10-07 00:25:03 | METOP-B | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5d8b4dab-62fa-3354-af76-9c04fdb34ec4 | -19.8929 | -42.634499 | 2024-10-07 00:25:03 | METOP-B | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c1369d14-69d6-3a1f-a095-e076b8eba928 | -19.8181 | -42.347 | 2024-10-07 00:25:03 | METOP-B | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 069dba3a-473b-3079-ab4b-2c7101eb907b | -19.819799 | -42.3545 | 2024-10-07 00:25:03 | METOP-B | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5b9bf86b-feee-3cc4-8cc1-693d7ea3ab29 | -19.821501 | -42.3619 | 2024-10-07 00:25:03 | METOP-B | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 968ef4e5-e08b-33eb-aeca-94515fc32965 | -19.823099 | -42.3694 | 2024-10-07 00:25:03 | METOP-B | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 451c2144-b3ba-3a18-916b-32777f486bcf | -19.879801 | -42.622101 | 2024-10-07 00:25:03 | METOP-B | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d0c4dbf5-c7c6-3ff2-80ae-eec45cb35479 | -19.8815 | -42.629501 | 2024-10-07 00:25:03 | METOP-B | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| edbca546-3660-3b20-a15f-ebd98bbad17b | -19.883101 | -42.636902 | 2024-10-07 00:25:03 | METOP-B | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4e3a7844-9398-3db9-afe0-6f795e57b801 | -19.8848 | -42.644299 | 2024-10-07 00:25:03 | METOP-B | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 57800a6b-93ca-3756-910e-32d5e3fe41ec | -21.3557 | -50.110298 | 2024-10-07 00:25:04 | METOP-B | PENÁPOLIS | SÃO PAULO | Brasil | 3537305 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 40c805ef-7f40-30e6-987d-c33c4af09637 | -19.8717 | -42.632 | 2024-10-07 00:25:04 | METOP-B | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f84ca0f6-69fe-3f1c-9850-7d1f33b42bef | -19.873301 | -42.6394 | 2024-10-07 00:25:04 | METOP-B | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3dad1100-92e2-301f-ad39-c0b6ed8f7442 | -20.1283 | -43.847 | 2024-10-07 00:25:04 | METOP-B | RIO ACIMA | MINAS GERAIS | Brasil | 3154804 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d3a788ca-c539-3078-b812-271506a21487 | -20.129801 | -43.854301 | 2024-10-07 00:25:04 | METOP-B | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cbaccfc1-6293-37c0-9a63-6be764c3cfad | -20.131399 | -43.861599 | 2024-10-07 00:25:04 | METOP-B | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a42dd1b7-16e9-3e51-b4ef-95cb78fd6c90 | -21.358101 | -50.124199 | 2024-10-07 00:25:04 | METOP-B | PENÁPOLIS | SÃO PAULO | Brasil | 3537305 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 64cba989-a301-3ee3-ab6b-961c0cf49139 | -21.3459 | -50.112202 | 2024-10-07 00:25:04 | METOP-B | PENÁPOLIS | SÃO PAULO | Brasil | 3537305 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 82625c8e-5fbe-3f2e-9769-48cc232ddc9d | -21.348301 | -50.126099 | 2024-10-07 00:25:04 | METOP-B | PENÁPOLIS | SÃO PAULO | Brasil | 3537305 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 47b25f24-3c4e-359c-b1b0-1a4b616d177d | -17.847799 | -42.216499 | 2024-10-07 00:25:04 | METOP-B | MALACACHETA | MINAS GERAIS | Brasil | 3139201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a75b0174-83bc-3a6d-9209-fd9417d8a5bd | -19.768999 | -42.634102 | 2024-10-07 00:25:05 | METOP-B | MARLIÉRIA | MINAS GERAIS | Brasil | 3140308 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| daabd8d4-f563-3570-904d-37bd6e97cce3 | -19.7707 | -42.641499 | 2024-10-07 00:25:05 | METOP-B | MARLIÉRIA | MINAS GERAIS | Brasil | 3140308 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5d264a97-b203-3bca-b0d6-5aa95af34b94 | -19.772301 | -42.648899 | 2024-10-07 00:25:05 | METOP-B | MARLIÉRIA | MINAS GERAIS | Brasil | 3140308 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a7017b08-0a69-37ff-b269-dd02e62a8908 | -20.091299 | -44.2015 | 2024-10-07 00:25:06 | METOP-B | MÁRIO CAMPOS | MINAS GERAIS | Brasil | 3140159 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e6c8bb59-fd76-314f-a260-012de115ac7b | -20.092899 | -44.208801 | 2024-10-07 00:25:06 | METOP-B | MÁRIO CAMPOS | MINAS GERAIS | Brasil | 3140159 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 77b5007c-f2b5-3c74-b32f-050fd76a2b29 | -20.236799 | -44.9865 | 2024-10-07 00:25:06 | METOP-B | SÃO SEBASTIÃO DO OESTE | MINAS GERAIS | Brasil | 3164605 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 119f6050-5b0c-381a-a51f-17f3ca1ad728 | -20.2384 | -44.994099 | 2024-10-07 00:25:06 | METOP-B | SÃO SEBASTIÃO DO OESTE | MINAS GERAIS | Brasil | 3164605 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1a1aac87-760f-3a7d-80a8-8274ca2f1c1c | -20.8344 | -48.196899 | 2024-10-07 00:25:07 | METOP-B | MORRO AGUDO | SÃO PAULO | Brasil | 3531902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| ae039f25-76cf-3773-850b-cd97c0f9845c | -19.8246 | -43.774601 | 2024-10-07 00:25:08 | METOP-B | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7a2aa73b-0db9-3d91-9de1-f3bafce8f84f | -19.826099 | -43.781898 | 2024-10-07 00:25:08 | METOP-B | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f3102b2b-d811-3c2d-bac9-3169a783d19f | -18.2159 | -45.042198 | 2024-10-07 00:25:08 | METOP-B | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 76b84fae-58d3-3922-bbc8-00df5b264778 | -19.8132 | -43.769699 | 2024-10-07 00:25:09 | METOP-B | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 748dbbf2-924f-3f09-83f0-2cd53f362a8b | -19.8148 | -43.777 | 2024-10-07 00:25:09 | METOP-B | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7e404aa5-0fa2-347b-bd68-d7d390bb5af6 | -19.816299 | -43.784199 | 2024-10-07 00:25:09 | METOP-B | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 7cad3286-b84d-369b-b0fb-07375fdb1093 | -19.4277 | -42.126801 | 2024-10-07 00:25:09 | METOP-B | INHAPIM | MINAS GERAIS | Brasil | 3130903 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ae7e736c-3f0e-3b70-96bf-a785831ec6b4 | -19.859699 | -44.080002 | 2024-10-07 00:25:09 | METOP-B | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 81aee446-d9c5-3fdd-999d-09aea72117d4 | -19.8613 | -44.087299 | 2024-10-07 00:25:09 | METOP-B | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 21b24f6a-0c57-3b68-87ef-e1ea6355e780 | -19.554199 | -42.7341 | 2024-10-07 00:25:09 | METOP-B | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1bc3278d-ab89-3a15-bea8-9e05e0bde91c | -19.555901 | -42.741501 | 2024-10-07 00:25:09 | METOP-B | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1fc2d8cd-1b5e-3d6b-a242-a51c407b1c4c | -19.6535 | -43.181 | 2024-10-07 00:25:09 | METOP-B | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 5f29c3aa-aeb9-3a9f-a47a-499c3b545705 | -19.7981 | -43.842201 | 2024-10-07 00:25:09 | METOP-B | SANTA LUZIA | MINAS GERAIS | Brasil | 3157807 | 31 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README5.md)
