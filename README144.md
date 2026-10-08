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

## Dados Diários - Página 144

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8741c26d-ac0c-3225-86d6-0014029096eb | -3.24798 | -56.80555 | 2026-10-08 05:23:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b136aaa2-01f7-3bab-9966-395d8fb43e19 | -2.5874 | -56.16987 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2fd81e8d-e770-3617-8516-211ac3a443cc | -3.02274 | -54.06549 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c5298a77-b9ec-3a3d-9fb8-23e08eb4fc15 | -3.07286 | -59.26957 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| accde722-dc74-3937-8012-bb33613ad69c | -2.89948 | -54.02269 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ffc6516-42c4-3b2c-ab3e-e4f163c54605 | -3.06704 | -54.24481 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 270abe44-e1b5-30c7-916d-854c5dc922a7 | -2.99263 | -54.14395 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 80326438-169c-3aef-916e-3b2f27f1d736 | -5.19869 | -48.21328 | 2026-10-08 05:23:00 | NPP-375D | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7fa12c78-a688-34a8-9d0c-545c08279776 | -7.16466 | -47.78426 | 2026-10-08 05:23:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe231ec1-9abf-3a13-8761-a50d1894e7cd | -4.30703 | -54.79795 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf3bcdf7-83e5-392b-82ae-5455f2c06a14 | -4.36282 | -55.64527 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fc25605f-2f88-3dbf-a676-f995557d5f8c | -2.7751 | -54.06004 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 765a8830-9a5a-3d6e-a121-d549ddad2ebf | -3.07867 | -54.23886 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ec4213e-bbe3-31ea-bf42-777f7f442328 | -2.86914 | -54.19569 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9eb58464-1bba-322b-b49e-d9ef9dda74f2 | -2.76974 | -54.09475 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 64dd6ab3-3e56-3806-a27e-3b0336f722b5 | -3.32565 | -58.15431 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 117e8512-18dd-3b1d-80db-974755e87dc2 | -1.71466 | -55.44276 | 2026-10-08 05:23:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5335b4b2-de69-3209-bf07-61d0c699e353 | -3.18266 | -58.65488 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7962f0fc-cde2-31d8-ab0d-e3be76e9e9de | -4.10728 | -54.4112 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3be09ef5-7d86-3dc3-bd42-ed1c29b9e1e8 | -3.10837 | -53.7722 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 574f4999-de5c-341d-87f4-6774b5e71577 | -4.06921 | -59.84457 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 24438999-f2e7-32a4-b986-6be6faa9cfc1 | -2.10443 | -52.06035 | 2026-10-08 05:23:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 504c6fa5-884f-39ac-b583-4b2307ac7ac9 | -2.9974 | -54.11309 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 88645908-532b-3e1a-9acf-1a90b4f2314b | -2.8816 | -54.88054 | 2026-10-08 05:23:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 955a26d3-3c45-3f1f-89c6-93d5bee5f123 | -3.09832 | -53.76653 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6c0ea84c-40b3-3e43-a2b6-661f7fcb0ef8 | -10.49737 | -51.93736 | 2026-10-08 05:23:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 831aae2b-111e-30ed-bbb6-bbd9c3c53e23 | -5.26696 | -55.95574 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a735a16-e31b-3106-89e4-04dabd6d151b | -2.99817 | -54.06167 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b2aa755-a6aa-3b99-9ce2-51c047a1d756 | -3.29572 | -54.68756 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0840da9-fd9b-304e-96ad-0334c1e1be7b | -3.27081 | -54.04606 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e05fe6ed-44be-3e7d-9478-362dcf18e37f | -3.10866 | -54.16075 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| c495b492-8a04-3720-9ffc-6e12387349a2 | -3.16039 | -54.72774 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ad92134-a2cf-38bd-b215-23059770a00b | -3.03663 | -59.11419 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d8c5d538-0064-3469-9b20-8d0c65d1bf4c | -4.09657 | -53.9918 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ca30893-6e04-3bde-af9e-af528656c142 | -3.21667 | -53.88538 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65bbb547-351c-33a1-88c0-ad082fc47441 | -2.98029 | -54.03519 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a25d44ed-047d-3b15-ba3d-a01987bdad98 | -4.5687 | -54.95967 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8c4d7b6d-e60c-3d14-ad1c-872e65042691 | -2.56913 | -56.17763 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5754f205-49a1-3db5-a94e-cc7af426d89d | -3.37029 | -58.20243 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e54e3811-0497-34d5-b783-e4ce666948e5 | -2.99585 | -54.05335 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a646c894-c3e7-3545-abb8-b47d0a8dc8ce | -3.18282 | -50.55097 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2e269b5-adc7-3abb-a186-7a3a70b6a082 | -4.25224 | -56.3573 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 009f25b3-e87b-3b16-98cb-a7249408a480 | -4.11587 | -59.8777 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1d7b3a11-986a-3d2b-b6af-ba51c1dc5ce0 | -3.5421 | -50.10303 | 2026-10-08 05:23:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 24cf6c66-d501-3e64-90bf-a7b4809752ad | -3.28117 | -59.20773 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 61fe239a-ca8c-3fb1-8490-3046ea098d47 | -3.52507 | -54.64997 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c21f1384-e5a6-3164-bd1a-46895097a49d | -7.19152 | -55.13139 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e963ae8a-65df-372b-bd66-3e4572f05c68 | -4.16059 | -56.3182 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 81ae0a50-0604-3f3a-b581-d618f767b5bb | -4.95916 | -55.11641 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1bc07b44-cebe-3c4d-9ccc-af3d604473ff | -3.11318 | -53.76479 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 912780a7-eafb-3bc6-aae6-e0f76e090cdb | -3.76859 | -59.40304 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 819ba55d-1275-338e-9dca-2b7914ae6cab | -2.32692 | -57.97962 | 2026-10-08 05:23:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 388a8069-c889-38a2-ab6b-b258b2b9d490 | -2.72006 | -57.46542 | 2026-10-08 05:23:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7d75f474-489c-3e6e-9004-1a403071c5da | -3.81183 | -60.47593 | 2026-10-08 05:23:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| abf1738d-77ff-31ae-8905-b65a69e86c17 | -3.29458 | -54.00961 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 37c8c909-7c1d-3e7d-b0fe-5244dbf6f63c | -2.50802 | -56.16114 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 2e83dc56-b893-3b04-b415-3c81893b94a6 | -3.7407 | -59.44904 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2bad4a57-bbc7-3a6b-9fbc-cd29d75dbe60 | -8.72787 | -45.17709 | 2026-10-08 05:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a396b987-eb74-3017-bb7d-87d2b9d7bf54 | -3.08677 | -54.25578 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 027e6fce-9417-3e89-8505-3b6812e2a8c2 | -2.04804 | -56.20201 | 2026-10-08 05:23:00 | NPP-375D | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ed7e521c-6ae4-3973-9324-63faec979853 | -7.18918 | -52.62793 | 2026-10-08 05:23:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6144b0d0-2b30-319b-95c2-929218cdcd14 | -2.92251 | -54.1056 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f0ace9bc-d73d-3728-8aac-660659c4a533 | -3.02844 | -54.09811 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 71220b24-576f-3161-ab7b-f3dc41071a70 | -2.938 | -54.05251 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 7c38310b-c376-38a9-8e90-47b1165a5d02 | -10.88511 | -49.14677 | 2026-10-08 05:23:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6dc8d70d-fb86-3c42-8ee7-6e2fc3ef3bb8 | -2.8154 | -58.28887 | 2026-10-08 05:23:00 | NPP-375D | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c0550102-1b72-3977-9e25-a53c4b8952b0 | -5.25727 | -60.17612 | 2026-10-08 05:23:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a6a634a-b020-3ecb-a244-008f5ed42c3a | -2.77555 | -54.10352 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c3c6c751-b974-3919-9c57-ffcaa3d8e991 | -4.66059 | -56.21831 | 2026-10-08 05:23:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 440198fd-832a-3faa-9123-7207377091bd | -7.37836 | -55.20578 | 2026-10-08 05:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c88a0c3e-a621-3c8c-96b2-fd03b36e57e3 | -3.55861 | -59.47449 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d73f0991-85b5-3824-b43f-4abba09f6bd8 | -8.72115 | -45.17646 | 2026-10-08 05:23:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b4a961c1-f893-3870-aa9c-ee6386eae28d | -4.06109 | -55.32346 | 2026-10-08 05:23:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab807b45-2408-3847-ab92-bc7a1d0789b3 | -2.80303 | -54.0881 | 2026-10-08 05:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 858b2275-82f5-3f7d-b3b5-0cfb4f85d4fe | -3.33128 | -58.16265 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9785e92b-62cf-318a-aa45-1c90b7ff017d | -3.20077 | -50.54951 | 2026-10-08 05:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 41e5ec63-bcbd-33a1-a16c-6825d8ea8e0e | -6.68082 | -55.09974 | 2026-10-08 05:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b7fc0dff-8a2a-319c-adc6-bfef6aeedf2a | -3.51869 | -54.6681 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 768bec31-653a-3250-8d39-7519c1013aa2 | -2.86511 | -59.23871 | 2026-10-08 05:23:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9c271a5d-461d-355c-8f9c-3cdedf891f8d | -1.52315 | -54.81618 | 2026-10-08 05:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 01959f8c-63ea-3a25-834c-9abf0f6571e9 | -6.22697 | -55.62055 | 2026-10-08 05:23:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 617a514b-fec5-36d5-ac73-71c82fcf1a91 | -4.3575 | -43.79498 | 2026-10-08 05:23:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 15a7d695-c3c9-3302-96b5-93f276fb3925 | -3.31598 | -54.05706 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8790ee9a-196b-30a2-a329-97e3657f01a9 | -8.06245 | -44.80423 | 2026-10-08 05:23:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 35bf86e7-801a-3135-b97e-98213045acde | -3.72614 | -54.65697 | 2026-10-08 05:23:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 426a8914-7432-3b72-931b-8ae6ac1b6811 | -2.49341 | -56.05964 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 95c09139-eab1-3127-a925-d28eaf927109 | -6.954 | -45.25975 | 2026-10-08 05:23:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5757afb5-3486-3897-8bd6-f8f0acf13f06 | -2.49615 | -56.34333 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9cfa3eb5-0e2f-30ed-82e2-2d1a122d72fa | -4.26625 | -46.39492 | 2026-10-08 05:23:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8cd848d5-e3b5-3de9-ad2a-d949f08b3fa3 | -3.30418 | -54.06324 | 2026-10-08 05:23:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 66412663-efe4-3b98-99d6-1000e58693a1 | -9.5846 | -65.25116 | 2026-10-08 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 63168648-548a-394f-ba85-be901e6f4e5e | -9.48978 | -64.35029 | 2026-10-08 05:23:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d9d0afe4-9e0c-33d3-86bd-72b878ad99bc | -4.42894 | -55.16105 | 2026-10-08 05:23:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e6b17d3b-984c-3617-bddb-85bdb0727eb1 | -9.12089 | -67.8267 | 2026-10-08 05:23:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 953794eb-b202-3fd3-85a8-8351f5a85240 | -2.49017 | -56.10167 | 2026-10-08 05:23:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a36e45a1-a692-3f2a-a8bd-0379dd4a61e6 | -3.05517 | -54.22451 | 2026-10-08 05:23:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e925d896-da58-388c-9b88-95d53c4b1dbc | -4.11949 | -59.87827 | 2026-10-08 05:23:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a95f9935-6893-33b0-a41d-a7ad1158e8b3 | -3.03479 | -54.52223 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37a81328-37d7-3b83-9a5e-cbb4c6b330c6 | -3.07796 | -54.28959 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5b6d9c15-721c-3264-9173-c32068528f07 | -3.25194 | -54.28059 | 2026-10-08 05:23:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README145.md)
