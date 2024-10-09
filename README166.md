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

## Dados Diários - Página 166

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dac0493e-01de-393f-8dd6-eb551ea61cc7 | -1.17044 | -54.14502 | 2024-10-09 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9992e820-5447-3d87-8ae8-d644dd4ded67 | -1.13982 | -54.21066 | 2024-10-09 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f987cfd2-dbf7-3f34-b582-e74dcfd86d39 | -1.13928 | -54.2141 | 2024-10-09 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 64c0818d-9722-3bfc-8ac2-b14a7208a059 | -1.13232 | -54.10738 | 2024-10-09 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| fb2e1c0c-e316-36f1-a69a-177f31bd3761 | -1.13106 | -54.22338 | 2024-10-09 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7e941a5-d6f7-3b91-b3ce-273adc6be744 | -1.13052 | -54.22682 | 2024-10-09 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f8d3290d-ce6e-3abf-9dc6-430bc12c5eed | -3.56912 | -54.3373 | 2024-10-09 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 21ebec04-fe07-3470-961a-9f1e02c44063 | -3.56858 | -54.34077 | 2024-10-09 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 32ba14dd-4c51-3aef-aceb-58a008ac9884 | -3.56804 | -54.34424 | 2024-10-09 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74870ad2-3e5e-3297-897f-f4a8736e2780 | -3.56702 | -54.02562 | 2024-10-09 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5d7ac0a-da25-3f17-8891-3d164c83fd9c | -3.56603 | -54.33681 | 2024-10-09 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3b5827cc-cfb8-356a-a30f-9f7d81984fcf | -3.56549 | -54.34028 | 2024-10-09 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8603a631-8805-39a1-bd92-988c046d8940 | -3.56494 | -54.34375 | 2024-10-09 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9eb0891b-8cbf-3a0a-a28b-33d3f82c1a38 | -3.5644 | -54.34722 | 2024-10-09 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 212e078d-dbdf-346c-aff6-518c239314a5 | -3.56271 | -54.33631 | 2024-10-09 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 62f41e98-4c70-3bda-aae6-09c54b965480 | -3.56108 | -54.34671 | 2024-10-09 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b9e2e161-91b1-33c4-a228-0e755c7fbc1f | -3.5583 | -54.34275 | 2024-10-09 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb0e757b-b669-3175-a965-7e51b137b66d | -3.55775 | -54.34621 | 2024-10-09 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 05a9c1b7-5580-3739-bfa5-7e865af0c079 | -3.55721 | -54.34969 | 2024-10-09 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 765e0072-0777-33af-9376-ca1f0f62484b | -3.53763 | -54.06071 | 2024-10-09 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b901f2bd-1b46-394c-9234-4065859544bf | -3.43875 | -54.06311 | 2024-10-09 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e963de6b-b09c-32e8-975c-9c2562a31d06 | -3.27866 | -54.17494 | 2024-10-09 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5a1b3ee8-2014-3c8e-a63f-3b132f0973c4 | -3.27533 | -54.17443 | 2024-10-09 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c0be84f9-4a92-3731-90f5-54dc6ec28ae2 | -3.27479 | -54.17794 | 2024-10-09 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d8c447d6-0373-321e-89d3-d1b10d266c4f | -3.26008 | -54.1861 | 2024-10-09 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 1b437f86-3343-3e26-b525-bed733440cb8 | -3.25953 | -54.18961 | 2024-10-09 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c2c17c46-452c-3bee-a3c2-1d3403631edd | -3.25898 | -54.1931 | 2024-10-09 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 22cd6d7a-d990-3a59-bbe4-fcf05c256be0 | -3.25675 | -54.1856 | 2024-10-09 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c54e7d90-ccb4-372d-bf48-ef442c063027 | -3.2562 | -54.1891 | 2024-10-09 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e2977817-f3e7-3ce7-b5ba-971c781016af | -2.9401 | -54.21116 | 2024-10-09 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 648f0729-8492-3abb-bc56-7c9e1f558de1 | -2.93678 | -54.21065 | 2024-10-09 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f8a9225-92f9-3659-9038-be8e1df971dd | -2.93525 | -54.17836 | 2024-10-09 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 05a96d2f-9699-3111-842f-20cb09d3bd8f | -2.93471 | -54.18184 | 2024-10-09 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e11c300a-05d8-32cc-866a-d1761912b376 | -2.93139 | -54.18132 | 2024-10-09 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 959bcc24-2105-316b-9c0c-755d7f1b5b2f | -2.91909 | -54.12958 | 2024-10-09 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 03a73201-63bf-360e-9e34-d1801dc366fa | -2.91665 | -54.03638 | 2024-10-09 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cf8345a2-5529-39f8-b9c3-b671ab23f28e | -2.8776 | -53.95873 | 2024-10-09 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e258c01a-070c-36ed-b54f-1d3a68ed3023 | -2.87712 | -53.98375 | 2024-10-09 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 409ceaf6-eb8e-3907-9402-aeeb2c5265cc | -2.87705 | -53.96224 | 2024-10-09 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0390285e-21fb-370b-aa3b-b4d6b2f96ad0 | -2.87426 | -53.95821 | 2024-10-09 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7e2595d8-6c23-3dfc-99c7-7de04e30db24 | -2.87372 | -53.96172 | 2024-10-09 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f66abfb9-bc93-38c0-97ba-9eb5dc75cda0 | -2.85352 | -53.94095 | 2024-10-09 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 63e14872-e8df-3272-a7d7-e499a775ab04 | -2.81533 | -54.35846 | 2024-10-09 05:01:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1785d2f7-411b-3193-a3e3-c5c17ad24e70 | -2.81479 | -54.36192 | 2024-10-09 05:01:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| fea438ed-2a21-3fa1-8a9c-c7a2ee908a11 | -2.81148 | -54.36141 | 2024-10-09 05:01:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8955a9df-7178-3b71-8be7-9dc008f3021e | -2.74647 | -53.95293 | 2024-10-09 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a3a066f3-c295-32c0-b794-32d09a826ca2 | -2.74592 | -53.95643 | 2024-10-09 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 11c168a3-5580-3d70-a162-c46a748879d4 | -2.74258 | -53.95592 | 2024-10-09 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 533ad95f-a711-31de-941d-c8c22faa3ca7 | -2.74203 | -53.95942 | 2024-10-09 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba91fcc0-c054-34ed-bec7-00d8aab144d2 | -2.72937 | -54.14677 | 2024-10-09 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4db1a032-2af6-3528-85fb-1a7c72114ef6 | -2.57278 | -54.21451 | 2024-10-09 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2abf1f35-e7e8-3e7b-b953-adf3ac589e21 | -3.45986 | -53.81731 | 2024-10-09 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 127930e0-73d9-3494-b4e1-e02ba8e0d91d | -3.22736 | -54.85012 | 2024-10-09 05:01:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 22764bf6-ff12-36cd-94bf-56a9745599d9 | -3.15337 | -54.56335 | 2024-10-09 05:01:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d6e58ff-2f68-3e25-9cac-45f9aada45dd | -3.08366 | -54.5313 | 2024-10-09 05:01:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 74b7532b-e674-315c-b701-862f139cb671 | -3.08312 | -54.53476 | 2024-10-09 05:01:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 01eeca58-48a2-3e32-9906-fc3dc93dfe49 | -3.06597 | -54.77537 | 2024-10-09 05:01:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 27139415-7d58-3360-8533-90d01bcce860 | -3.06489 | -54.78225 | 2024-10-09 05:01:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1dea493a-642d-3592-b0e9-d15ad31ba5bc | -3.06183 | -54.77818 | 2024-10-09 05:01:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9e56d33c-9511-3e31-980f-bfd187acaa2d | -2.93605 | -54.82156 | 2024-10-09 05:01:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bcf16e60-6f2a-3446-ae98-cc436fcf4772 | -2.93275 | -54.82105 | 2024-10-09 05:01:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b23d355a-0160-36da-88bd-68f9236867a0 | -2.81282 | -54.59112 | 2024-10-09 05:01:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 74d3c9e6-33a9-378b-8885-5aa43bbd14fb | -2.80013 | -54.58562 | 2024-10-09 05:01:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f30b2f8b-ad1f-3779-b2f2-1e7ea6f1209f | -2.79683 | -54.58511 | 2024-10-09 05:01:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9fc5fd16-5e34-3f19-a7db-188a232686cc | -2.57597 | -54.95195 | 2024-10-09 05:01:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e53ae453-880f-3ee7-9a45-db801c6dc3f1 | -3.12858 | -53.74157 | 2024-10-09 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d5a5b8b0-2caf-3164-898d-2d0f488bb087 | -3.12578 | -53.73751 | 2024-10-09 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ba52437d-5845-3166-90d9-093122ed3d99 | -3.12523 | -53.74105 | 2024-10-09 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 838fce1c-ce5d-3722-badd-2d0256afbf61 | -3.12297 | -53.73345 | 2024-10-09 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0b29e770-e138-3f8c-abbe-8ce3b7d77212 | -3.12243 | -53.73699 | 2024-10-09 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5089719-2dae-31a4-bce3-ffa668db7c5f | -3.12188 | -53.74054 | 2024-10-09 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 081b3a06-fd76-39bc-a82f-792a6383adf7 | -3.12017 | -53.72938 | 2024-10-09 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f179348-f526-35ff-a002-86c941e4e40a | -3.11962 | -53.73293 | 2024-10-09 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44cd0ad0-8bbc-379f-8f11-9d38950d8811 | -3.11739 | -53.73234 | 2024-10-09 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 26abad50-c2ab-3594-8826-66b1287389a1 | -2.97951 | -53.72206 | 2024-10-09 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 49f21fa5-60b0-38d5-af1d-c74117f59e79 | -2.97896 | -53.7256 | 2024-10-09 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 45b78abf-7b32-3231-bbd2-948499ff52cc | -2.97671 | -53.718 | 2024-10-09 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| f3c9f800-bf69-3df6-b419-bb9afe2ed907 | -2.97616 | -53.72155 | 2024-10-09 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 79afa64f-9872-3e8f-9310-fda480411060 | -2.97561 | -53.72509 | 2024-10-09 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a2e0b516-667d-3519-94d5-0d552a2d988a | -2.97336 | -53.71749 | 2024-10-09 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| bebd95f8-e9d3-370d-a10b-398e513a03ff | -2.97281 | -53.72104 | 2024-10-09 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| ae8acc46-1421-34c5-9c02-bb646b86cd5d | -2.97225 | -53.72458 | 2024-10-09 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 9ce58527-5e44-3197-851d-138b815efa89 | -2.95045 | -53.71033 | 2024-10-09 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c78298fa-0821-3fcc-9827-ca35dead4932 | -2.94765 | -53.70627 | 2024-10-09 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a9d5e396-6c8f-34ba-b879-70314722e380 | -2.94375 | -53.7093 | 2024-10-09 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad969e29-7445-381b-a29b-a5da2521653b | -4.40988 | -54.84771 | 2024-10-09 05:01:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b47ff900-3fb2-399f-a713-11c9b245c2bb | -4.07562 | -54.79219 | 2024-10-09 05:01:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 44d1831f-dd44-3e8c-bbf8-e1c27567bdca | -4.09326 | -54.44006 | 2024-10-09 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2ad9c3a-830b-3462-ae33-c0cec7d8f3f1 | -3.88394 | -54.21469 | 2024-10-09 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7708f221-dc2e-33c1-99de-aabb8cf089d0 | -3.78431 | -54.43855 | 2024-10-09 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0d403391-16fb-31fb-b200-7f510f7b8bdf | -3.65754 | -54.29401 | 2024-10-09 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b79f8f99-8347-31b0-aecd-7eee53deeaf0 | -3.657 | -54.29749 | 2024-10-09 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5f4e58c2-48f8-3530-a91c-aa1b4df36f54 | -6.43446 | -55.62852 | 2024-10-09 05:01:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d234929a-c66e-383c-96ee-0ac78f87e8af | -6.43116 | -55.62801 | 2024-10-09 05:01:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4079a3b9-481c-3ca6-a9b0-9dd7f5b4a2ca | -6.43062 | -55.63146 | 2024-10-09 05:01:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 99cd9443-c813-3dcc-bc15-dd7b856e982a | -6.29239 | -55.71226 | 2024-10-09 05:01:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f3be760-f324-3fed-bc2f-35be99a3588b | -6.1716 | -55.48486 | 2024-10-09 05:01:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4fdc18bc-c0d3-3788-8eaa-79993668cd1b | -6.17106 | -55.48831 | 2024-10-09 05:01:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 90fb2298-daaf-374e-b1c1-ef822a28c4d9 | -6.1683 | -55.48434 | 2024-10-09 05:01:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 86f8a99a-71d9-380e-af3a-03936e821a3e | -6.16716 | -55.47002 | 2024-10-09 05:01:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README167.md)
