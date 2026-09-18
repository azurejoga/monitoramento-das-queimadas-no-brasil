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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 536b9d7b-ba24-3388-a17f-fc4b46c8dfde | -4.48371 | -54.98268 | 2026-09-18 00:03:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 06db6e12-9b46-3dd5-aeb1-564b7288ee93 | -3.06696 | -49.51952 | 2026-09-18 00:03:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 9b87cd8c-95db-30a3-b9b5-e7f4aa898885 | -0.78148 | -48.64999 | 2026-09-18 00:03:00 | TERRA_M-M | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 82ff9d16-e85d-32aa-a725-42a44cea7686 | -3.17782 | -48.58866 | 2026-09-18 00:03:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| c4acea80-b858-3d22-a864-a8cad733a9c1 | -3.16205 | -48.61072 | 2026-09-18 00:03:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 61a55c1c-97cc-3218-b0ff-80941b7165c5 | -3.10842 | -48.69702 | 2026-09-18 00:03:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 5ce932f0-4ea7-3a65-862b-d133f799e3ee | -2.82537 | -49.24066 | 2026-09-18 00:03:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c52da2f3-5f98-3f99-b0ce-129456432585 | -4.5339 | -54.92567 | 2026-09-18 00:03:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 5429d671-c990-326c-ae11-834eb973a648 | -3.3795 | -50.4461 | 2026-09-18 00:03:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 1c778d11-af21-32fe-885a-0e414fcc9be6 | -3.4859 | -54.72121 | 2026-09-18 00:03:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 3e06700c-f862-32a1-af95-36fa76b85f57 | -1.23216 | -49.25108 | 2026-09-18 00:03:00 | TERRA_M-M | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7e3cb075-72d0-3e03-a790-c89bbb54eafc | 1.06983 | -51.00817 | 2026-09-18 00:03:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 2cd274d3-ab40-343e-8a95-ccd61839565f | -2.87858 | -54.06745 | 2026-09-18 00:03:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 333c9442-3739-3fde-99f5-e7f25636cc3c | -2.87105 | -49.63269 | 2026-09-18 00:03:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 1ed23410-6edd-3f29-b20f-105c572abc89 | -2.90513 | -54.18607 | 2026-09-18 00:03:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 9467b9ff-3917-380c-b702-5d44a4dcf59b | -2.89488 | -54.18746 | 2026-09-18 00:03:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 31a36b56-f8e5-30cd-843e-5a57d0939da3 | -1.25297 | -54.21896 | 2026-09-18 00:03:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| e703d9ec-e792-32b6-b278-e500d9e3b9d5 | -3.49938 | -51.25486 | 2026-09-18 00:03:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| d2c51b79-27b3-36ec-b287-9c19de5bcfb0 | -4.42724 | -55.51239 | 2026-09-18 00:03:00 | TERRA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 542281a5-9d14-3955-948d-cb9aa991c0e5 | -0.54473 | -49.14616 | 2026-09-18 00:03:00 | TERRA_M-M | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e0592e12-8346-3cf8-b79a-843a332c1333 | -2.49006 | -49.41517 | 2026-09-18 00:03:00 | TERRA_M-M | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 1b5f25a1-c417-3b17-8b09-ca4219c99473 | -1.12439 | -49.20436 | 2026-09-18 00:03:00 | TERRA_M-M | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| d8506a11-cc03-3cf5-b945-58d0268ab56d | 1.39969 | -50.89917 | 2026-09-18 00:03:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 7.6 |
| dcad2de0-5e52-316f-abde-dfc86f5228f4 | -3.37829 | -50.43735 | 2026-09-18 00:03:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 44b0a079-0ef7-3b67-9fd4-0b556302829b | -3.26922 | -54.31292 | 2026-09-18 00:03:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 1b1f5c72-15b2-3604-8205-f917f7f1034f | -1.2015 | -54.21546 | 2026-09-18 00:03:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2bb6a59a-1dea-39c6-993d-82dab2540845 | -1.22174 | -49.24289 | 2026-09-18 00:03:00 | TERRA_M-M | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 047d47c1-c24e-3e2c-ba45-3475d5b49bcc | -1.03085 | -49.19466 | 2026-09-18 00:03:00 | TERRA_M-M | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| d4f5d21a-b6d4-3997-bb00-23834e8d26fc | 1.4009 | -50.89035 | 2026-09-18 00:03:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b5ca273f-08f7-3ae2-9712-eaa575ae9456 | -3.3695 | -50.43858 | 2026-09-18 00:03:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| ced82b01-597c-3c3a-a404-f859fe74a053 | 1.25015 | -50.77618 | 2026-09-18 00:03:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 7dc5488f-118f-34b7-8bc1-f3659b63d9ed | -4.52693 | -56.08606 | 2026-09-18 00:03:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| fb7de326-99d5-386c-8a6c-d4ac8511b125 | -3.43429 | -58.19693 | 2026-09-18 00:03:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 22.5 |
| 58e8a8c0-a9de-3fb5-9784-0516a427c44a | -3.36433 | -50.46606 | 2026-09-18 00:03:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c82d518d-6d02-33ea-a019-d89062ba8ad6 | -3.34187 | -53.26756 | 2026-09-18 00:03:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| a7750f11-8061-3489-9f18-201a41d670ed | -2.83395 | -48.64557 | 2026-09-18 00:03:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 2c13042e-ea7d-362c-a506-c0cac0bc37e9 | -2.19011 | -47.65211 | 2026-09-18 00:03:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 8913cc35-23f3-3449-8411-b2e1abdeaf4d | -1.37628 | -49.3624 | 2026-09-18 00:03:00 | TERRA_M-M | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9b734c62-c50c-3030-91aa-91d2b9ef5d2a | -2.5455 | -54.72049 | 2026-09-18 00:03:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 8663b935-61f1-3aee-9262-bbe759d79f48 | -4.51225 | -56.06913 | 2026-09-18 00:03:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| ecc6ffde-3904-3624-82cb-f96e22c32bd5 | -3.73097 | -52.27886 | 2026-09-18 00:03:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| eb786b94-4a0d-32d9-bfe9-2f84ccbe4051 | 1.07104 | -50.9994 | 2026-09-18 00:03:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 28510483-4f29-32b2-b245-ee614144f2be | -3.68987 | -54.54607 | 2026-09-18 00:03:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 085c1935-adfe-311e-9c82-76e588739298 | -3.03716 | -51.37656 | 2026-09-18 00:03:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 3ccc80c8-3bbb-3360-b65b-33282e5a22e2 | -2.54729 | -48.16374 | 2026-09-18 00:03:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 25.2 |
| b3e16ad2-a24f-31f4-9b26-a9214d712a26 | -1.02954 | -49.18511 | 2026-09-18 00:03:00 | TERRA_M-M | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a9eb4158-c471-3d8b-ae20-4760741436ee | 1.40851 | -50.9004 | 2026-09-18 00:03:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 3eb1bf1d-717e-36e4-8783-b939c8106535 | -2.58525 | -48.43809 | 2026-09-18 00:03:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 8b3de33b-a262-3034-83b0-2df735d6a986 | -1.7844 | -47.83099 | 2026-09-18 00:03:00 | TERRA_M-M | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 31.0 |
| a8032f95-dc65-3af1-9884-68c7ad3dc1dd | -0.78526 | -47.5556 | 2026-09-18 00:03:00 | TERRA_M-M | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 0ddef5e8-148b-3d27-91c5-4893bb18a816 | -3.47335 | -54.70908 | 2026-09-18 00:03:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| be9237b6-f115-3adf-b4af-969b38e6d492 | -3.26752 | -54.30031 | 2026-09-18 00:03:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| dbf6bc2a-a009-34df-b794-a3619f6b4bbf | -1.78885 | -47.84663 | 2026-09-18 00:03:00 | TERRA_M-M | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 9cd7bcbf-d289-3d8c-9250-c3e681b2bade | -2.0562 | -52.15838 | 2026-09-18 00:03:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 8baf6f4b-a52b-3620-9699-b89a253ec62c | -3.03837 | -51.38546 | 2026-09-18 00:03:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| bfc9506e-8adb-35c6-8147-79ebe68e9dac | -2.83532 | -48.65528 | 2026-09-18 00:03:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 27.2 |
| 7967510d-1014-3067-b6d1-3d5d6f05144d | -4.51459 | -56.08696 | 2026-09-18 00:03:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 99.1 |
| e84648e9-7f61-3770-82e3-569bee1a8179 | -3.37312 | -50.46484 | 2026-09-18 00:03:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 807d0048-a485-349a-a07e-cfaf14e48413 | -3.26417 | -54.2754 | 2026-09-18 00:03:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 03fac745-bc26-3649-ba4d-f2f7f9135bdc | -3.36312 | -50.45731 | 2026-09-18 00:03:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 95.0 |
| d1a68be8-9d23-3037-be4e-af1e1fa60599 | -3.92001 | -55.74891 | 2026-09-18 00:03:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 2c2c6809-96d5-3901-9712-caa6df71e488 | -3.36192 | -50.44856 | 2026-09-18 00:03:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 4ca12aee-eeb9-38c0-9fdc-f93243c5230c | -3.2625 | -54.26295 | 2026-09-18 00:03:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 4ca18f10-42bf-3017-ab54-8cf0a72567e9 | -3.04603 | -51.37531 | 2026-09-18 00:03:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 7845e637-ca23-3152-858b-2903352141c3 | -2.05746 | -52.16764 | 2026-09-18 00:03:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 103.8 |
| ae84b40b-31c7-30a2-9e1a-3e36026c499e | 1.33998 | -50.59578 | 2026-09-18 00:03:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f21ebfaa-165f-3b43-af5b-a81c9a1e1b54 | -3.04725 | -51.38424 | 2026-09-18 00:03:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| fc9a71e8-3cbb-35f6-a543-0bdcc12a58d9 | -3.44859 | -58.19501 | 2026-09-18 00:03:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 2c0a548c-d959-3868-8423-36651dc87353 | -3.47158 | -54.69563 | 2026-09-18 00:03:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 0ac376a0-fbda-38ef-bf31-4e929e984b9f | 3.97353 | -51.69447 | 2026-09-18 00:05:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 63a8ea6e-0770-3990-a9c0-445d83b6c458 | 3.98233 | -51.6957 | 2026-09-18 00:05:00 | TERRA_M-M | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.3 |
| edbca465-97b2-3d46-9c1c-5f56749205ce | -12.2817 | -50.7868 | 2026-09-18 00:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 05efe772-81e6-3403-837a-6a0bfdec22b1 | -4.5589 | -42.9289 | 2026-09-18 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 111.0 |
| 984edeeb-3483-3935-bab4-3be7b95842b6 | -11.2783 | -43.388 | 2026-09-18 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 155.9 |
| 413d8b5f-112c-3bcb-8462-3665d6f2d03d | -12.4501 | -55.0063 | 2026-09-18 00:10:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 7702e8df-bf32-3847-b5a1-e1b271227f91 | -3.3823 | -50.4486 | 2026-09-18 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| cf439516-a9e9-31fe-9d08-ed6326194ca7 | -6.1359 | -59.9446 | 2026-09-18 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 4fafe0da-00ce-3859-ade7-1b83c7397065 | -3.3639 | -50.4282 | 2026-09-18 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 4792ab49-183c-333c-90d6-214fef233d42 | -5.7567 | -45.1067 | 2026-09-18 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 131.4 |
| ed775484-536d-3623-9a6c-3d3ce9c96bda | -4.5772 | -42.9746 | 2026-09-18 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 493.0 |
| 21cfbc97-b292-3f6f-beeb-0f8e4f05c738 | -12.2626 | -50.7891 | 2026-09-18 00:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 91.1 |
| f19250c2-f06e-3e4e-83fe-cf0b85355cf8 | -3.028 | -51.376 | 2026-09-18 00:10:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| c9f2877e-3909-3ad1-80ce-123020950dff | -5.7615 | -57.5807 | 2026-09-18 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 422cb327-1a87-3e2d-82eb-64c62ac76823 | -6.1174 | -59.9644 | 2026-09-18 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.2 |
| a33b1898-e0df-36d0-914a-620b95f84e19 | -4.5177 | -56.0751 | 2026-09-18 00:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 94.7 |
| ab885f21-ccdb-3834-b900-9578d057ce38 | -2.8284 | -50.4863 | 2026-09-18 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.3 |
| f70c3b3b-8f36-3e9b-b3f5-e5d9c04f10e9 | -2.8285 | -50.4653 | 2026-09-18 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| a29d6567-19fc-3c44-b1b8-65a6280f09c2 | -6.1175 | -59.9452 | 2026-09-18 00:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 7072b1c2-1eda-36a5-81b2-fe4572983969 | -4.5961 | -42.95 | 2026-09-18 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 4ffdfaaa-b2ad-37db-9522-ef8a735cebb0 | -12.4742 | -50.6781 | 2026-09-18 00:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 93.7 |
| f96a8b40-040f-3d8e-b915-91e5559392f7 | -8.9479 | -51.4618 | 2026-09-18 00:10:00 | GOES-19 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 6880b37f-17a9-3e6e-976e-21dc55e1b2c8 | -19.2015 | -48.7675 | 2026-09-18 00:10:00 | GOES-19 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 70.2 |
| a99fdd3b-078f-3819-b26e-c39bda79238e | -3.3638 | -50.4492 | 2026-09-18 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 132.2 |
| e855cbcb-91dd-3ed8-85cc-f97a3b9660c8 | -3.3637 | -50.4701 | 2026-09-18 00:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 6fff5d7c-70cd-30b3-ab28-44f27b5bbe8f | -11.2975 | -43.3851 | 2026-09-18 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 459.0 |
| f0ab9213-eb1f-3884-979f-5c1f6d3926eb | -11.2979 | -43.3614 | 2026-09-18 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 636.0 |
| 853d38e2-9193-3928-b169-5db590b32718 | -5.7429 | -57.6009 | 2026-09-18 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 1cfcef89-05e8-3872-93be-039adbecb7a7 | -5.738 | -45.108 | 2026-09-18 00:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 31d238f9-56fc-3884-9dc3-a5c1cdc08b43 | -12.644 | -54.7212 | 2026-09-18 00:10:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 79.2 |
| 4f6d70ce-599c-3f5b-a3ee-a316898affb7 | -11.2983 | -43.3376 | 2026-09-18 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 112.0 |


[Clique aqui para ver as próximas entradas](README6.md)
