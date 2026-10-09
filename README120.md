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

## Dados Diários - Página 120

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8819065a-a489-3eb3-bb7c-f3ad0e405dfb | -15.63632 | -39.18173 | 2026-10-09 04:29:00 | NOAA-21 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 087f9401-a56e-3671-b809-13cc31c510f4 | -17.96841 | -44.34872 | 2026-10-09 04:29:00 | NOAA-21 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 704d84da-b58c-3041-a78a-e4811a5af431 | -15.10806 | -43.63223 | 2026-10-09 04:29:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ddd6740c-47e3-3a64-8524-8ac66f70460d | -16.51941 | -42.51529 | 2026-10-09 04:29:00 | NOAA-21 | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f3dc2c1-e5b5-30cb-8782-7bd00169df19 | -15.25802 | -42.36598 | 2026-10-09 04:29:00 | NOAA-21 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 6239cff4-d5e6-3629-ada1-0ac859ba5cd8 | -14.94562 | -48.1029 | 2026-10-09 04:29:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9720926b-2ff6-3308-9133-09906dabfdb8 | -14.35136 | -55.02942 | 2026-10-09 04:29:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1198d00a-4ebf-345e-beca-1e5f403c2f48 | -16.52151 | -42.51326 | 2026-10-09 04:29:00 | NOAA-21 | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 753b4691-ce8a-3156-903d-5161049d7b13 | -18.47843 | -42.24895 | 2026-10-09 04:29:00 | NOAA-21 | NACIP RAYDAN | MINAS GERAIS | Brasil | 3144201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 6a80ae92-92c9-32f7-a786-12c7808c115d | -14.87669 | -50.3021 | 2026-10-09 04:29:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| adf3cd26-5acb-3521-8266-0d4fbaf016a8 | -18.33283 | -42.37565 | 2026-10-09 04:29:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| e820d484-7660-3f93-95a4-357715e12f55 | -15.94944 | -41.08337 | 2026-10-09 04:29:00 | NOAA-21 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 77208c52-dcd3-3efb-a38f-790d2ad81b6f | -17.88017 | -45.98527 | 2026-10-09 04:29:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e8008580-cf7a-39ee-aecb-b7e4a0c88b75 | -17.01506 | -51.89585 | 2026-10-09 04:29:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 40a2b430-eab6-3bb7-a21c-d93598b1f083 | -15.56146 | -44.51247 | 2026-10-09 04:29:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 53413b19-958a-3f80-a84b-38d82456df7d | -18.64315 | -41.34944 | 2026-10-09 04:29:00 | NOAA-21 | MENDES PIMENTEL | MINAS GERAIS | Brasil | 3141504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 05937a0b-1972-35dd-b9ed-497670c83ba6 | -16.88291 | -40.70995 | 2026-10-09 04:29:00 | NOAA-21 | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| eff962e0-6635-3dfd-bb39-5a2ae7fff520 | -16.96815 | -41.23281 | 2026-10-09 04:29:00 | NOAA-21 | MONTE FORMOSO | MINAS GERAIS | Brasil | 3143153 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| f6ffc4ed-27de-3ee9-8d78-521e784f9113 | -17.17814 | -51.7496 | 2026-10-09 04:29:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6ad0266d-895c-3850-a97a-2dd07a882f7a | -14.96701 | -47.54213 | 2026-10-09 04:29:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| bb642f88-fdac-3d50-a6d0-5ce59c3b892b | -20.32311 | -42.01751 | 2026-10-09 04:29:00 | NOAA-21 | MANHUAÇU | MINAS GERAIS | Brasil | 3139409 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 712ed7ea-9ee2-3476-a18f-8f9983c73aa7 | -15.34388 | -50.58174 | 2026-10-09 04:29:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b25cad8a-a776-31a3-96c3-0c5c3e02d64a | -16.53578 | -52.74483 | 2026-10-09 04:29:00 | NOAA-21 | RIBEIRÃOZINHO | MATO GROSSO | Brasil | 5107198 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 429776a1-d94a-3d09-a8b8-1598695ca57f | -15.95412 | -41.08442 | 2026-10-09 04:29:00 | NOAA-21 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| ccd60c0c-3a4f-3a97-bba0-01487a2a233f | -15.94882 | -41.08873 | 2026-10-09 04:29:00 | NOAA-21 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| f785df70-4c5e-335e-acf2-15170b205a0a | -15.25513 | -42.36754 | 2026-10-09 04:29:00 | NOAA-21 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| c63c6d0c-a939-37ba-aa14-3470cd18de8c | -14.92746 | -48.11091 | 2026-10-09 04:29:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 38c63adc-dc4a-369a-8bc0-dc6247d4d2f8 | -14.35405 | -55.0327 | 2026-10-09 04:29:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8651dd40-e47b-32ba-9739-4295e55d6377 | -17.02719 | -41.06284 | 2026-10-09 04:29:00 | NOAA-21 | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| af223aaa-3114-3f62-997c-79caae68e27a | -15.42821 | -43.24561 | 2026-10-09 04:29:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 59e04500-0731-335b-89e0-548b19f8bcfb | -15.63632 | -39.18172 | 2026-10-09 04:29:00 | NOAA-21 | CANAVIEIRAS | BAHIA | Brasil | 2906303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| fdc99e5c-5d34-36e9-ac90-b1c043e464d7 | -8.7234 | -45.1355 | 2026-10-09 04:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 59.5 |
| e5228649-d00d-3e9e-87ab-32c72b90cc9a | -3.1101 | -54.1661 | 2026-10-09 04:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 3e7de8ea-924d-3767-a1c5-7eb90647a979 | -11.3103 | -44.8337 | 2026-10-09 04:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 238c7a48-50a7-35cf-ad3f-a8a6c71c105f | -3.5676 | -54.6946 | 2026-10-09 04:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| a8b9e48c-e9a4-3582-b0a6-1e91b5a783b1 | -3.0007 | -53.9075 | 2026-10-09 04:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 2d3588e2-3b99-30f6-8891-fa05268af27c | -3.1285 | -54.1657 | 2026-10-09 04:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 357b824e-3a23-37a4-9d13-45c930d530ee | -3.0925 | -53.9455 | 2026-10-09 04:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 8aab8fd3-0831-377e-ad56-163c2046dbdc | -7.3909 | -44.7445 | 2026-10-09 04:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 57.0 |
| ed33799c-2b7f-394b-8ce3-c60feb5cf667 | -13.1827 | -54.3571 | 2026-10-09 04:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 27ab4b6f-49a5-3a60-ba5e-89454490908b | -9.297 | -47.4313 | 2026-10-09 04:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 99.9 |
| cd9953ed-67b4-3030-978e-3128ed9844a3 | -13.1636 | -54.3591 | 2026-10-09 04:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 6247bd5b-f1fc-3116-a36f-ec786150de33 | -8.9687 | -45.1542 | 2026-10-09 04:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 95.8 |
| fa2d852c-468f-3584-a4c4-768e01e46467 | -8.7423 | -45.1334 | 2026-10-09 04:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 69.3 |
| a3491e90-430c-313a-8b96-cb1ceebf923a | -2.499 | -56.0675 | 2026-10-09 04:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| f5eeb494-6f61-3938-a71f-1635b55d643b | -2.8047 | -58.2841 | 2026-10-09 04:30:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 71.4 |
| cdb7c025-69b9-364b-94da-bd04897be830 | -3.1109 | -53.945 | 2026-10-09 04:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 72c194aa-7be2-3003-99dc-890604dc2ab6 | -2.7428 | -54.1146 | 2026-10-09 04:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| e92076ef-0b00-3e9b-acf9-2fb75af826dd | -3.5677 | -54.6746 | 2026-10-09 04:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 5a40f663-2df8-324c-bfd7-fff589129905 | -4.7404 | -55.672 | 2026-10-09 04:30:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 0f982b54-3018-3f86-a5dd-ae700493ab7e | -22.76796 | -49.3581 | 2026-10-09 04:32:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c533cfe9-0e1e-36ee-9ade-b221e669d3ab | -21.97418 | -55.93326 | 2026-10-09 04:32:00 | NOAA-21 | PONTA PORÃ | MATO GROSSO DO SUL | Brasil | 5006606 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0df2cd93-00ad-3873-b288-be229538f1ab | -22.76407 | -49.3613 | 2026-10-09 04:32:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0b6ca0f9-57f4-3709-861a-e5e89e2200fe | -22.99009 | -48.65749 | 2026-10-09 04:32:00 | NOAA-21 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d10173bd-0df2-3865-a9df-33d763f03df4 | -20.7477 | -51.66203 | 2026-10-09 04:32:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 15ea5045-e90b-34bc-9695-a2b7914449d2 | -22.7674 | -49.36189 | 2026-10-09 04:32:00 | NOAA-21 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c282b9cb-6b5c-3aa7-94d2-a7608eab7c72 | -3.5677 | -54.6746 | 2026-10-09 04:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 9dcd1901-4027-3593-9032-3f20552125a3 | -13.1636 | -54.3591 | 2026-10-09 04:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| ca21e4c3-e28f-394c-820d-873fe7a51fdb | -3.5676 | -54.6946 | 2026-10-09 04:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 37edbb04-166d-30fc-a694-6e5cf4b8f8bf | -3.1285 | -54.1657 | 2026-10-09 04:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 71.0 |
| d2151c8f-9778-38f3-a3f2-d35d3296949f | -3.0007 | -53.9075 | 2026-10-09 04:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 7d4c3cf8-3f2f-3209-aac4-c6675e731810 | -3.1101 | -54.1661 | 2026-10-09 04:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| ad8e457d-76d7-3af9-b15c-e1b016294de4 | -4.7404 | -55.672 | 2026-10-09 04:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 6c571703-c3a2-3dfc-98fa-a6f5f1a2d581 | -2.823 | -58.2838 | 2026-10-09 04:40:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 990b1cf6-03bf-3113-9712-16fb1561d9f7 | -13.1827 | -54.3571 | 2026-10-09 04:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 3e728b92-76ea-3194-b22b-49791dfcd4a5 | -3.1114 | -53.7839 | 2026-10-09 04:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 98520563-3741-385b-b3c4-3436e7eb7241 | -2.7428 | -54.1146 | 2026-10-09 04:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| add300bb-ade8-3714-a9a6-67584149da2d | -3.1109 | -53.945 | 2026-10-09 04:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| ee065114-7310-347a-a433-15630694c1ef | -3.0925 | -53.9455 | 2026-10-09 04:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 14ef6c64-c88d-38f9-9178-b5986124b7e0 | -2.499 | -56.0675 | 2026-10-09 04:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 5c732158-bf5b-3e61-8f69-6d7d82225c21 | -2.8047 | -58.2841 | 2026-10-09 04:40:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| a9a5f2fb-ddf9-34d6-940a-8792133cbbdf | -2.499 | -56.0675 | 2026-10-09 04:50:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 1ff119d9-194b-36ac-a5e6-435b5a843e7f | -2.7428 | -54.1146 | 2026-10-09 04:50:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| c355a4cc-342c-3935-8e6e-080f76367129 | -3.1114 | -53.7839 | 2026-10-09 04:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 30f9beae-f36a-3165-bcae-9828cb9a20f6 | -3.5493 | -54.6951 | 2026-10-09 04:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 7c64ed39-878c-3c69-b1d5-3e8697cd4215 | -3.0007 | -53.9075 | 2026-10-09 04:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| dd64c26d-19cb-3b56-aff1-8d73dff70ec6 | -3.1101 | -54.1661 | 2026-10-09 04:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 4a41f46e-dee9-3ccf-94ee-b856a4075c51 | -2.8047 | -58.2841 | 2026-10-09 04:50:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| aa2c5b8e-b3dd-3cdd-95b9-dbe73d080a87 | -3.5676 | -54.6946 | 2026-10-09 04:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| f8eb8b0a-cb13-3cbc-b3ad-9f2223124b99 | -3.1285 | -54.1657 | 2026-10-09 04:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 471e4dbc-c81e-3ad0-83d0-0941552048e9 | -3.0925 | -53.9455 | 2026-10-09 04:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 21796094-6bc8-3b55-b401-b0b3915e4033 | -2.8047 | -58.2841 | 2026-10-09 05:00:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| a5a31604-b150-359c-a4e0-534de32147c2 | -2.499 | -56.0675 | 2026-10-09 05:00:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| dbb62774-7b5b-3d9b-b431-f70c9d3e477a | -2.03058 | -55.62866 | 2026-10-09 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c0f55d14-8eb7-3c1c-8b1c-00255de990c3 | 0.0565 | -49.99093 | 2026-10-09 05:01:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 942a6ab1-25a4-3fc6-a8c9-3427bbc387ee | -3.34684 | -50.48101 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7ae77369-e4eb-3b45-a8a4-66ed0518e0f7 | -3.19084 | -50.58501 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a5bbadb2-d7db-37d3-a838-27c34f25323f | -2.48628 | -56.17116 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a1f17f35-8033-327b-b41e-4b348c26d745 | -4.07752 | -44.11924 | 2026-10-09 05:01:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4b2eb847-ab61-3fff-b360-2001f291c5bd | -0.08262 | -49.48847 | 2026-10-09 05:01:00 | NPP-375D | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fb0e947f-a14f-3b0b-9cc4-cc4c6496cd4d | -2.842 | -54.07016 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1b471421-889b-3949-99ee-108dc3ed43ff | -3.17961 | -50.59055 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 31489f92-a5e4-309a-8636-396c86b626a2 | -2.7425 | -54.1068 | 2026-10-09 05:01:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 60220f89-6cd2-393e-8a1c-ca03ef384df8 | -2.8267 | -51.28181 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| b1d1f9c7-8c82-3b35-afa5-152d2a15b417 | -2.50607 | -56.12379 | 2026-10-09 05:01:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 62382977-8eae-3468-ba61-61a5378afb14 | -2.82392 | -51.27782 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b24af828-168b-3a4c-9b2f-8ae0d1a6d82c | -1.32367 | -55.44112 | 2026-10-09 05:01:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4d71d8a2-9e72-3b14-bd8b-f698606ba2fd | -3.19758 | -50.56418 | 2026-10-09 05:01:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 947851dc-4b4e-3cfe-81fe-25b3e732bb3b | -1.15041 | -54.22387 | 2026-10-09 05:01:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b36c80cc-c6e2-39b2-96e4-272e45f34517 | 0.51959 | -50.7738 | 2026-10-09 05:01:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README121.md)
