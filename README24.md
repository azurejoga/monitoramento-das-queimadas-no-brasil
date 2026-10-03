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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0492c94b-acaa-3c75-be66-d37fbd21af62 | -3.30073 | -50.32153 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a29c56c0-1c61-3887-95dc-70a2dd8e3159 | -3.07999 | -51.27613 | 2026-10-03 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c01bf2f2-d494-321f-99b9-29e200b9e94f | -3.10385 | -50.29795 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8d882fa-3ecb-325d-ab6f-b2e5a018a8ba | -2.88004 | -51.0316 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c3df74d0-04b1-3720-a0c7-16a4eab5f120 | -3.13047 | -53.73116 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| e32fdced-f806-37ae-857e-b065cfaced08 | -3.98405 | -45.8803 | 2026-10-03 04:38:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8b57f403-bfaf-3479-b194-660b2ddeb3dc | -3.00895 | -53.88573 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a28ee1af-afe3-3564-a139-e42f55265507 | -3.24109 | -54.51572 | 2026-10-03 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea6bcf84-9bd7-3ea7-ba26-a8578a971f53 | -2.98094 | -53.26401 | 2026-10-03 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6c5e2ae1-82cd-3eec-a00a-29dabdb4a310 | -3.1775 | -54.08345 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| cc6703ba-166c-3051-a518-fb2a7375b9fa | 2.35423 | -50.75135 | 2026-10-03 04:38:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e794d065-ac92-330c-b052-07ccb450ff80 | -3.98341 | -45.88449 | 2026-10-03 04:38:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a59eb6ac-4483-34a9-802f-6cdd2ed733b9 | -2.91759 | -54.08955 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1775e069-e73e-3c78-b96c-1bf54559c513 | -4.89117 | -45.45443 | 2026-10-03 04:38:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c7388435-5db0-33f7-a094-1ce005f4089b | 1.78962 | -55.5916 | 2026-10-03 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3a18c356-3dd0-3796-bd81-ea5d70a0e199 | 1.03752 | -50.02051 | 2026-10-03 04:38:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef35f21c-cf8b-3aae-81e8-53789cf7d72f | -2.88847 | -54.14093 | 2026-10-03 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 2818dcbb-e316-323b-a2b2-c580de1b7769 | -3.28675 | -53.8405 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cec5fb09-33e8-3457-a7e4-0a4988e25b19 | -3.2728 | -54.00671 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6158f0f4-77fe-367f-a172-4862e41ddae6 | -1.25941 | -54.56028 | 2026-10-03 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da804bf0-b951-3745-ac81-cd0eb66bb8cc | 1.73598 | -50.8062 | 2026-10-03 04:38:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6de6e5e7-0db8-3116-9778-f061aaa7c411 | -4.06088 | -51.09411 | 2026-10-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c40d42d0-2c0c-3ac7-9d40-0a4749b37baa | -3.77616 | -52.14386 | 2026-10-03 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 53d3c7ea-a854-3213-8d82-00a6355aaa2e | -3.13388 | -53.73521 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 29dd9686-1ec1-3835-9228-8aff84292588 | -4.28998 | -48.56401 | 2026-10-03 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 787c849b-69de-33e8-a683-18b496b1a823 | -1.0899 | -49.27118 | 2026-10-03 04:38:00 | NOAA-21 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3d22bbf2-d297-34c0-9601-ab7317503a45 | -3.88229 | -52.18455 | 2026-10-03 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a3f0f42d-2918-320d-a6f7-00d74618d927 | -3.14238 | -53.73304 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 950b0b7a-d31d-39cb-8aa4-71d04a2ec153 | -3.06659 | -49.36158 | 2026-10-03 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e6f098e-8c87-38be-ba4d-44f6b48740a0 | -3.22817 | -54.30907 | 2026-10-03 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 02c2040f-96c4-3e33-b321-d00839bb83d7 | -1.26503 | -54.55285 | 2026-10-03 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7803d38e-d902-369e-a4c7-31864f8aba2b | -2.91734 | -46.72168 | 2026-10-03 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a884ad68-d87d-301d-a40e-69daa707d0ff | -3.76939 | -51.86462 | 2026-10-03 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1ff54067-2c8a-3b38-aab8-b070c3ed56a3 | -1.27169 | -54.56648 | 2026-10-03 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| eb492c4c-bcf2-3f34-b7d0-7bd95e08ea0f | -3.12658 | -53.7551 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 71675dab-78c7-3cbb-9049-695f6669ca19 | -2.17346 | -49.76167 | 2026-10-03 04:38:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f8ff296-1b5c-37e7-91f3-d2557744090f | -1.105 | -54.14396 | 2026-10-03 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef3df86e-37c3-3f83-9c7f-7f5051736a01 | -3.88327 | -49.68756 | 2026-10-03 04:38:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0d5f3aec-7fce-3fbb-b20a-fa8ea5ea2dba | -3.16186 | -54.07729 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc275d40-e224-3e41-959d-91745fe933f8 | -3.24947 | -54.51686 | 2026-10-03 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99ed0d92-b389-3f3b-b581-a4ebe6b469bf | -1.27732 | -54.55896 | 2026-10-03 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c55d7d54-a07f-3acd-ad46-12af31a81967 | -1.26738 | -54.56579 | 2026-10-03 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e80bab8a-c432-31e9-ba0c-39633913e5e7 | -3.13333 | -53.73863 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6cea7f96-81e3-3505-b45f-2e581c502392 | -3.29183 | -53.8342 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6da37c00-be32-3f26-a0bb-7aa908dc3101 | -3.1288 | -53.74142 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 554dc915-e55c-35fb-96a0-8d7cbc1ea48e | -3.01641 | -53.8905 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0755f660-333b-3af6-9d46-e655d2c7649d | -3.29128 | -53.83766 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37fc7fbf-7c90-321f-873c-440742ba5ff6 | -2.9211 | -54.0938 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c7ea7c85-d020-382d-b55c-50767e04d92e | -3.17866 | -54.10188 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91862283-b129-3652-ab4a-95298001bf2e | -2.91351 | -54.08893 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fb85087f-cecc-3dd5-8a01-aab38bb4a551 | -3.51609 | -50.31462 | 2026-10-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3abf3aa5-8ae1-3998-92f8-16acb3e5c806 | -1.11574 | -47.73313 | 2026-10-03 04:38:00 | NOAA-21 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6c37c147-f66e-325a-82e6-fb1605c082dd | -0.34903 | -51.9991 | 2026-10-03 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0adb2620-71cb-35a4-ad25-22e6c30207e9 | -3.21669 | -53.94454 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 627b9e54-4ab6-3ced-8bb4-cf30c68c3b72 | 1.92889 | -55.79947 | 2026-10-03 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1d9fef08-3bfb-3ad0-bad8-88bb804c3902 | -3.24528 | -54.51628 | 2026-10-03 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f5ba5aa-01f8-3fdf-a67a-88a4c0076330 | -2.27501 | -48.74484 | 2026-10-03 04:38:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33bb2bbc-c7a3-35a1-a491-543f2c688053 | -1.26372 | -54.56097 | 2026-10-03 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f0d4757c-a96c-3cc8-9d85-a3c0884d23f4 | -3.71324 | -50.654 | 2026-10-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9b8087db-ede2-3a29-8010-9ccf1b9dbbd3 | -2.89663 | -54.08994 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2707df5b-f135-330a-b9fc-e60902d64bfb | 2.09228 | -50.7475 | 2026-10-03 04:38:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d06e1c21-418a-34bd-ad75-28aa2d0b416b | -2.17625 | -49.76569 | 2026-10-03 04:38:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 82cfb5aa-2aac-3e8a-bf9b-a061dd8825fa | -2.92808 | -54.15182 | 2026-10-03 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 007f440a-4681-36d4-a186-14568d3a016e | -3.19138 | -54.10051 | 2026-10-03 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 81c3b495-5c5d-38b7-99e3-ca54dfdb30a3 | -4.45622 | -47.92695 | 2026-10-03 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| d10ca3de-ab04-3df9-8bea-1e4c88262e84 | -4.3611 | -47.77805 | 2026-10-03 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e34df24-d888-349c-b706-e51f8e919895 | -2.89315 | -54.11168 | 2026-10-03 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 993c5bcd-2812-3bf1-a4f3-de3b3e273b3d | 0.98075 | -50.12829 | 2026-10-03 04:38:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f97050cf-d673-3603-a6de-ee3d8c152c84 | -3.11497 | -50.28503 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e042012e-865b-3c0a-8039-3ddef90e52d3 | -2.87173 | -50.32391 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd6eadf1-47da-3125-b4ae-840f1faf47e8 | -3.56414 | -50.28639 | 2026-10-03 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5664795f-62fd-35de-8c95-3ffd783fb2b6 | 0.70167 | -51.43271 | 2026-10-03 04:38:00 | NOAA-21 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 87b12aa3-3f84-3ac5-aa00-4ed384157788 | 1.79936 | -55.59015 | 2026-10-03 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 98cd8cce-c251-3cdf-908d-c5ef9cfe3fa9 | -4.02066 | -44.82781 | 2026-10-03 04:38:00 | NOAA-21 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57ba3687-e727-3094-85a9-1f93b567a2f9 | -2.22879 | -51.92485 | 2026-10-03 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ae3e7bd-3503-3b4b-8df0-4b7fbc1c22e2 | -1.14993 | -54.1871 | 2026-10-03 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d424c99-042a-3c4d-832a-f7f49c202b77 | -0.35133 | -52.00855 | 2026-10-03 04:38:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d7efa4b4-fb58-386e-880d-92161aca8162 | -5.71334 | -44.32599 | 2026-10-03 04:40:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f9fe3706-07dc-369e-9886-7aacc4057b6a | -4.26714 | -50.74793 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e9894e44-9278-33c2-a993-3f953e46a7e7 | -4.28226 | -50.78359 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e05e6c4-40f0-3446-adcf-ff762762f101 | -5.29924 | -45.80329 | 2026-10-03 04:40:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| da06aa00-e3c3-3e29-879c-796ff71125ff | -6.02143 | -53.53516 | 2026-10-03 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e1d4f77-e77b-3f87-8374-e1312d2c06e3 | -6.84105 | -59.26701 | 2026-10-03 04:40:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 23eb7aab-a477-3088-8b5e-d18216ccbb8d | -5.95863 | -43.65203 | 2026-10-03 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4966a4e9-bb19-3687-a88f-6509c804983d | -7.46695 | -54.99363 | 2026-10-03 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78a4f821-fdee-3d73-aa59-f3f067d38bb3 | -5.7353 | -43.28403 | 2026-10-03 04:40:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 93a41062-1414-396b-8ae8-b16ddabc7a80 | -5.13515 | -45.57933 | 2026-10-03 04:40:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| eeb5f92d-d1dd-30d6-ac3f-081b22111eea | -5.61741 | -44.38185 | 2026-10-03 04:40:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| e7af9733-f254-30b1-a5e3-fca4295401c9 | -4.211 | -53.56679 | 2026-10-03 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4c4a25e9-3718-3905-bc8d-0ff368713eef | -4.81004 | -49.87635 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 71b5eb46-ba06-3606-8d75-ba07c81f387a | -4.71221 | -56.15147 | 2026-10-03 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 252e7e3e-758e-33bc-a2b5-f2786f0f6db8 | -5.74484 | -45.0593 | 2026-10-03 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5084e879-9fe5-36b8-b6ef-8d32ea1cf568 | -5.3448 | -50.08902 | 2026-10-03 04:40:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 83d087d6-2892-3bb8-b268-cef5c99d5cfb | -5.95957 | -43.65003 | 2026-10-03 04:40:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9831ab4a-579d-3dc1-bd7b-130ae76f15eb | -3.62629 | -60.21139 | 2026-10-03 04:40:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86262989-6e38-3a22-ab28-d8535c746238 | -9.69992 | -57.46211 | 2026-10-03 04:40:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| efa603d9-2edd-3d04-a93c-61cd708402db | -4.26772 | -50.74432 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ab16dcca-dbfe-3f84-9e49-edb206f7edd6 | -4.2806 | -50.77219 | 2026-10-03 04:40:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26435f45-2073-3670-8e61-deffb26bdc00 | -5.64025 | -44.36718 | 2026-10-03 04:40:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 652b16e2-1503-31b6-9b8e-a9a434048f8d | -3.85098 | -55.80796 | 2026-10-03 04:40:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |


[Clique aqui para ver as próximas entradas](README25.md)
