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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 94be645a-c5ef-3208-8c3b-774905d1b4bd | -3.586 | -54.6941 | 2026-10-08 03:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| e6fb2265-50d4-352c-8f7d-391604feaf76 | -3.1786 | -50.6016 | 2026-10-08 03:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| eb6c3609-e985-3c20-902c-c33aa414b4ac | -2.4031 | -57.9041 | 2026-10-08 03:30:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 9488f872-40b1-368a-9e61-c154513049fd | -2.572 | -56.1646 | 2026-10-08 03:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 60e3b540-9eec-3779-be84-e20b829b0c9e | -10.4337 | -47.2824 | 2026-10-08 03:30:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 371ddcbc-92bf-36fc-9c62-1a30706e785d | -3.5861 | -54.6741 | 2026-10-08 03:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 202e3442-58d5-3b1d-943b-2bd4ae262069 | -5.7117 | -53.4862 | 2026-10-08 03:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.6 |
| b749c443-9715-37a9-9bdd-8161d488056c | -4.3471 | -43.8021 | 2026-10-08 03:30:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 68.7 |
| ec269758-2272-3c77-8bc2-91a616af4c78 | -3.531 | -54.6757 | 2026-10-08 03:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 1c6bae38-08e6-3fac-b93e-dc890d0605e8 | -9.0592 | -65.9209 | 2026-10-08 03:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 41.0 |
| a8963065-af40-3761-a46c-26905c68addf | -9.0591 | -65.9396 | 2026-10-08 03:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.6 |
| f83cf085-a22c-3b07-9619-5d594aa7970f | -2.4987 | -56.1659 | 2026-10-08 03:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| fdf47e53-cb0b-3dea-8523-c7e1cf36bd7e | -6.6319 | -43.7068 | 2026-10-08 03:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 47.2 |
| ef25e881-9f33-32bc-a99a-f8e23217dcef | -2.7796 | -54.0937 | 2026-10-08 03:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 87e8ecd5-7cbd-3b1b-9e68-bdbe56b314bf | -3.1101 | -54.1661 | 2026-10-08 03:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| f71e3e0d-3928-3441-9b41-e87b233a71e1 | -5.6932 | -53.487 | 2026-10-08 03:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 8a5ad55f-34dd-3a47-aea9-017eb5c3b263 | -2.4988 | -56.1462 | 2026-10-08 03:30:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 218ced2c-3588-39bd-80eb-bdd776918877 | -3.9662 | -56.1316 | 2026-10-08 03:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 684c50a0-55f5-32e0-96ec-739bcb6fef76 | -3.531 | -54.6557 | 2026-10-08 03:30:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| b7fa67ef-db6e-3336-8f06-7e0a24d8d3c6 | -3.1114 | -53.7839 | 2026-10-08 03:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 05c720cb-8193-3154-8660-e1bd67be6805 | -3.5865 | -54.5742 | 2026-10-08 03:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 39.3 |
| 4a525ca1-cee7-30e7-92b7-7ce561fcce01 | -2.7796 | -54.0937 | 2026-10-08 03:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| cd0f5043-c846-3bd4-a758-41c34d556c57 | -2.499 | -56.0675 | 2026-10-08 03:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 45.0 |
| dd40f654-8513-3d65-908e-416ed5022d9d | -9.0592 | -65.9209 | 2026-10-08 03:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 36.3 |
| 3dcab198-bdc5-36a7-a3fa-421961070b8b | -3.1101 | -54.1661 | 2026-10-08 03:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 0f0d59a5-ceca-3643-bc5c-d8db774eb013 | -5.6932 | -53.487 | 2026-10-08 03:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 2a4a5c9a-76b9-3ea7-a87d-1da02d1dc5fc | -6.1431 | -47.9214 | 2026-10-08 03:40:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 483c2137-a7d2-3ab6-a28b-3675fe3f386e | -3.11 | -54.1862 | 2026-10-08 03:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| b8c5dc35-c992-314e-a16a-9e67ab41c5c9 | -3.1972 | -50.5592 | 2026-10-08 03:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 0a95517d-f04c-3a78-a809-85762ddb19d1 | -9.0591 | -65.9396 | 2026-10-08 03:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.5 |
| d5422186-bd99-348d-b25a-570804a2c62e | -3.9662 | -56.1316 | 2026-10-08 03:40:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 0177207d-33f3-32c9-be7c-ae63d78848e2 | -3.1114 | -53.7839 | 2026-10-08 03:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 3949f304-5a56-3914-9991-410d1c4a0e43 | -7.0065 | -59.1223 | 2026-10-08 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.2 |
| dba5fcf4-ccf3-33bd-a8e5-df326d9ce512 | -2.7797 | -54.0736 | 2026-10-08 03:40:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| d06b28a6-5698-3b9b-88bd-f7a2f0b4afeb | -2.4987 | -56.1659 | 2026-10-08 03:40:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 42d6f447-969d-3f42-8018-026f7a068002 | -3.5493 | -54.6752 | 2026-10-08 03:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| a2b7abd5-6dc8-33bf-a715-b595a43f97ab | -6.1429 | -47.9432 | 2026-10-08 03:40:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 7bde666a-20b1-3b0a-8103-a2adb37cf559 | -3.5861 | -54.6741 | 2026-10-08 03:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 93745a21-01ce-39b5-8b11-d1c1cdad368f | -1.5306 | -54.5558 | 2026-10-08 03:40:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 35.1 |
| d65ad97d-f7b9-3c90-b006-1108717c8c14 | -3.531 | -54.6757 | 2026-10-08 03:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 6a3dac25-280f-3757-a4a3-fe41448fc326 | -6.6315 | -43.7533 | 2026-10-08 03:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 8ed277f1-b17e-3031-9f83-fd26c12e395e | -8.7228 | -45.1812 | 2026-10-08 03:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 104.0 |
| 8fe8f827-3142-3a9e-814a-164132a60a76 | -3.586 | -54.6941 | 2026-10-08 03:40:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| b3811794-b638-37ac-929b-8cdff0cd092c | -8.6107 | -67.0301 | 2026-10-08 03:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 776f2ecf-6f0f-349a-bdd8-142541e0dd45 | -8.7231 | -45.1583 | 2026-10-08 03:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 95.0 |
| a207462a-5c00-39bf-ba45-2785dad793e7 | -6.6317 | -43.73 | 2026-10-08 03:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 8ff2f46f-d7b3-3fff-adcd-812678d76659 | -3.1697 | -58.6437 | 2026-10-08 03:40:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 21.8 |
| f1057296-7310-36fe-864b-05bcbecdf030 | -8.742 | -45.1563 | 2026-10-08 03:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 62d63ecd-90ac-3106-842f-ab8bb288c228 | -5.7376 | -45.1533 | 2026-10-08 03:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 046477e4-7fdb-3f89-a062-e7ffa5efb524 | -3.0913 | -54.287 | 2026-10-08 03:40:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 6d367a81-02fb-386b-8e93-0ce3ad8e1ef7 | -3.1786 | -50.6016 | 2026-10-08 03:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 20e35b5c-96fa-3fb2-bab0-911349703c1d | -3.9663 | -56.1119 | 2026-10-08 03:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 11000f19-2f64-35f6-a0f0-576694e00544 | -2.4031 | -57.9041 | 2026-10-08 03:40:00 | GOES-19 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 22.5 |
| a084ef6f-b968-3f8d-a303-6b8e408415a0 | -4.3471 | -43.8021 | 2026-10-08 03:40:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 103.8 |
| 73eb2463-d7d0-3fe5-9dae-6b7680848366 | -4.01429 | -38.25417 | 2026-10-08 03:40:00 | NPP-375D | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2b34e6cc-65a3-3089-ab7f-3d4a5cdd2ef5 | -4.01567 | -38.25245 | 2026-10-08 03:40:00 | NPP-375D | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0af85a59-a36c-3f79-a1fb-1b3932df5677 | -5.75589 | -42.07075 | 2026-10-08 03:42:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ca920275-ee74-3668-a13e-fd541033776d | -5.75298 | -42.05375 | 2026-10-08 03:42:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0807d25a-87db-3276-add3-48c6c095b65f | -4.72708 | -37.84303 | 2026-10-08 03:42:00 | NPP-375D | ITAIÇABA | CEARÁ | Brasil | 2306207 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 54e3f5a4-870f-3fe0-b32b-d569cce968fd | -6.92499 | -43.66201 | 2026-10-08 03:42:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 78023ace-a36f-3dbf-a968-9632a34b7de1 | -8.73096 | -45.17759 | 2026-10-08 03:42:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 57f37a65-2c79-3e3e-b529-7d0ef756a898 | -8.22079 | -46.34451 | 2026-10-08 03:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 57cd8b1f-dd56-3bee-958d-3749a90832ac | -9.86195 | -36.49651 | 2026-10-08 03:42:00 | NPP-375D | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9ca99afd-f14a-394c-a7a4-d55f79a25d52 | -8.71436 | -45.19207 | 2026-10-08 03:42:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.3 |
| b1641605-ec39-39f0-b354-90009673ca21 | -7.59903 | -42.38407 | 2026-10-08 03:42:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| bf187e3a-671a-36e5-b640-f285094ea0cd | -6.62371 | -43.7338 | 2026-10-08 03:42:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 57f82c4c-7dd1-3e31-9c04-e8476dbbab71 | -5.95896 | -40.92712 | 2026-10-08 03:42:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d8fb01dd-d443-317d-af94-285518984e03 | -6.95477 | -45.25949 | 2026-10-08 03:42:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 226f0931-41d6-3e98-87f3-d07e03d84dd8 | -6.94231 | -45.28725 | 2026-10-08 03:42:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cde1de60-be07-3741-af18-7cd0deec03ee | -8.73443 | -45.15971 | 2026-10-08 03:42:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| a0138e8e-fa6d-3745-a06e-a08bfbbe2856 | -6.89001 | -43.6947 | 2026-10-08 03:42:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 09fca9b8-cc26-36dd-837e-c3e4fa555863 | -4.34888 | -43.79714 | 2026-10-08 03:42:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| a301b8a5-7d7e-38a6-89e2-fd8f9172e39c | -8.22322 | -46.34503 | 2026-10-08 03:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a025424a-7fab-3894-a223-b71fddf28358 | -6.62463 | -43.72886 | 2026-10-08 03:42:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 47cec630-7e01-32fd-b3f1-0e58a14d183b | -7.46706 | -42.84459 | 2026-10-08 03:42:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 47e1f2fc-aeb1-30a4-a656-70c7e3fd6019 | -5.76167 | -42.07167 | 2026-10-08 03:42:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 48bf2171-c9b4-3b04-9733-13df57e4a6b6 | -8.74216 | -45.15536 | 2026-10-08 03:42:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 718aeb6d-e5c5-3a86-95a0-7855ef7d32e6 | -6.92835 | -43.66174 | 2026-10-08 03:42:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| a1355c98-8447-37a9-8a26-911ae675c784 | -6.15232 | -39.43653 | 2026-10-08 03:42:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 981a9c49-3461-3ddf-84b7-154fb556488b | -6.82729 | -39.54999 | 2026-10-08 03:42:00 | NPP-375D | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| bf2bd84e-b5aa-3790-b571-6706e04631f3 | -6.9018 | -40.91394 | 2026-10-08 03:42:00 | NPP-375D | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9336a9a0-f56d-3b7c-a8e6-cf978a31740d | -9.79193 | -37.3221 | 2026-10-08 03:42:00 | NPP-375D | PÃO DE AÇÚCAR | ALAGOAS | Brasil | 2706406 | 27 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7382ae87-4b85-36b3-adc1-43104ad96c44 | -6.61492 | -37.90244 | 2026-10-08 03:42:00 | NPP-375D | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4ccfa8b0-5d9d-30ec-bdeb-9a7d38521a2c | -8.73558 | -45.15379 | 2026-10-08 03:42:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 10.2 |
| ff059b2e-8ff3-3b89-8bb0-22cccf78676c | -9.56416 | -40.34052 | 2026-10-08 03:42:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| d89678df-6244-39c5-a0c5-eb75bce48648 | -5.77026 | -42.0568 | 2026-10-08 03:42:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6aa4dcf2-2a1c-31e3-a2e7-e6b55304aae3 | -6.36718 | -42.90701 | 2026-10-08 03:42:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c85daa78-88e4-30ba-bb69-44d072219d36 | -5.71593 | -41.72832 | 2026-10-08 03:42:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| f8ec20e4-915c-38cb-ac61-dec88cb9dacc | -6.8665 | -39.11016 | 2026-10-08 03:42:00 | NPP-375D | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 910941a6-d232-3d94-99f2-f11f1e945b1c | -6.94146 | -45.29329 | 2026-10-08 03:42:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c01a85a4-80a7-38a1-8024-6ef0d533e68d | -6.99221 | -40.03649 | 2026-10-08 03:42:00 | NPP-375D | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| dca1602e-56ef-3bc8-a952-4661518f60fa | -4.35541 | -43.79845 | 2026-10-08 03:42:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 7e9e95bf-aa7c-3fd3-9282-3f3a8e4e9bec | -6.62907 | -43.7401 | 2026-10-08 03:42:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 43.6 |
| b8e4f06d-395a-3d5d-bbe9-07a078b670b0 | -5.48439 | -42.85109 | 2026-10-08 03:42:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 3989c829-d70f-34c4-bc7d-b5605bda672e | -4.35443 | -43.80415 | 2026-10-08 03:42:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 8c4b956c-92cd-3311-924b-6561afdb863c | -8.21898 | -46.32916 | 2026-10-08 03:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b2a3bee9-b6e0-3ba3-b5e2-22bca87e6e31 | -6.63183 | -43.72517 | 2026-10-08 03:42:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 390093d3-5650-3baa-9295-c6155d7215b4 | -5.48525 | -42.84634 | 2026-10-08 03:42:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 1e3fb35f-2a81-3e2d-b264-14f72e0bfbcb | -10.24792 | -36.33732 | 2026-10-08 03:42:00 | NPP-375D | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 468b8a35-82af-3638-adbb-569d23c86735 | -7.2293 | -44.27748 | 2026-10-08 03:42:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README56.md)
