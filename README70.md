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

## Dados Diários - Página 70

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 77a8f039-a2ee-35e2-80f9-169446f47875 | -17.00383 | -41.17167 | 2026-10-09 03:47:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| ede72897-c33e-3a52-b3a4-deb28c476507 | -18.63482 | -41.348 | 2026-10-09 03:47:00 | NOAA-20 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 93c9d017-4483-326d-b079-e8e237bb6e79 | -16.12563 | -43.74287 | 2026-10-09 03:47:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7143466a-f1e7-3ec2-a864-3d169a81e758 | -17.02731 | -41.06474 | 2026-10-09 03:47:00 | NOAA-20 | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2d17756c-36b5-3161-9feb-5b59260cd951 | -16.89614 | -40.89863 | 2026-10-09 03:47:00 | NOAA-20 | FRONTEIRA DOS VALES | MINAS GERAIS | Brasil | 3127057 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f3eb9f1b-4048-37a9-926f-d99f75040d60 | -17.28541 | -41.2196 | 2026-10-09 03:47:00 | NOAA-20 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| dbdb8719-ef41-3642-8b86-8eb0e278f8b6 | -16.96184 | -46.35667 | 2026-10-09 03:47:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fba4cd48-eb11-3ab3-bf30-a134ac643b32 | -15.10781 | -43.63546 | 2026-10-09 03:47:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 8d81bb82-37de-39d2-8182-38f00d03c84b | -17.25417 | -39.4703 | 2026-10-09 03:47:00 | NOAA-20 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| bf97869d-c171-3d11-8dae-ed1aaa83c505 | -16.11967 | -43.74813 | 2026-10-09 03:47:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0cec64bc-b38b-3cfe-992e-96ccfe0d1ed1 | -18.47568 | -42.25259 | 2026-10-09 03:47:00 | NOAA-20 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 49dd39aa-7065-30a7-a27f-9483e1012b66 | -18.47986 | -42.25304 | 2026-10-09 03:47:00 | NOAA-20 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| be517aff-ec43-30f7-b1f1-9ca61c7a15f9 | -17.96575 | -44.34787 | 2026-10-09 03:47:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 612103dc-16b3-3b41-96b2-2516b5f7edac | -16.92641 | -42.1143 | 2026-10-09 03:47:00 | NOAA-20 | ARAÇUAÍ | MINAS GERAIS | Brasil | 3103405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d945349d-bd8e-3b46-965e-f08b3ec9ac90 | -18.63478 | -41.3498 | 2026-10-09 03:47:00 | NOAA-20 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 1ce6dbb1-c309-32ee-952b-424ad6a4586b | -16.12401 | -43.74598 | 2026-10-09 03:47:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b979d779-9212-331a-a4e9-633b4b510d2f | -15.78703 | -44.68409 | 2026-10-09 03:47:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 661dcde7-6c34-35d2-82d1-4217d8201477 | -15.78642 | -44.68714 | 2026-10-09 03:47:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f08a061d-af45-367c-b18c-0908adee402e | -16.85252 | -40.56147 | 2026-10-09 03:47:00 | NOAA-20 | BERTÓPOLIS | MINAS GERAIS | Brasil | 3106606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f4c683e3-c3e2-320c-b4bf-cb5fd8950dce | -18.63776 | -41.35399 | 2026-10-09 03:47:00 | NOAA-20 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8dd16c30-7a32-3784-9eaa-5635c379ad93 | -16.1274 | -43.75398 | 2026-10-09 03:47:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| abcb1f6b-a993-35a1-b178-c9ac34b879e7 | -16.58719 | -46.75809 | 2026-10-09 03:47:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fe299d1f-d08f-3142-9847-6142ebb234bb | -18.47742 | -42.25381 | 2026-10-09 03:47:00 | NOAA-20 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| e952cdcd-919c-38b5-bcdb-1d640dc0ec1a | -15.45191 | -45.43946 | 2026-10-09 03:47:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 18161f00-78ab-3c79-b928-c755624bb248 | -15.42859 | -43.24977 | 2026-10-09 03:47:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 241e5b38-74b7-3de9-8c1a-2702acbfc7df | -16.96859 | -41.23017 | 2026-10-09 03:47:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| c3bfde44-1345-3cc7-aad2-f324f4a4790e | -15.10677 | -43.64079 | 2026-10-09 03:47:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6c64229d-9a9f-3f82-a160-6c064886ec4e | -18.62995 | -41.35268 | 2026-10-09 03:47:00 | NOAA-20 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| bc47d3ee-0161-325e-b7e8-f3a84866d43b | -16.58179 | -46.76534 | 2026-10-09 03:47:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| acca0f55-a139-31da-a6c8-c00ae8961d2c | -16.58834 | -46.76248 | 2026-10-09 03:47:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fada079f-4b90-3c15-aaf3-ccd8968a9ce9 | -15.44808 | -45.44528 | 2026-10-09 03:47:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5a16888e-b683-3b81-a8de-612aa11adc35 | -18.63576 | -41.3446 | 2026-10-09 03:47:00 | NOAA-20 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 1d786ec0-4645-3efd-b437-c04d95b0c3d5 | -20.12996 | -40.33895 | 2026-10-09 03:47:00 | NOAA-20 | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 005b0e21-ed6b-37ad-a962-59db075c5712 | -14.9402 | -48.09867 | 2026-10-09 03:47:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 68255684-a9a3-37e0-a2d9-89c7755a79ec | -16.96366 | -41.2347 | 2026-10-09 03:47:00 | NOAA-20 | MONTE FORMOSO | MINAS GERAIS | Brasil | 3143153 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c49bb508-a6a9-3ffa-bc3b-7db4e834ca0e | -18.08418 | -42.26432 | 2026-10-09 03:47:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| 29903552-8441-363e-a9c6-9caa06cc67a1 | -16.57981 | -46.76509 | 2026-10-09 03:47:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a21afd56-036a-3de1-b1f5-12ea2f1c837a | -18.32384 | -42.37804 | 2026-10-09 03:47:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 27.4 |
| 66802e23-f97e-38c7-b76a-191e77a4b4b9 | -18.78677 | -46.46893 | 2026-10-09 03:47:00 | NOAA-20 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4072532a-f3e8-32e1-9a8f-7dac6abb04ae | -15.44948 | -45.43851 | 2026-10-09 03:47:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 31f6dcf5-2e72-3696-a3e9-f82fe5f1ee63 | -18.47816 | -42.24982 | 2026-10-09 03:47:00 | NOAA-20 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 7c4faaba-9810-3593-a930-71891c60f6f2 | -18.63962 | -41.34371 | 2026-10-09 03:47:00 | NOAA-20 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 047a3266-3785-3d19-a97b-6342c39879c7 | -18.05374 | -44.59796 | 2026-10-09 03:47:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 71aea62a-ec71-3a86-92e8-a91d3f70a83a | -14.87087 | -50.30742 | 2026-10-09 03:47:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1ef59637-2577-3ca9-bf41-2547c91e1efc | -15.98572 | -44.85754 | 2026-10-09 03:47:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 52df32fa-0df4-3b0c-9377-1ed211e22631 | -18.6387 | -41.34877 | 2026-10-09 03:47:00 | NOAA-20 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| fd12d377-959e-3341-81d5-4dfde072300d | -17.51935 | -39.51784 | 2026-10-09 03:47:00 | NOAA-20 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ef4bd130-c74c-39f3-a404-688c871b81df | -16.58923 | -46.75833 | 2026-10-09 03:47:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b1cdb984-de6c-31be-86fb-764d049d234a | -16.51979 | -42.5141 | 2026-10-09 03:47:00 | NOAA-20 | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f17743a8-5781-3032-b108-6ad49f240417 | -16.99198 | -41.1695 | 2026-10-09 03:47:00 | NOAA-20 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 03f0f0f8-2763-383c-a7f7-232f5768077c | -18.08274 | -42.27194 | 2026-10-09 03:47:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| fc956194-8d6b-3d0e-99e9-1254d5a7a635 | -19.09036 | -43.99348 | 2026-10-09 03:47:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3f0ee9bd-e949-30f1-9aaf-668116d2532a | -15.56619 | -44.51738 | 2026-10-09 03:47:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a590734f-3bd3-33ec-86b2-f134c98efff5 | -15.94617 | -41.08863 | 2026-10-09 03:47:00 | NOAA-20 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| fdb485c9-19d8-3291-a67b-726bc77a1bd0 | -18.64163 | -41.35487 | 2026-10-09 03:47:00 | NOAA-20 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cd12cfda-f50c-31a2-b882-2bfdf8e89795 | -18.78066 | -46.4714 | 2026-10-09 03:47:00 | NOAA-20 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5e4281e3-8b01-37ae-8b6b-24ed1c9164d8 | -15.95022 | -41.08911 | 2026-10-09 03:47:00 | NOAA-20 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2deb5da0-2095-3288-8fe1-bfe5d0502be4 | -16.84871 | -40.5607 | 2026-10-09 03:47:00 | NOAA-20 | BERTÓPOLIS | MINAS GERAIS | Brasil | 3106606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e41a6a83-931c-355b-9761-497838f13d24 | -18.3288 | -42.37455 | 2026-10-09 03:47:00 | NOAA-20 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 27.4 |
| 9671ec1b-5e11-3dcf-92bf-6b66453128ea | -17.51234 | -43.68167 | 2026-10-09 03:47:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 99f6a227-bcca-3770-bf73-edce4ad506c5 | -16.58633 | -46.76221 | 2026-10-09 03:47:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3e27009e-a117-32cf-950b-d32db98bc919 | -15.56121 | -44.51617 | 2026-10-09 03:47:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3a0bb879-7491-3959-a61a-626b0c8cab0d | -16.58267 | -46.76127 | 2026-10-09 03:47:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b38b42d-79bd-3b89-9b88-72c04905eb7e | -15.42492 | -43.24382 | 2026-10-09 03:47:00 | NOAA-20 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 588a3ffe-76f8-3230-b6f8-9bdc3c9b9e0a | -15.49366 | -44.41355 | 2026-10-09 03:47:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 54550ae8-30e6-303a-a206-3727d9e6b55a | -18.08274 | -42.27195 | 2026-10-09 03:47:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 65d5b99b-029c-31cd-844e-e0258310b145 | -15.78702 | -44.68409 | 2026-10-09 03:47:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 527093c3-0b4f-330a-a258-1193f82ad342 | -16.88129 | -40.70983 | 2026-10-09 03:47:00 | NOAA-20 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4c71023c-7f83-34e6-b762-8ad1d01ded7a | -15.10677 | -43.6408 | 2026-10-09 03:47:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 2bef2ded-e419-3668-bc55-04ff9c6e27d7 | -15.10304 | -43.63444 | 2026-10-09 03:47:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 48a82c54-4ca5-3df6-be47-ad8f25808896 | -15.44525 | -45.44504 | 2026-10-09 03:47:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 94fc9aea-785c-3a6c-af96-9607aa4dc943 | -18.05374 | -44.59797 | 2026-10-09 03:47:00 | NOAA-20 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 96aec62c-6842-3217-98ec-5b099a13397d | -19.99342 | -49.09271 | 2026-10-09 03:47:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e79c2316-f348-3b3e-b42a-11c63262775a | -15.1078 | -43.63546 | 2026-10-09 03:47:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 9f88a959-e230-33a3-8ab7-98b8c825f4ee | -17.97021 | -44.34817 | 2026-10-09 03:47:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 546cbd64-9932-3b9e-a410-d686dc367c52 | -16.58834 | -46.76249 | 2026-10-09 03:47:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7819e279-959e-3382-99a4-e5755bda2f3a | -18.78677 | -46.46894 | 2026-10-09 03:47:00 | NOAA-20 | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 81045b80-ae76-3b64-8da5-c95aeed8d5b0 | -15.10201 | -43.63978 | 2026-10-09 03:47:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 2f0ee88d-2dee-390a-bdf5-b5fe006345ee | -18.47644 | -42.24861 | 2026-10-09 03:47:00 | NOAA-20 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 313c15c5-2558-36c8-a766-a7cf4d0a932c | -17.51935 | -39.51785 | 2026-10-09 03:47:00 | NOAA-20 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 81847572-e71b-311e-bd3b-a851bff1e472 | -17.93594 | -43.9556 | 2026-10-09 03:47:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d4110cdb-f685-39d9-89ce-d7edab586da3 | -18.63963 | -41.34541 | 2026-10-09 03:47:00 | NOAA-20 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 66c9e30a-2f27-38ed-86c9-d9f0ec5da78b | -15.95021 | -41.08911 | 2026-10-09 03:47:00 | NOAA-20 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 4e7abd39-e13d-3126-b80a-85f78349f208 | -16.57981 | -46.7651 | 2026-10-09 03:47:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ed4c208-046f-3732-904a-f7d1dc4627ed | -15.38576 | -41.89316 | 2026-10-09 03:47:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| efe6def5-38e1-3bdf-a2f0-50cea08b965b | -17.25416 | -39.4703 | 2026-10-09 03:47:00 | NOAA-20 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| b36e40ce-4492-37c9-bb87-c9a8d9a0e752 | -13.1827 | -54.3571 | 2026-10-09 03:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 23703459-74c7-3108-b1dd-bef9b4c81da9 | -2.7428 | -54.1146 | 2026-10-09 03:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| f1d5c34f-df31-3684-a53f-60c9b26e4a26 | -2.823 | -58.2838 | 2026-10-09 03:50:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 48.3 |
| bc41bdb9-72e2-3251-872b-bc7d5e051866 | -8.9113 | -45.2062 | 2026-10-09 03:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 4ed66145-90d5-34d6-bf29-892e390f484d | -7.218 | -55.1617 | 2026-10-09 03:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 2119e21c-0eb4-36d2-9272-9d73071b984f | -3.5676 | -54.6946 | 2026-10-09 03:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 73bcc2ef-d3e1-3087-8fc2-021baa6987f9 | -6.8907 | -45.8988 | 2026-10-09 03:50:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 5cfb1b46-1aef-3d4f-b8f0-ec3ab584aa8f | -11.3103 | -44.8337 | 2026-10-09 03:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 135.4 |
| ea358b29-e1a3-302c-b0f8-2e2a4b8a6b1b | -8.742 | -45.1563 | 2026-10-09 03:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 40.0 |
| fbb4508d-bac7-38ae-868f-742a4be25c5f | -8.7423 | -45.1334 | 2026-10-09 03:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 758beb8f-9ae9-31a0-a231-5228d2bc9dd5 | -3.1101 | -54.1661 | 2026-10-09 03:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| fa1d6361-b0f5-3800-8fc7-31446d78b518 | -6.0021 | -40.9594 | 2026-10-09 03:50:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 695.4 |
| e9b04630-b7ff-3a5f-b942-653efb25041f | -7.2182 | -55.1416 | 2026-10-09 03:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 34.2 |
| 8a590842-1aa1-3966-bc76-c6be2fec7a35 | -7.1995 | -55.1627 | 2026-10-09 03:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |


[Clique aqui para ver as próximas entradas](README71.md)
