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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ad506de7-668e-305b-bb68-4d4c6a144ee2 | -8.66153 | -62.81886 | 2025-08-31 06:33:00 | AQUA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 00dd8579-6d74-36f3-aba2-84b9c92aa41f | -8.74491 | -62.38471 | 2025-08-31 06:33:00 | AQUA_M-M | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 13.9 |
| ae9959df-a9e9-33ab-b157-026f6e90dac6 | -8.65863 | -62.83638 | 2025-08-31 06:33:00 | AQUA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 9efd57cf-ef24-3383-ad5c-9c12c4559d85 | -7.91948 | -63.0216 | 2025-08-31 06:33:00 | AQUA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 14.9 |
| e5efb09d-9779-34c8-814d-9d808e596982 | -7.91951 | -62.99727 | 2025-08-31 06:33:00 | AQUA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 466b9ba7-a109-3b71-a579-2c14ea608286 | -10.12862 | -58.01615 | 2025-08-31 06:35:00 | AQUA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| abe4d8bf-2db5-3251-9b0d-f4540b41b058 | -10.87858 | -55.76072 | 2025-08-31 06:35:00 | AQUA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 55b49362-ffed-3d9d-a55a-6ed4b2026ea2 | -12.80033 | -48.0712 | 2025-08-31 06:35:00 | AQUA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 00816a27-9a56-3bcd-a944-fc30bbe7e684 | -9.43727 | -60.57051 | 2025-08-31 06:35:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 25.0 |
| da9b41f0-3729-3af0-bc9d-87d4869c35ed | -9.43728 | -60.57617 | 2025-08-31 06:35:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 66a25dc4-1e4f-3a96-8b21-2c7fdb6b1e8c | -11.40905 | -63.2443 | 2025-08-31 06:35:00 | AQUA_M-M | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 1a3f2612-ea3c-3637-b321-5d334ec9f6eb | -9.44142 | -62.35467 | 2025-08-31 06:35:00 | AQUA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 79ff414b-e1eb-3784-8752-f8785250448c | -9.45546 | -62.34089 | 2025-08-31 06:35:00 | AQUA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 2eeee3e6-5645-396d-a032-9788d47203ae | -10.61162 | -54.91606 | 2025-08-31 06:35:00 | AQUA_M-M | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| f90e9ec6-ae36-3d40-8cd4-4ef72db1d6b6 | -9.44918 | -60.56608 | 2025-08-31 06:35:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 9fa02b7e-5c01-3ce3-ab91-79720fdaf860 | -9.69525 | -61.27846 | 2025-08-31 06:35:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| bbd25b55-5d23-341b-9695-023d0444e3ba | -10.31545 | -59.19602 | 2025-08-31 06:35:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 346cdcb1-f19e-3dd3-ab28-24c7f86c56b8 | -11.41904 | -63.23401 | 2025-08-31 06:35:00 | AQUA_M-M | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 173e3069-993f-36a1-b060-aedd40fb9bd8 | -12.93373 | -56.9812 | 2025-08-31 06:35:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 66cfe8c0-0302-308a-8067-713327eb29d3 | -11.41613 | -63.25092 | 2025-08-31 06:35:00 | AQUA_M-M | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 15.6 |
| caeb1538-3a5e-34c8-8856-90cc0a3e4e6a | -12.91591 | -56.97852 | 2025-08-31 06:35:00 | AQUA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 8d32a701-322e-3c1e-b9e6-63e742bf7be5 | -9.45286 | -62.35647 | 2025-08-31 06:35:00 | AQUA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 370313e2-b342-395d-afe1-287d3fbfba50 | -10.31393 | -59.2057 | 2025-08-31 06:35:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| dd9bea6f-9d43-3dc6-a860-b7577effdb42 | -9.43919 | -60.56448 | 2025-08-31 06:35:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 16.6 |
| a767a85c-3080-36e4-8097-164d7b3f8f62 | -9.44404 | -62.33902 | 2025-08-31 06:35:00 | AQUA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 14.8 |
| c4157d56-ef42-336c-8e61-d98b4ee9f734 | -11.41185 | -63.22735 | 2025-08-31 06:35:00 | AQUA_M-M | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 927c8035-65e0-32ee-9fd5-fdca9b8ff83e | -10.31697 | -59.18639 | 2025-08-31 06:35:00 | AQUA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 0baca3ed-5578-3713-9c93-2285854701ab | -16.21653 | -52.685 | 2025-08-31 06:37:00 | AQUA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 31.4 |
| cb9a536c-fdf9-3b6f-82f8-c4e9978323ee | -14.59723 | -54.55529 | 2025-08-31 06:37:00 | AQUA_M-M | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 0ad9afaf-4236-3ea2-a7b6-1f722bd4af9b | -15.71351 | -48.96532 | 2025-08-31 06:37:00 | AQUA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 72a42320-ec1c-3aef-ac04-59edd6ed9206 | -15.71109 | -48.90324 | 2025-08-31 06:37:00 | AQUA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 88b1433e-cc8f-3294-ad06-a7b40e28b28b | -20.68718 | -54.5832 | 2025-08-31 06:37:00 | AQUA_M-M | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 10.7 |
| e8d23e89-bd34-3773-be11-b43a065b889f | -15.70408 | -48.97194 | 2025-08-31 06:37:00 | AQUA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 81.4 |
| ebef19b6-bce3-365d-a2ed-0fbcc5a51ae6 | -15.72033 | -48.97365 | 2025-08-31 06:37:00 | AQUA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 8354b8dd-a30a-3f09-9f4d-e5fa95714a97 | -16.20651 | -52.66453 | 2025-08-31 06:37:00 | AQUA_M-M | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 234b91da-dcac-3a85-a4bb-f27e17121e49 | -15.7075 | -48.93842 | 2025-08-31 06:37:00 | AQUA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 2cb350c9-76e3-3269-a979-bf33bb836b18 | -15.7009 | -48.93004 | 2025-08-31 06:37:00 | AQUA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 47a759f9-58cd-37bb-b6be-094e90958841 | -15.72396 | -48.93856 | 2025-08-31 06:37:00 | AQUA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 86.4 |
| e7cfb3f9-dc14-332b-ab22-be42dee6b7fb | -14.79443 | -59.71817 | 2025-08-31 06:37:00 | AQUA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| c54fb943-f34a-3586-a969-3e6742cb87ef | -14.7929 | -59.72795 | 2025-08-31 06:37:00 | AQUA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2f4a3838-8ed5-3a6c-9189-ad404b6724f8 | -15.71715 | -48.93213 | 2025-08-31 06:37:00 | AQUA_M-M | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 89.3 |
| a37d85e3-1a0f-3d88-8c33-e21c806bd016 | -14.80334 | -59.72004 | 2025-08-31 06:37:00 | AQUA_M-M | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 9d546238-65b1-3764-9fee-ecf2d059b2ad | -15.7102 | -48.9479 | 2025-08-31 06:40:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 726d89f4-bd01-3b7a-a8e8-b8079f1305cb | -11.8956 | -46.3753 | 2025-08-31 06:40:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 62.8 |
| 66b5eb2f-e506-3b98-bdf3-26ed47aee778 | -11.4233 | -63.2444 | 2025-08-31 06:40:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 55.9 |
| bbf8a748-2aab-3cc3-84b2-e710580c717b | -6.1665 | -43.3273 | 2025-08-31 06:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 131.6 |
| ba490e1e-8f80-3e48-819b-f43e791ea08c | -6.1853 | -43.3257 | 2025-08-31 06:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 9dbb9f97-94ec-3968-b619-f3b1e4a18185 | -15.7294 | -48.9669 | 2025-08-31 06:40:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 12baf6e8-36e6-3281-bdb8-28f139b1b5fd | -9.4683 | -62.3476 | 2025-08-31 06:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 5723fe56-3fc5-3713-b4be-72fd63627fb8 | -9.4497 | -62.3485 | 2025-08-31 06:40:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 71.6 |
| cae0ad45-2f37-320d-b9da-b054ed621591 | -9.4432 | -60.5692 | 2025-08-31 06:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 44.8 |
| a5e1b513-df57-3b67-8cb2-edf7f8d7efb0 | -15.7298 | -48.9446 | 2025-08-31 06:40:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 07ed0c7b-6c73-3f9c-9fd8-429d36123bb2 | -6.1667 | -43.3039 | 2025-08-31 06:40:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 61.3 |
| 8c963c9d-ff8e-317a-a603-2f7d96702cbb | -15.7098 | -48.9702 | 2025-08-31 06:40:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 9029ad41-4231-37de-9770-1eb8f4130cf2 | -28.70919 | -55.63099 | 2025-08-31 06:40:00 | AQUA_M-M | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 13.4 |
| a2b66e35-4255-31fd-8161-792f398fe840 | -9.4497 | -62.3485 | 2025-08-31 06:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 74e80d60-cb51-3afe-a8e4-894de9c2fcbc | -15.7294 | -48.9669 | 2025-08-31 06:50:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 46774caa-125c-303a-bb10-f75a9e0ae868 | -9.4683 | -62.3476 | 2025-08-31 06:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 59.8 |
| 71b87fd4-9f5d-3f1b-891f-23ec127f9963 | -11.8181 | -46.4314 | 2025-08-31 06:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 8bb4c7b8-841e-30ad-a614-83cc3baab851 | -6.1853 | -43.3257 | 2025-08-31 06:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 5a8df3e4-769a-3bb6-ad6f-ad2b70a7f786 | -9.4432 | -60.5692 | 2025-08-31 06:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 44.0 |
| 78de00e4-dad8-3a99-9446-741143e60c16 | -6.1667 | -43.3039 | 2025-08-31 06:50:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 61.8 |
| c9bb47a8-2df3-32ed-aed5-1f8f577cb4be | -11.4045 | -63.2453 | 2025-08-31 06:50:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 7a15a64b-43f0-308a-9f46-bafb5276a650 | -6.1665 | -43.3273 | 2025-08-31 06:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 155.4 |
| a185a4d2-ab7a-3031-80f9-19d2b96dcd0f | -11.8956 | -46.3753 | 2025-08-31 06:50:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 12ce2203-54b7-3e83-bbc6-860a8e1af670 | -15.7298 | -48.9446 | 2025-08-31 06:50:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 4382ffa3-4290-33b3-979f-00edcb51ba15 | -11.4233 | -63.2444 | 2025-08-31 06:50:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 65.1 |
| ae693d76-86b5-3b4a-a004-deea27882c68 | -15.7098 | -48.9702 | 2025-08-31 06:50:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 77.5 |
| c12191d6-9e24-3c5b-8f0d-bba2f7b13624 | -15.7102 | -48.9479 | 2025-08-31 06:50:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 7396237c-9871-3c21-9505-3507fd5f6736 | -11.4233 | -63.2444 | 2025-08-31 07:00:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 124.9 |
| 318e5559-5995-3b6a-9e8e-bf97598e3e5a | -6.1667 | -43.3039 | 2025-08-31 07:00:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 50.8 |
| 7db506bb-5a78-3758-bf02-3e3aa5dde515 | -15.7102 | -48.9479 | 2025-08-31 07:00:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 5cc6e906-ecc8-3762-857c-3e4783fd1f3f | -6.1853 | -43.3257 | 2025-08-31 07:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 53.3 |
| e0e45c12-487d-393a-863d-94c05ec6f3a2 | -15.7298 | -48.9446 | 2025-08-31 07:00:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 78c84aac-599c-3635-959b-c7ec198c678b | -11.8181 | -46.4314 | 2025-08-31 07:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| b1ecdced-9a03-304d-8be7-c59adf3e6d2a | -9.4497 | -62.3485 | 2025-08-31 07:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 70.8 |
| ae762185-1ec9-31bd-bb4b-41a697f66c38 | -6.1665 | -43.3273 | 2025-08-31 07:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 147.4 |
| 9b1da5cd-e5a3-3bfe-af1d-d82af94c5e41 | -11.4045 | -63.2453 | 2025-08-31 07:00:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 8840c5d2-b9c1-3f62-a550-01e5146a8591 | -9.4432 | -60.5692 | 2025-08-31 07:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 46.9 |
| c8b9d095-6d9d-31a5-8246-037173b06846 | -11.8357 | -46.5194 | 2025-08-31 07:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 0592d199-e106-3237-ab35-3c29cfa6d992 | -15.7098 | -48.9702 | 2025-08-31 07:00:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 119f7e28-6337-3f47-a6a0-5512707a8429 | -9.4683 | -62.3476 | 2025-08-31 07:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 55.9 |
| aa76ce8c-27e8-36e0-a911-222322689cb2 | -6.5758 | -43.6885 | 2025-08-31 07:10:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 190be47e-0df6-37a9-9ef6-463585ca3fd3 | -15.7098 | -48.9702 | 2025-08-31 07:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 7af6c869-a774-362e-83c4-185147136ad9 | -15.7294 | -48.9669 | 2025-08-31 07:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 962ac3c7-19fe-3167-adec-85bd2d2c4ec2 | -9.4432 | -60.5692 | 2025-08-31 07:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 6a62301d-67ea-3962-8245-d7147a5f926f | -11.8361 | -46.4967 | 2025-08-31 07:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 0de3a55c-5fa0-3825-aa26-95731031c385 | -9.4497 | -62.3485 | 2025-08-31 07:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 4512f4b3-8cd8-384b-b7e4-91525f271fa3 | -11.8165 | -46.522 | 2025-08-31 07:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 72.7 |
| e0c21cfd-a5b4-350f-93ad-40e9e5dd30f5 | -11.8357 | -46.5194 | 2025-08-31 07:10:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 148.5 |
| 77462209-b8ff-352a-be29-916683367105 | -6.1667 | -43.3039 | 2025-08-31 07:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 42.9 |
| e2ccec79-835a-3906-a196-f3ad0d72d3ed | -6.1665 | -43.3273 | 2025-08-31 07:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 91.1 |
| d118034c-a79a-3b4f-b85e-e9d5454b33fd | -9.4683 | -62.3476 | 2025-08-31 07:10:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 56.0 |
| bc24d3a9-203f-3ae3-af59-103f04158b8f | -11.8353 | -46.542 | 2025-08-31 07:10:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 27c67f1d-4466-35b9-aa0f-6102017b627c | -6.1853 | -43.3257 | 2025-08-31 07:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 1b84ddf3-2804-3afc-a956-6ad2cf511c6b | -12.8621 | -48.0768 | 2025-08-31 07:10:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 2fcee535-8820-3c12-85fb-3299c20c8152 | -15.7298 | -48.9446 | 2025-08-31 07:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 2a1fe0a7-742b-3963-bd9c-b17de9b024a0 | -15.7102 | -48.9479 | 2025-08-31 07:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 8d04eeab-9660-3d8a-99c2-b5b1fb142940 | -11.4233 | -63.2444 | 2025-08-31 07:10:00 | GOES-19 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 53220496-be16-30a2-b1c9-f38ab02e1ae2 | -6.1665 | -43.3273 | 2025-08-31 07:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 94.9 |


[Clique aqui para ver as próximas entradas](README84.md)
