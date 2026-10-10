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

## Dados Diários - Página 123

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3e25dace-6a49-3891-9415-5f1c808f2738 | -5.74688 | -45.13572 | 2026-10-10 05:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| dd32c468-0284-33d3-9d5d-38b9539fb40a | -3.53348 | -54.74514 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 78da9d21-3493-3de1-8312-bca65cd6b4b9 | -4.14186 | -53.99605 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 90b15938-8426-3e04-9671-77d55358cb20 | -3.80665 | -59.21579 | 2026-10-10 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 61583ea1-c8af-3fa8-8f11-ddbe71db4d1a | -2.52164 | -58.07661 | 2026-10-10 05:04:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1451d45c-bfdb-3890-9613-c6e24ed52126 | -7.226 | -55.07256 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9bced27f-1067-3438-9dab-d46924fe2897 | -3.92006 | -55.76955 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8b451ab1-e0f7-3814-8b3a-a388a5241083 | -4.37603 | -54.74588 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8adacdc7-e184-31d6-85e0-4d16b0b08d23 | -2.73382 | -54.13338 | 2026-10-10 05:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c04d483c-be81-3228-9045-e92cb738a704 | -3.04192 | -54.09731 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 60f875f8-5d20-3d49-b1dd-07232962cebf | -3.18273 | -60.0479 | 2026-10-10 05:04:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be13d957-bc47-3aab-818f-49e8d776b2df | -3.5498 | -55.51923 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d6e6c7d-6c87-3308-ad00-2c945851a606 | -2.58398 | -56.19226 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fca7ac11-a0bc-3fc8-92ac-b4e52ae1b827 | -2.36726 | -55.28247 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b111f51-814c-3a6e-b2ef-7908a093f7c2 | -6.88028 | -45.91694 | 2026-10-10 05:04:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77011136-4605-3f96-955f-05d50f59c3f7 | -1.28776 | -56.99147 | 2026-10-10 05:04:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9d9af089-597e-3c7a-9162-f52f13dbe6d4 | -3.25121 | -54.02047 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 22236256-6f12-3ab3-96da-59d4929b4bd7 | -6.4005 | -52.72625 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 305e9fe2-740f-3a53-bf81-8654a7393752 | -2.48618 | -56.16908 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e368c034-31e4-328b-82d2-9165a736f45c | -5.95825 | -55.3723 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 48380b02-5ac1-36bf-a10b-0c247531b240 | -2.50013 | -58.0865 | 2026-10-10 05:04:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4bccedd8-0aec-38e7-8e01-1f6d8e4a6a2e | -2.80484 | -58.26554 | 2026-10-10 05:04:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 457ee130-c602-3a9c-a004-6c3bec768466 | -2.93135 | -53.95969 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1736cfd3-fb23-399e-9426-4ba36f90dd2b | -3.21479 | -50.55109 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e9cfe32f-f9ff-3f69-b74e-4fe1dd8226aa | 0.00039 | -60.57903 | 2026-10-10 05:04:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 521cbfb9-88b7-3b98-9503-bc1a020a9eea | -6.33822 | -55.31015 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 72ceb2d8-8dfb-3aa6-8363-e2203ae9f41b | -1.01204 | -52.28376 | 2026-10-10 05:04:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6dfe5994-54b6-360f-9863-0fd8a05da35b | -2.46436 | -56.05685 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 761e1de9-bf2f-3338-ad19-d42e55788320 | -3.48471 | -54.62674 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed66ec62-a49c-3eb3-a7ef-bf6c2f89909f | -7.23593 | -55.18092 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1e73ea7a-42fe-3379-91a0-992a97e388e5 | -3.31688 | -54.67529 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 14228858-dc44-3b01-ab60-aba7d71340a3 | -3.87416 | -55.98887 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6599be12-3df6-3aa6-bc50-788824ebcac1 | -5.97165 | -55.35284 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf84a08f-beed-320e-ad53-6fdf2a115cfa | -3.0699 | -54.3713 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bef626c8-d7fd-365d-ad66-7f3a293517c9 | -6.07207 | -59.91278 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f949470-50b5-3791-87fc-cc04c4bc3a36 | -3.12282 | -54.16644 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c7ffa828-be76-3be8-a577-efafeb61bfb1 | -2.7283 | -54.1467 | 2026-10-10 05:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 02e4ba8e-30ce-3c00-8618-9c191863be8e | -3.94704 | -58.84297 | 2026-10-10 05:04:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ef7ab134-ff72-35fe-b3f4-4ec2ba8b6bd6 | -3.96237 | -60.00063 | 2026-10-10 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4436a4d8-6331-3db0-a655-637309d0f729 | -3.00582 | -54.79583 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 36936141-fe5e-3371-8b86-5de970dd8d52 | -3.01045 | -54.08174 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6eaa0e7-26b0-34c7-97a6-8268c8764616 | -2.89289 | -54.07379 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| cf2e387d-a2b5-3856-87c4-06210f8c0156 | -3.10216 | -53.95464 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f02e67ca-81d1-3a31-a165-b77c79623817 | -3.2604 | -54.28425 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3f33961b-a148-3c0c-82d2-b2658ed3bf4c | -2.937 | -54.05243 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30a19bc3-9211-36ed-afd7-5c5105519a42 | -3.05383 | -54.23711 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2a113d9b-3123-34bb-bc18-5e4049010ef3 | -3.18468 | -58.636 | 2026-10-10 05:04:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e78efb08-528e-3978-a12e-aa3ce9de7da6 | -3.30575 | -53.69777 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc3ff173-b2fe-3624-a085-a3556c85f9ed | -2.72565 | -57.4744 | 2026-10-10 05:04:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eac29b68-1198-389c-afff-3bc724da7cdb | -1.32679 | -55.45071 | 2026-10-10 05:04:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 56761e51-6915-3154-8af0-8ffaf2fbb9e1 | -3.54921 | -55.5229 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f29fb035-44cd-3ea5-9655-169abfbd0401 | -3.30051 | -54.01099 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75a2dc20-965f-3dd4-ab7d-33b6efb10949 | -5.07511 | -60.2252 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 04b21ccb-721f-3071-a48d-91724f275750 | -4.74151 | -55.65321 | 2026-10-10 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 76ce79d7-3227-3f62-8470-c3fa99231cae | -4.10089 | -56.12954 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 002e7973-a1ce-3fa3-a771-865d544720f0 | -2.43584 | -55.98839 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d21780f9-cb35-3080-95e0-427d34f7591a | -5.74876 | -45.12251 | 2026-10-10 05:04:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d30f5a7b-a2a5-3dc7-a6a6-fa84b15f9903 | -3.00221 | -54.11228 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 36f00625-1930-3732-948b-667d69634cc5 | -6.42277 | -51.95486 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1983a735-1bd2-39a2-8389-5a9fc2d1eb00 | -3.27703 | -50.02512 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e775f850-06ce-3f0c-b35b-69308a985aac | -3.02601 | -59.21885 | 2026-10-10 05:04:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7b9d97d5-4537-3d74-a158-93aed43f482a | -3.16912 | -54.08883 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68b9164c-573d-3484-abe8-229901a813de | -3.59627 | -54.30861 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e675da8-afaa-3e8a-a228-c9071431316e | -2.52247 | -56.25968 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 81c4e183-2e6f-3fa7-aa86-bb24b10f0d0f | -6.04409 | -59.90034 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4604f08-fb87-36a7-b0da-bdb249b5857b | -3.00804 | -51.02129 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2aa95b91-0774-36df-8a3d-02704fc2c4c1 | -6.43649 | -60.04347 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a594a32-a204-3038-99f9-99754eac8434 | -3.19975 | -50.553 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d6cca20-8ba3-3d82-812b-2ce58bd36ce1 | -3.21297 | -54.36888 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e07f7687-d4ba-3ea4-932e-8ce2b4c8d84a | -2.50092 | -58.08152 | 2026-10-10 05:04:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd2617e6-ec4c-3507-bd64-4bfd5818d992 | -6.53929 | -55.26665 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 59d1ef23-2ad2-36a1-8453-5db7970f0013 | -4.31118 | -50.78662 | 2026-10-10 05:04:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2d6e7101-1e86-3842-a266-b996c39847e3 | -2.93594 | -54.08056 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 48afa2fd-e1e0-347e-8896-8fffdb0cb681 | -3.57472 | -54.37981 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 61892a36-8afa-3c09-8827-151a065ce2c2 | -2.99094 | -53.90562 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 813d9543-746d-33d2-8cd4-85ac38c167cd | -3.23063 | -53.89377 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b106d640-b0ac-3609-853f-9a406f7b8b86 | -3.31576 | -54.68228 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 66ce051a-a37a-38c6-849c-370d5016da75 | -7.23045 | -55.15141 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe7796db-5897-3b2a-acd3-32bf5d15d1c8 | -3.19098 | -58.64782 | 2026-10-10 05:04:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| feb68226-4de2-332a-96f9-a397eba519e2 | -4.34524 | -55.13048 | 2026-10-10 05:04:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b7d8d02-dc05-3838-bb87-54b73e938b8a | -1.27387 | -55.75734 | 2026-10-10 05:04:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bc4b6acb-4495-308b-9561-19bdc92a4dea | -3.35426 | -50.42203 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f1fa9f9e-a0ca-3239-9ffc-7a1f34e3f34a | -7.26722 | -57.12116 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 66ff3792-0d5a-3640-b100-b69bf513156e | -6.07302 | -59.88163 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 86169c6e-fabf-31fa-8187-e5403745926f | -5.08082 | -60.21761 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7ad9541c-9742-3a5c-b2ee-7a3d11b42e26 | -1.07997 | -54.10738 | 2026-10-10 05:04:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 37547d3e-71d7-3ca7-8c60-25024bdca5c4 | -2.96525 | -54.15254 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4fa5438c-c330-3c09-a789-5068172dadc4 | -3.36356 | -54.74752 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f0339de5-4e8a-30ac-b5f7-5ff601f6dd75 | -3.42159 | -59.58197 | 2026-10-10 05:04:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01fa37f6-801a-3402-bdd1-7f471c7a40a2 | -6.26014 | -55.43823 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6c375c9c-6c63-30aa-a71a-8ed0cbf99db9 | -5.685 | -53.45331 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a11c238e-b6ad-374b-8c8a-15a109473f6b | -3.26451 | -54.06494 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 893d7a46-471e-37e8-b49b-2124cdbb8cf0 | -3.20804 | -53.88671 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 286ddd11-b98e-3b0d-a365-1c9036128ded | -2.8383 | -54.22474 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2ccf6e56-5d0a-39e5-b060-0ae8b31e5eca | -2.39348 | -51.30789 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6515bcf7-b802-3d80-afd2-635270b24dec | -4.1062 | -54.628 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 28873725-5c51-3c35-a0e5-edf51b65e7c9 | -2.60726 | -59.98597 | 2026-10-10 05:04:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 066a3a21-e5df-3f21-b062-a4bce22fad0a | -7.39997 | -55.15359 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 26b2c200-9c31-3118-a8c8-af982723afb8 | -6.39993 | -52.7299 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70fd0a00-98f9-35a9-9068-5b49298dc363 | -1.64079 | -54.40435 | 2026-10-10 05:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |


[Clique aqui para ver as próximas entradas](README124.md)
