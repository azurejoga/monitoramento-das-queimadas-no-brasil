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
| 133e9387-dd1e-3ec5-af21-979acd429793 | -8.87254 | -49.5373 | 2025-09-12 00:11:00 | TERRA_M-M | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 23.5 |
| f9e9e4de-a72b-3757-b266-a50f92e62e60 | -5.59741 | -42.91434 | 2025-09-12 00:11:00 | TERRA_M-M | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 4e604f96-97e3-3c66-b46a-6c38d77e272a | -10.57696 | -47.21279 | 2025-09-12 00:11:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 47ee9546-ade3-39b0-ac0d-ff50ea4c9338 | -6.11123 | -45.93336 | 2025-09-12 00:11:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 9f249b36-d30a-3fa1-b807-3f7eddd2ac78 | -5.79582 | -43.88657 | 2025-09-12 00:11:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 3b911b86-b33a-3a1c-b61a-ead0f8c70f30 | -8.95223 | -46.72216 | 2025-09-12 00:11:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| a06ade30-38ef-3ce9-a049-b5d560038026 | -5.52766 | -44.33851 | 2025-09-12 00:11:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 4443b339-a2d0-376f-83ee-5290469f57c0 | -9.01635 | -46.12395 | 2025-09-12 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| a0ef5dc8-bfc5-34a1-ac20-937b2b471b09 | -12.58372 | -45.69329 | 2025-09-12 00:11:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 6806c182-d482-3389-bd4b-28522a943811 | -8.04517 | -44.49441 | 2025-09-12 00:11:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 16bc2feb-e58c-3472-837d-5b9537535ebb | -10.70709 | -48.63294 | 2025-09-12 00:11:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 806f042d-2d8c-3662-a9c6-90c217d0379f | -8.15059 | -39.89264 | 2025-09-12 00:11:00 | TERRA_M-M | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 4f770d5b-c11f-37ac-95a5-729b4811e9d7 | -6.18469 | -43.4957 | 2025-09-12 00:11:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4b1c9a34-00d6-382c-a767-ccf57eba89fe | -6.46567 | -44.93686 | 2025-09-12 00:11:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 43.2 |
| fcc10777-47b8-3861-b011-82780c416c4f | -8.25719 | -49.9348 | 2025-09-12 00:11:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| 22dcbed9-b201-3e92-931e-b25f6d86a9b2 | -5.82895 | -45.26835 | 2025-09-12 00:11:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| e7bd441c-aacd-387f-855d-691fa1d237d3 | -9.07495 | -46.95541 | 2025-09-12 00:11:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 9c411f8a-e1be-3257-b7c1-9dd8bd5e04fe | -6.30328 | -42.23497 | 2025-09-12 00:11:00 | TERRA_M-M | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 20.3 |
| 0b16b278-aabf-3d2d-a40f-9cd47b739a20 | -11.74949 | -48.28492 | 2025-09-12 00:11:00 | TERRA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| fe5a124e-589d-3be9-88c9-6ca055f9b6e6 | -6.13991 | -43.36728 | 2025-09-12 00:11:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 178956ae-17a4-32c3-91ed-31138e938fc2 | -6.1683 | -43.50699 | 2025-09-12 00:11:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| a88a75e8-7a92-3ff4-8f44-0278b6c6a898 | -6.097 | -45.94167 | 2025-09-12 00:11:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 3cb5c49d-b609-304e-8440-5b7795ab579e | -8.93926 | -46.08345 | 2025-09-12 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 74cd9307-2a4d-385e-83eb-e7f08ebe610f | -10.48465 | -49.38035 | 2025-09-12 00:11:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 59a75a6c-92bc-35f2-9f82-75b842fd6167 | -9.10816 | -47.1253 | 2025-09-12 00:11:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| ed37e5f9-c2c8-3383-a719-408c3ee83dc1 | -10.42262 | -50.60181 | 2025-09-12 00:11:00 | TERRA_M-M | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 28.7 |
| f03c47d9-2d03-3832-9ea9-95f779582f71 | -5.83023 | -45.27785 | 2025-09-12 00:11:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 1350100f-f8af-33f8-a3a0-1c55aede91fa | -7.44574 | -44.4241 | 2025-09-12 00:11:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b39400bb-d96b-313c-bea2-89731bda1e7a | -6.44916 | -44.07555 | 2025-09-12 00:11:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| bcabdbb5-6732-352b-87ad-1814862497ec | -6.71072 | -42.05046 | 2025-09-12 00:11:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 25.8 |
| 02d9ddc4-c715-38ce-8629-68d2a44f766a | -7.52672 | -44.67878 | 2025-09-12 00:11:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8757a1a3-ff96-39a8-b02b-3945d6521766 | -8.19677 | -46.10643 | 2025-09-12 00:11:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| ece97af1-bf3c-3565-ae35-1dd69b97a787 | -6.28171 | -42.40723 | 2025-09-12 00:11:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 3600e3f1-ddff-3f28-ab2c-36ed75f6ac3a | -5.3169 | -43.88583 | 2025-09-12 00:11:00 | TERRA_M-M | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d9a8bf6a-c05f-3750-bfc1-dce3d841d5ae | -7.52799 | -44.68817 | 2025-09-12 00:11:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 98a990aa-0522-3e47-8673-39fbbf14c79b | -6.84406 | -47.86367 | 2025-09-12 00:11:00 | TERRA_M-M | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 7463c56a-e24c-3221-bd6f-02cdb3febf4f | -6.82898 | -52.79299 | 2025-09-12 00:11:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| dea197cd-25d0-3028-9cb5-2c4adbda4e7d | -6.4879 | -43.88385 | 2025-09-12 00:11:00 | TERRA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 1725fd4f-870f-36c1-bfbb-94d2283132c3 | -6.67841 | -44.13986 | 2025-09-12 00:11:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 895ff433-389b-3dcb-974e-d52c9925a6d9 | -5.65398 | -45.95515 | 2025-09-12 00:11:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| fcf7c3b9-12e0-3dd0-bcb7-42c448dc8232 | -11.6957 | -46.55501 | 2025-09-12 00:11:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 19.0 |
| a7ba8006-29ae-3464-9130-3b86e3f96be8 | -5.86221 | -48.16131 | 2025-09-12 00:11:00 | TERRA_M-M | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 17.0 |
| a2c423f0-d2b4-3e6e-883c-9e0e753d1ba8 | -11.68975 | -46.54956 | 2025-09-12 00:11:00 | TERRA_M-M | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 123.2 |
| c54217d8-8155-3bff-9356-f592a7422010 | -5.76315 | -45.52274 | 2025-09-12 00:11:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6f52e8ad-8d9c-38f3-86fa-9bee3283356b | -9.77609 | -47.85204 | 2025-09-12 00:11:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| b2e25a9b-4878-36db-9c11-3342032922a7 | -6.1018 | -45.93466 | 2025-09-12 00:11:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 4fea48d4-69d8-3352-95a4-1b37733a6b48 | -5.69902 | -44.39013 | 2025-09-12 00:11:00 | TERRA_M-M | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| cfa5b092-491d-31c9-873a-8d5e7c6774fb | -11.42622 | -43.55248 | 2025-09-12 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 9d76ad60-9493-39a2-887c-26ad9ca7bed3 | -6.18168 | -42.74812 | 2025-09-12 00:11:00 | TERRA_M-M | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 17b40bab-b145-3e34-b8e1-32cef85cff01 | -11.98334 | -51.14825 | 2025-09-12 00:11:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 127.7 |
| b7cfaa4b-9197-33ee-bb25-0cea4c3c76a0 | -6.11965 | -42.96363 | 2025-09-12 00:11:00 | TERRA_M-M | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 14.9 |
| a3a3d689-a559-3918-9ba2-ee80c800e09e | -6.48911 | -43.89269 | 2025-09-12 00:11:00 | TERRA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| f6952a0c-1552-34a2-891c-25ce7850d20c | -8.56336 | -45.623 | 2025-09-12 00:11:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 31daa9df-d3a1-3ec4-b987-70df0a3a6b51 | -11.97124 | -51.18058 | 2025-09-12 00:11:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 5391f745-4628-3620-84ed-192495923d71 | -6.59325 | -44.32224 | 2025-09-12 00:11:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e6482680-4d93-360c-bc79-f0ab1d612e06 | -6.15383 | -42.61416 | 2025-09-12 00:11:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 21.9 |
| f05c4e80-fadb-3f08-bcf5-dbb2a779ceff | -12.18897 | -40.89204 | 2025-09-12 00:11:00 | TERRA_M-M | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 85c01a81-892e-3efd-97bb-0290b512b49c | -4.47658 | -38.72084 | 2025-09-12 00:11:00 | TERRA_M-M | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 4f0886e6-cdab-3438-a987-776ae5bf3bc3 | -6.10315 | -45.94485 | 2025-09-12 00:11:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 8b02ebac-deb9-3979-ba54-d3db0cbb4c92 | -11.53085 | -41.91132 | 2025-09-12 00:11:00 | TERRA_M-M | IBITITÁ | BAHIA | Brasil | 2913101 | 29 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 0d1803fc-1c7b-3d02-b243-c45bb3516a83 | -9.06384 | -47.11744 | 2025-09-12 00:11:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 75e6503b-d32e-3cf0-b606-b7ffc5c3d929 | -9.71633 | -48.30301 | 2025-09-12 00:11:00 | TERRA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 5e7eda71-fd95-3921-89bc-db072a3af67a | -8.42858 | -47.25744 | 2025-09-12 00:11:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 7c11d2af-99eb-3f7f-ad5a-960e18c980f7 | -6.66954 | -44.14103 | 2025-09-12 00:11:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 75d18f8e-820e-3108-9128-f0bb391c4630 | -8.95203 | -46.10415 | 2025-09-12 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 5f4f9994-f9af-3822-86d1-bd9fe3ff81cc | -11.46179 | -43.61328 | 2025-09-12 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 09f97cac-544c-36f1-ab79-447f9db6b03e | -10.74515 | -48.19379 | 2025-09-12 00:11:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 37.0 |
| a014d8ba-bc97-302a-94ea-664695b9aef6 | -9.49771 | -48.66356 | 2025-09-12 00:11:00 | TERRA_M-M | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 9e6f6c92-8877-34d2-ae8d-d3920f6ee4e2 | -11.74273 | -43.37073 | 2025-09-12 00:11:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 65f9e9fa-90cd-3b71-a555-ef93b19e2feb | -12.60103 | -45.67279 | 2025-09-12 00:11:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 315f3c93-ad6f-3d94-9867-fbf1fdda842e | -11.88446 | -41.27864 | 2025-09-12 00:11:00 | TERRA_M-M | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 22.9 |
| 137821bf-7a4d-3efe-becb-66e69669583d | -12.92831 | -48.00295 | 2025-09-12 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| fc28ca38-90e3-3ff0-9353-2aa4b310de71 | -8.07229 | -42.95414 | 2025-09-12 00:11:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 21.5 |
| 03be40db-a278-3053-b6d0-d9fdcc037df8 | -5.88634 | -43.93916 | 2025-09-12 00:11:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| a7ca8718-4216-38da-9858-b5780d869eff | -8.18303 | -42.42574 | 2025-09-12 00:11:00 | TERRA_M-M | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| b2f90e8f-95a4-37e9-bb15-e02a2b7f3f6d | -12.58218 | -45.68134 | 2025-09-12 00:11:00 | TERRA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 61.9 |
| f3fb6a10-4f98-3b9e-aff4-343eb36953be | -11.14618 | -45.24133 | 2025-09-12 00:11:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 8d3e800a-c6d7-3924-bfd5-332bce98b2fb | -11.99735 | -47.76444 | 2025-09-12 00:11:00 | TERRA_M-M | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| b89f9b1d-714b-37da-9e75-21eea018d287 | -8.94911 | -46.08205 | 2025-09-12 00:11:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 39444bdd-22ab-3d1c-a0a8-4b5169f2f556 | -6.22433 | -43.37638 | 2025-09-12 00:11:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| b5885768-5014-39b7-8a26-ffc00330f4ce | -6.28049 | -43.18202 | 2025-09-12 00:11:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 8a035edd-82da-3bcb-9c9a-259de564b0bd | -6.17711 | -43.50574 | 2025-09-12 00:11:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| c36a81ed-2ed9-3d9d-9662-d2ee9d12a547 | -8.18701 | -46.10785 | 2025-09-12 00:11:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 42db770a-3ebb-3718-80cf-273147cf6eb1 | -6.68832 | -44.13264 | 2025-09-12 00:11:00 | TERRA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f03044ea-41e3-378e-840d-1811f80f7ff9 | -6.26637 | -43.22637 | 2025-09-12 00:11:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 798c58ba-0b48-3514-adbf-50698b07ab6c | -11.43764 | -43.56961 | 2025-09-12 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.2 |
| f6447845-0296-3046-85e0-0a2de0b64143 | -10.59991 | -43.02686 | 2025-09-12 00:11:00 | TERRA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 696f63ae-65ec-35d1-bff3-c06e442588db | -7.40871 | -50.66399 | 2025-09-12 00:11:00 | TERRA_M-M | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 712492b4-85b0-334b-83f8-ff172b7dd447 | -6.24474 | -44.80149 | 2025-09-12 00:11:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| d50fcd32-cc52-356c-ae86-cb43262c56d6 | -7.46374 | -44.41568 | 2025-09-12 00:11:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 4f21c68a-9057-398e-a3c8-e4976931254b | -6.19318 | -42.70055 | 2025-09-12 00:11:00 | TERRA_M-M | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 34a67bdd-5c70-3782-a749-df0d75befed9 | -7.3181 | -49.64166 | 2025-09-12 00:11:00 | TERRA_M-M | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| ce5fc1fb-7157-3fa0-87a4-464bc198cc43 | -7.54295 | -44.39519 | 2025-09-12 00:11:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| edf69d50-0c0f-35a9-8c91-165d54e6f0ed | -9.69384 | -47.56345 | 2025-09-12 00:11:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 6a0537dc-aac2-3851-b247-a8dc15496616 | -11.48947 | -49.27691 | 2025-09-12 00:11:00 | TERRA_M-M | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 21.7 |
| d458a350-c10a-319b-98df-adce2e3a453c | -10.70481 | -48.61411 | 2025-09-12 00:11:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 2901e63a-7c93-348f-888a-02286f37ef33 | -11.97134 | -51.1547 | 2025-09-12 00:11:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 804cd69d-c0e2-3eff-921c-cae695cf1240 | -9.03068 | -45.75628 | 2025-09-12 00:11:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 01919321-8c93-31e1-9cd5-38f57a5ba773 | -5.79704 | -43.89538 | 2025-09-12 00:11:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 7ae69c4f-7542-355f-82f2-5c6af8bbb95a | -6.38119 | -43.51841 | 2025-09-12 00:11:00 | TERRA_M-M | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |


[Clique aqui para ver as próximas entradas](README5.md)
