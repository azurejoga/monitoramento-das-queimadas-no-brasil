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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 10589fb7-6379-3a22-9cd1-dc5c7fedc377 | -5.87029 | -53.48769 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 352729d3-2961-35a8-bf5d-2750d99c7a54 | -4.29811 | -50.77232 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9befd396-88d0-3a7d-895c-6570a8167834 | -7.83545 | -55.13417 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24ed39d0-f20e-3972-8f56-7b026bf0e36f | -5.87361 | -53.48819 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60f1a973-0553-3f95-b351-2cc39d5a0cec | -3.4745 | -54.62425 | 2026-10-02 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 90cb5434-6eea-3bb4-8c38-b09b989931c0 | -4.45903 | -47.92713 | 2026-10-02 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 3396c726-7b97-38a2-98b4-8b7d75a28fdb | -7.73185 | -54.81576 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0f80fc05-1872-3388-adef-988e11584a35 | -4.29028 | -50.77538 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c25d64b1-0629-3a65-a6dc-e8236e03e342 | -7.59495 | -55.06003 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c0e002f0-4576-3d44-88c2-ec9cb17a73a0 | -8.212 | -54.72946 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4c9cb2d4-df83-370e-aad9-f7cf286dcc19 | -3.8486 | -55.9702 | 2026-10-02 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1f7e7068-c912-3048-bd54-780af005f665 | -3.60578 | -55.37091 | 2026-10-02 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4e07fb07-6570-38c5-86b6-69874b104b5e | -7.54647 | -55.02396 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0da85655-751e-36e2-97ab-6b52fe0f1ce6 | -6.84881 | -55.54215 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83b2439d-8989-3d22-bdac-af4cae86aeb5 | -4.35959 | -47.77456 | 2026-10-02 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8515493d-d3b7-3aec-9f4d-3eee4691600b | -1.486 | -55.8705 | 2026-10-02 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c44651c1-d584-3b00-b5ca-946faf4c0d5e | -3.16563 | -54.09699 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3b5ab1f9-7277-3903-8336-5a0adf50364d | -7.6312 | -55.04803 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d0d8ac5c-f2f2-3273-8a1e-9a7b96b8bc6a | -4.0423 | -54.23873 | 2026-10-02 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d8d9670-7607-399a-9c46-26a25b197b2f | -3.85046 | -55.8023 | 2026-10-02 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0d7a8591-a83d-3b31-982f-f647ef418966 | -2.93159 | -54.20121 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c07d4894-88b2-32ac-acf3-fa50a6a5629d | -3.29941 | -53.85065 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 09789b00-dcf0-3073-bc66-82c097610eab | -6.39883 | -56.40886 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c034d57-7d20-35c9-bb47-255b01468428 | -3.29558 | -53.85357 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c81945b7-8bcb-349d-a129-27cb40c242a8 | -7.28931 | -55.5759 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 43126ef4-8d75-30d4-97e8-c7c15476a460 | -6.67739 | -52.48771 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2a6a6ee8-9d2c-3106-8549-057160458649 | -6.90086 | -43.69074 | 2026-10-02 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 35bbb862-af63-315a-9b13-a4e65e485cdf | -8.2603 | -54.70161 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2a0e3c8-af24-3542-b1d7-53d02480c432 | -6.24171 | -53.13089 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 73a9087a-58c3-3190-88d1-fa1ee70ee600 | -5.26862 | -56.05278 | 2026-10-02 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b508398b-9aa8-3437-8251-be1b062f1bc1 | -4.29315 | -49.09579 | 2026-10-02 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b87000df-3b69-3a9a-b321-3c334bbabb09 | -7.73731 | -54.80244 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 69df3e4e-7369-3b68-aaee-499443960ef6 | -6.23841 | -53.15228 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 374bf27b-544b-33d8-b686-03a824a400d5 | -4.48592 | -54.87967 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6412edfa-2813-3f62-a0ae-eded41dbe809 | -7.33948 | -55.58029 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 82caa0de-3f96-3fb7-b63e-4fdde9d4f2a2 | -6.72194 | -44.28089 | 2026-10-02 04:57:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 981b75d5-e075-35f9-aa20-2ff5f0082328 | -5.86595 | -43.59553 | 2026-10-02 04:57:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 30047d64-ac7c-3508-b073-b9a5d49b6833 | -3.17215 | -54.07687 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 10d78b2c-f59d-33aa-bb34-fea4e09018ab | -3.87767 | -51.8948 | 2026-10-02 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 4d97019e-9fac-3bbc-ad44-754363e7e6aa | -3.01796 | -53.89064 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 77ba008d-0d32-3452-851e-cf7517ce944b | -5.99688 | -53.54974 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57ee0609-fed8-3951-8338-d5d7e97c171a | -7.28875 | -55.60106 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 678c097f-4227-31ba-b7f3-abc7f30fbc2f | -3.01882 | -53.97157 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| cd15bb6b-000b-3c49-ac16-2a3edda00c68 | -3.48022 | -55.41037 | 2026-10-02 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 37d663bd-e612-32fd-af82-ed0b22857463 | -7.04295 | -55.627 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d51744b7-c0d5-3f69-b9a8-6bd38cf513e1 | -3.175 | -54.10196 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9b9db113-261d-3fb8-aff2-441b9bdac2dc | -6.89375 | -43.69867 | 2026-10-02 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 588897af-5dbd-3bb5-8841-67d111370e5c | -7.75458 | -54.80512 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 98f755f1-48f9-3418-a7a0-2fb4ea2269e1 | -7.78706 | -55.63422 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2b20501-8db7-325d-9aa9-d24a31b66442 | -3.12238 | -50.2784 | 2026-10-02 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5565de1f-9c9b-3aa6-b4f3-4177ec190fb2 | -6.33368 | -43.38062 | 2026-10-02 04:57:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b86acf76-bfe1-3888-991f-11ed4ba3a5e8 | -6.14924 | -52.80136 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9ed9063-6a2f-3b4d-9223-ab7dcf5106ee | -5.72331 | -47.41616 | 2026-10-02 04:57:00 | NOAA-21 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 11babe39-c88d-37fc-ba88-4ef1da599dc8 | -4.45219 | -54.89944 | 2026-10-02 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d46278eb-ac2b-3df2-b700-321f9a7c33ed | -4.25255 | -50.75679 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0cd4cd4f-ce85-32da-b647-ac04edae1bbf | -5.13919 | -49.86795 | 2026-10-02 04:57:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3abf98ee-6d26-367c-b4a4-a9c7caaa0967 | -1.65739 | -55.21176 | 2026-10-02 04:57:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8f4e16c4-fca1-3a3d-a6b5-28581cc15ce8 | -3.29665 | -53.84671 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ff7768a0-3e85-30ea-974f-b07ed6045841 | -6.31986 | -43.34637 | 2026-10-02 04:57:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 270e796d-41f8-323a-b416-9ebbda8e9114 | -1.90819 | -55.04501 | 2026-10-02 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d3cf6906-220e-3cb7-8466-ab7e9271ad5a | -2.86235 | -49.62917 | 2026-10-02 04:57:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5d49ddf4-56b0-3256-9e72-c607f125bc53 | -3.0706 | -54.37934 | 2026-10-02 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 864422ff-e053-3042-997c-30bdecbc363c | -2.551 | -57.40488 | 2026-10-02 04:57:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 31ee5b63-2a84-31a2-a632-cf450e99f7d5 | -6.43587 | -55.80446 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 594f8b7f-ccb3-3854-9103-e9ba74166a6a | -6.18204 | -52.90203 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 262be590-be87-38df-a260-2bf08e672d53 | -2.5487 | -57.40334 | 2026-10-02 04:57:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 75b300f1-61ca-3d97-8f9e-412be9e367ad | -3.13572 | -53.74792 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 14ca0ab4-72ae-38b5-bc11-b3b1bc6de869 | -8.16544 | -54.80654 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1be2ff04-4911-30ce-8f00-ae691043f67f | -3.06729 | -54.37884 | 2026-10-02 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c051f44-3c5b-31c7-9243-92d0e1d10804 | -6.84659 | -55.53458 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a26dcd9a-cacb-3ad2-b1af-6f6af472dc79 | -6.86687 | -57.7189 | 2026-10-02 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 07f67ac9-fdc3-3fac-ba71-207a5d1ca2e4 | -4.26993 | -50.76379 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34b24028-c78f-312e-a17d-6d3179e68057 | -4.06813 | -51.09314 | 2026-10-02 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 096f20cc-77f5-3ac0-b7fc-e0df58feb813 | -3.15902 | -54.09597 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa56c95b-5974-3c20-988c-c1c70953d716 | -2.92659 | -54.18985 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 08043930-8208-3a70-b35d-f86e270d116e | -7.63177 | -55.06588 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 20235433-8ae1-35fb-900c-d0653c8ce24e | -6.2666 | -55.43462 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f53dcca9-664e-3af1-a1c8-7055bce3d956 | -6.19366 | -52.80436 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e2896eda-ff24-3cb8-8677-ff4dfa3c8afa | -7.28598 | -55.59704 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 26b50cf1-269a-3586-8096-99c6f16151cd | -3.61501 | -51.79884 | 2026-10-02 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 236a5a0e-1b0a-30e3-bc1a-1eaf04b09b5f | -5.74216 | -55.74204 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0a41d0e6-5eb7-38d0-b09e-6711fc4e4e46 | -5.9735 | -55.37359 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32386020-ceb9-3bae-9ecc-c87c26677fe9 | -3.23012 | -54.31555 | 2026-10-02 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2979e9ea-2f9c-3b1d-ba2a-6fc65012dd2e | -3.00415 | -53.87093 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 79436b95-f696-337c-859f-3a51fed8e8c5 | -7.31898 | -55.23637 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2621a4dc-1d3d-33f7-a9dd-a0192e0c49d2 | -2.96586 | -54.09367 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b5589779-0e8c-3138-afb6-50f30d06c300 | -2.77657 | -54.69048 | 2026-10-02 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 374b5079-9bbf-38cf-9213-af46313fec46 | -4.26867 | -50.77214 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6f696fcd-eca2-3474-b092-58aba5953b32 | -6.27313 | -53.34532 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6894ea5-93ea-3ea3-a043-7618bbf4a9da | -6.12688 | -53.19257 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2f886dcb-8b3a-3a04-ba1a-b08d3c3c3f91 | -3.80669 | -51.02631 | 2026-10-02 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b5175c9-6ad5-335f-8e90-76fe078ac64d | -7.3915 | -55.20863 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 078262dc-528f-3ab8-b602-d2c1b7315864 | -3.015 | -53.21215 | 2026-10-02 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f7e8e964-b581-340d-808b-ab03f5b38748 | -7.78097 | -55.62963 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12d98f75-69ab-31ae-a020-0baaf0333e04 | -1.1034 | -54.14219 | 2026-10-02 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c31058b3-e32f-3f79-b9c7-8153c19a7ce7 | -6.73328 | -52.95615 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe0f3857-07fe-3a42-a9d7-472e454ca6e9 | -1.34063 | -54.69505 | 2026-10-02 04:57:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6ba7ea2f-26f3-366e-a607-06c14b2211f6 | -3.11636 | -48.59849 | 2026-10-02 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2737b28c-b970-36f6-b40a-e36dd73eeac7 | -6.0002 | -53.55028 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e428a7a6-685c-35e9-ba8a-18023a132fcd | -8.18026 | -54.79822 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README60.md)
