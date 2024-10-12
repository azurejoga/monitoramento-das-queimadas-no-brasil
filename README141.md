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

## Dados Diários - Página 141

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 98eed551-bec3-33e9-8494-5778a9267430 | -10.88678 | -63.92855 | 2024-10-12 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9df10a2f-d77f-38f9-9529-5a741df0ce85 | -10.88238 | -63.93251 | 2024-10-12 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b0f85a2d-458a-3ca7-befe-ca053eedf2bf | -10.88185 | -63.90907 | 2024-10-12 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8b697433-f6d8-3e20-815c-10822ad87f33 | -10.86318 | -63.92702 | 2024-10-12 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9b5a9293-90c5-39f0-b120-1e30d0fedc3e | -10.8629 | -63.90281 | 2024-10-12 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e6a0ecc7-ba39-3d80-970e-5bd85e32bb95 | -10.86013 | -63.92167 | 2024-10-12 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9a4ae147-31b2-3e37-9ab7-0718b6ff5062 | -10.85914 | -63.90227 | 2024-10-12 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c50f60ec-2161-31fd-82d9-eaf64ce118a3 | -10.85844 | -63.907 | 2024-10-12 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8d8d4a6b-e271-3ace-abc3-559af4fc3189 | -10.85775 | -63.91169 | 2024-10-12 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5f808203-c51a-3949-92c0-4046589a9fc4 | -10.83762 | -64.22086 | 2024-10-12 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 79b38961-4dc0-3a38-a573-cae9cc951cd4 | -10.83151 | -64.21068 | 2024-10-12 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6c71a264-a445-3821-9473-2ac6d11884ef | -10.83044 | -64.17522 | 2024-10-12 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 11baf95a-4e51-3643-a3c4-441b1e27230f | -10.82783 | -64.21001 | 2024-10-12 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 786b7e82-b0eb-390a-81e2-2db7651e61ef | -10.82608 | -64.1791 | 2024-10-12 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 779c2a64-132f-335c-86a8-085fd5232687 | -11.78223 | -64.25053 | 2024-10-12 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| dcd58f5e-517e-36d7-9c20-af17ea8cccfa | -11.77853 | -64.17066 | 2024-10-12 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 83bb5927-2c50-3d7a-9c28-4d45434ca5c1 | -10.97368 | -63.9417 | 2024-10-12 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9919941a-1cd0-36da-9d61-e78bc494e47b | -10.97288 | -63.94398 | 2024-10-12 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 76b47db1-0500-3179-b8eb-580312d0d0f7 | -10.97025 | -63.99335 | 2024-10-12 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b7172d16-b293-3b8a-bfa3-94eee7152a0e | -10.96654 | -63.99254 | 2024-10-12 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 08d90dbb-60ed-3ef5-8fa3-fc1c2c13eb07 | -10.92806 | -63.88171 | 2024-10-12 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a5d4149-3088-393f-a265-02c79f2d99cf | -10.89498 | -63.92487 | 2024-10-12 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| af74af86-0746-3179-a517-04ab451740b4 | -10.89055 | -63.92901 | 2024-10-12 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c18ff0c3-a574-3ada-aad5-7d101caea398 | -10.88614 | -63.93308 | 2024-10-12 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 42a970c1-1116-3915-a89f-129467a1f000 | -10.87487 | -63.93132 | 2024-10-12 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 709204a7-f825-30a1-8244-cc013343c965 | -10.85945 | -63.92632 | 2024-10-12 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 86e83bc6-7755-37cc-8db7-0aee6970d356 | -10.85468 | -63.90647 | 2024-10-12 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 17.3 |
| a98bedcf-7a57-39dd-a8e4-40b299bf959a | -10.854 | -63.91109 | 2024-10-12 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4dd2bc39-48d3-395d-afc7-d0fef6d157b0 | -10.837 | -64.22517 | 2024-10-12 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9d8bb3d1-d153-3568-8084-fe66b9b02f95 | -10.8288 | -64.21181 | 2024-10-12 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d414b93f-5133-3a5c-98b0-cde02ec46874 | -10.8286 | -64.17786 | 2024-10-12 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a2571232-fde2-34d2-bdbb-d3bfeb1d7514 | -12.16798 | -63.34441 | 2024-10-12 05:48:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 887d27fe-a096-398a-8197-459efe8d3cea | -12.16402 | -63.34385 | 2024-10-12 05:48:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 704557ee-4fc2-3870-ba57-0cb7b04a0d8d | -11.76608 | -63.79466 | 2024-10-12 05:48:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9ddfe402-84ca-3a8d-b7ac-de68ef014750 | -11.75955 | -63.81347 | 2024-10-12 05:48:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a8924e11-7a5e-363f-9400-dbf0d18101a9 | -11.75529 | -64.0918 | 2024-10-12 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a2e2e3b-f12e-3f19-b5a7-2efc6adbdd75 | -11.75127 | -63.82528 | 2024-10-12 05:48:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3d9c40d6-f521-34c0-82a3-faf80bb2eb87 | -11.75057 | -63.83009 | 2024-10-12 05:48:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b0a159d2-7ee9-361f-8f25-36af34ce883e | -11.74988 | -63.82686 | 2024-10-12 05:48:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 98903852-1007-347a-99c7-c6efea8141a3 | -11.74853 | -63.83661 | 2024-10-12 05:48:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5beb0702-70a9-35aa-b978-5a075a071587 | -11.74744 | -63.82477 | 2024-10-12 05:48:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 95685967-8a3f-3af5-97c8-b429e5f259ce | -11.74602 | -63.83453 | 2024-10-12 05:48:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c8ba69b6-07d8-3a0b-b417-3f1f5e1e3a78 | -11.7447 | -63.83616 | 2024-10-12 05:48:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 93a62dfd-c2bf-37f0-a3bd-e7d2d405876b | -11.74153 | -63.83081 | 2024-10-12 05:48:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4d76aac9-92c2-359e-a8f3-a2d59c8b73d0 | -11.73904 | -63.8288 | 2024-10-12 05:48:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 844337ba-2551-3336-9bca-1d3a57e6e11c | -12.49699 | -63.94568 | 2024-10-12 05:48:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f3451ad6-c809-33eb-9ed6-ad148cbf5803 | -12.49633 | -63.95052 | 2024-10-12 05:48:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9ea2523d-c6a7-3705-9f67-9c0718a0e9d5 | -12.49372 | -63.95293 | 2024-10-12 05:48:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 90ebd90e-434a-3a3a-a150-61ed1ad3ee9b | -12.49182 | -63.9548 | 2024-10-12 05:48:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6e3c33c6-b08d-33cd-a0e1-c5880a477f66 | -12.48919 | -63.9572 | 2024-10-12 05:48:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bac1a0d0-bea9-313b-94e2-fdfbb1ce8c99 | -7.49043 | -64.28143 | 2024-10-12 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6eeb39d5-9b8a-3216-a3fb-35bce57baa97 | -7.46268 | -64.24831 | 2024-10-12 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a974a862-9579-3f26-bf2c-a8fda5d93cfe | -7.42781 | -64.58005 | 2024-10-12 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2522398d-c58a-3163-8d8b-b63f808c67ba | -9.21857 | -65.56425 | 2024-10-12 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9d815866-01b6-3344-8644-211dd836295f | -9.21856 | -65.56482 | 2024-10-12 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c03d8088-99de-3767-850f-f12c70780d14 | -9.49211 | -64.35831 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f64f03f3-36d3-37d2-87ac-15a0939263df | -9.41857 | -64.38159 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b8cc42f1-d9bf-344d-b933-59021c9bdebd | -9.40837 | -64.37575 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a62ebcb2-f446-3639-ba42-a490dc2235c6 | -9.39868 | -64.41698 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 46febb43-cfad-37b3-ae76-5e22bccbbde7 | -9.35162 | -64.35165 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8585ab4b-3c9f-3b0d-8468-21efacd321a7 | -9.31404 | -64.45662 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce70750a-c9cf-334a-b872-6f12ef1805ed | -8.93492 | -64.23933 | 2024-10-12 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9f62aa9a-843c-333f-bebb-92015e0fc0a8 | -8.9343 | -64.24352 | 2024-10-12 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8d442a01-31e7-3373-a5f4-8c4a51bd03b6 | -8.65805 | -64.29826 | 2024-10-12 05:48:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9679db8a-475b-318e-abc6-ec25925262d1 | -9.64388 | -65.7382 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 58728a10-9063-3260-914a-0d4c5513b366 | -9.404 | -65.58868 | 2024-10-12 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 967f3a55-cfd1-3299-9a13-66362318264c | -9.40343 | -65.59242 | 2024-10-12 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 041ede8b-17e9-3a9d-8bce-ec01aa180b3e | -9.36144 | -65.75349 | 2024-10-12 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8fb3e166-8217-3961-8d1f-f9823fe9ec2d | -9.35973 | -65.74182 | 2024-10-12 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bf4d6550-0494-3c59-9483-2d92eb56485f | -9.35917 | -65.74554 | 2024-10-12 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c9abc655-70b6-3a38-a728-4df4416bbfff | -9.3586 | -65.74925 | 2024-10-12 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2d408f53-e4c5-3f4f-9d99-fac28b2a6484 | -9.35804 | -65.75296 | 2024-10-12 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 65223f04-c3e6-3dc5-bd43-6854d1fdad20 | -9.35633 | -65.74129 | 2024-10-12 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1ad3b023-d276-30f5-91c9-0529d6e77a88 | -9.35576 | -65.74501 | 2024-10-12 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b20287b0-4483-3ee3-b3ce-0418d4fa561f | -9.3552 | -65.74873 | 2024-10-12 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b04f6049-3769-3ccf-b54a-422dc786ad5a | -9.35463 | -65.75243 | 2024-10-12 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c9ccd623-a837-3d50-a1e4-a9dc570664ca | -9.35236 | -65.74449 | 2024-10-12 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae552b58-845e-37ee-a8a6-e162cc3ca99d | -9.31498 | -65.76141 | 2024-10-12 05:48:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d011bcc-3ef4-3817-ad9a-8f35e38b2d5c | -9.56459 | -64.62267 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c01b26e6-4b69-3f79-928d-dc0ad850371d | -9.53797 | -64.58092 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 977b3b87-91da-3ab5-817b-151cbcba2aa2 | -9.535 | -64.57628 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fa769957-0367-3d8f-a1ce-fb751a60606e | -9.53082 | -64.57982 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fb3ac25d-ac96-3303-ac11-4ce04b81722d | -10.74238 | -65.08124 | 2024-10-12 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c8ebf1e8-ba37-3174-b634-1dd19918b798 | -10.64322 | -65.14028 | 2024-10-12 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6419fc2-704c-3ee6-9d8d-fba0710832b8 | -10.64262 | -65.14428 | 2024-10-12 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b9eb032-52d0-3719-9e5e-9881abbc7573 | -10.6385 | -65.14776 | 2024-10-12 05:48:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96c556b0-013e-3c4f-93bf-13836529366c | -10.06307 | -64.93578 | 2024-10-12 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a2c7b66-3c53-3a24-b67c-5565f9e3d6dc | -10.05954 | -64.93525 | 2024-10-12 05:48:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 96036334-6ee9-3083-9629-d12463e21d69 | -9.92128 | -64.77162 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dac4adbf-1fe9-34ff-aa08-6f51dcd964dc | -9.91772 | -64.77106 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ba85a44b-7a6b-3e4f-809a-764575ff87e8 | -9.89163 | -64.80025 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8e0b8bfc-1204-3a1c-8280-21829986b6e8 | -9.89104 | -64.80431 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c0cad54-7e76-3c37-94d2-f54031563750 | -9.89044 | -64.80838 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b5061287-4749-3010-86ff-86ab91802826 | -9.89026 | -65.00533 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68dc66cd-dee7-3975-b60f-b5d00fc043eb | -9.88985 | -64.81245 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 36610d06-c421-3e0b-a4ce-c1ce1689ab7d | -9.88967 | -65.0093 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6662acac-9e57-380d-ace2-8334e9edaafc | -9.88925 | -64.81649 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 548c2264-910f-3116-bccd-be66b421fd0f | -9.88868 | -64.79563 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cae1c91d-9780-36f4-ac4c-4b1d0525876c | -9.88808 | -64.7997 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d17d3b81-50c4-30a4-ae56-d3313118620d | -9.88749 | -64.80376 | 2024-10-12 05:48:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README142.md)
