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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 77e4c7e0-1c08-3ba9-8ff7-baceb3aaff37 | -4.92655 | -44.65834 | 2024-11-13 04:57:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 733cb9b6-c947-3d48-b983-c2d6933d7e20 | -3.35297 | -49.15569 | 2024-11-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 60e2bae5-f7a7-38d2-a9bf-4dd6fc3c8d1d | -2.7183 | -54.69002 | 2024-11-13 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1267476f-1600-3e05-8c0c-30238204b21b | -2.75679 | -54.03311 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a647a722-fd62-32ea-be55-7ba3b410fdd6 | -3.53212 | -54.49167 | 2024-11-13 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f513dfbb-ee8b-36ae-9c92-e75f97b949f8 | -2.77012 | -54.73045 | 2024-11-13 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 137cb389-666c-32ce-b7ca-943d536a6b0e | -4.33164 | -48.61406 | 2024-11-13 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a79d209c-6dd9-329f-9cd5-bf420c79884f | -3.53729 | -54.08886 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 91455c79-af24-3f93-ace3-e77d60ac2353 | -3.36148 | -54.58199 | 2024-11-13 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dbe0200f-5aed-3203-b4a3-ad8bb7858192 | -2.23292 | -46.43996 | 2024-11-13 04:57:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8f3a4378-840a-35b3-8876-f2ce88860584 | -3.52657 | -54.48371 | 2024-11-13 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 28860fa9-88e9-3fe7-bb42-cc2a0c6651cb | -3.54515 | -51.59472 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 16267201-eb01-3b66-812b-bb8cabc67e21 | -4.11266 | -51.09966 | 2024-11-13 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 32db6571-f7c6-3e94-9ae1-719fa6f306c2 | -1.18162 | -53.92371 | 2024-11-13 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 386e2df1-9540-3eea-bf24-c41b7fffdc19 | -3.0769 | -50.33304 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| a0d6d871-0dc8-3e8f-bc65-5f5cf43a6f73 | -3.76919 | -54.65007 | 2024-11-13 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d51ef278-55bd-39ef-bf9b-b703d7fd3bd0 | -4.11499 | -51.10807 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ca416eb1-1c6f-370c-b69d-70da600b9edb | -1.60913 | -52.40427 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e1a6eff7-0a5d-3ce1-af2c-ae95485bcbad | -1.20949 | -51.77555 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d85f8f61-5992-300d-9572-5165439d4a1a | -2.77134 | -52.86963 | 2024-11-13 04:57:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0a425b42-07ca-3ed5-8a39-b17dd3e1d99c | -2.43707 | -50.40186 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16447a5d-5fa6-3eb1-b410-2d25c64c177d | -3.40823 | -50.37021 | 2024-11-13 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 842a96e1-e634-303b-bfee-395ff98d7090 | -1.12099 | -51.9331 | 2024-11-13 04:57:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2b198e7-3980-3b04-88ae-d59dbbd588d0 | -3.74592 | -51.93288 | 2024-11-13 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 708ed196-ca7e-3b76-9336-84183c7a1df6 | 0.81004 | -50.67265 | 2024-11-13 04:57:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 755bc3ac-13c2-3bfd-b775-2ac48441906e | -2.69814 | -49.34503 | 2024-11-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 664cc18e-a6ae-329f-9705-4cf15a0d93b3 | -3.06236 | -50.33077 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ea831068-9bfb-31a6-9370-b9bf19cf6d85 | -1.39279 | -52.39553 | 2024-11-13 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 357e6ffd-52c6-3f91-8272-7650f2c4f04f | -2.12112 | -50.69185 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c60cd5c1-3164-39e6-a8ad-7e6a3e38e208 | -4.21755 | -55.30535 | 2024-11-13 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab0b082f-50bd-32a6-9328-203a3217bddf | -3.76745 | -51.27113 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08e79997-2d5b-30f9-8dc1-1ebbf98d9250 | -2.54743 | -53.97946 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a8fe6674-0b9f-3875-88de-44513fac7b24 | -2.809 | -54.00235 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cc3e4278-8817-36be-822f-5dcad396c8a2 | -1.22738 | -51.74897 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0931b07-66df-3010-9b41-2cbed23be4d5 | 0.72488 | -52.01369 | 2024-11-13 04:57:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 141db4b8-cc53-3467-be8c-5375e79754ab | -3.76587 | -54.64955 | 2024-11-13 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c1f7e3df-9c2d-3261-8dfb-936dad516aee | -1.39408 | -51.4402 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e63a288c-1f65-3e44-b941-7c606a276d37 | -1.65969 | -52.62554 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 64d3b3f7-486f-3ca2-a102-0fd65c9e1bfa | -2.80743 | -54.47063 | 2024-11-13 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 729899f6-25f6-3af9-8d8f-9fa4a6619366 | -2.9881 | -51.34232 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a1eead2a-59ad-3f34-9cce-77fd30fc9553 | -1.79362 | -56.25944 | 2024-11-13 04:57:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d30292b2-14e1-39cc-94b4-645f6c2bc9a1 | -3.62865 | -54.11377 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 87f26116-87d4-35d4-913c-97b337010222 | 1.06002 | -60.60266 | 2024-11-13 04:57:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 0ce997f9-9fb6-3bec-a683-2e7e8eca19eb | -2.81686 | -54.71602 | 2024-11-13 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb2fa93f-b5f1-3b5c-9567-f974ce269054 | -3.04571 | -50.33798 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4f3e3131-d90c-3920-bb8a-bfb69d4564f5 | -4.63038 | -48.90222 | 2024-11-13 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d2daab2-5dc5-35be-a00d-ac0c8687c591 | -2.96087 | -53.86114 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 443a0e1d-6b5a-37e0-937b-456232af231b | -3.07326 | -50.33248 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| e80df368-6ec9-3157-b6b5-0aa5f5e2b1f7 | 3.16225 | -60.66858 | 2024-11-13 04:57:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 333ca83b-1d87-3e4d-b210-8dd6106d259b | -3.82004 | -51.26254 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 39dd9fbd-288c-3ffc-bc68-87145bfcb258 | -4.89291 | -48.06284 | 2024-11-13 04:57:00 | NOAA-21 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b90e108-8c82-3288-a489-cf948c66d0e4 | -3.73554 | -54.43156 | 2024-11-13 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1a734ea0-41ed-350c-b139-0ae6d48da87a | -4.20311 | -55.15704 | 2024-11-13 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dcfbe18b-3a64-3cf5-8f61-5fb714bf4684 | -2.25842 | -48.32978 | 2024-11-13 04:57:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 844bdce8-85b1-345d-89d8-dfc45dc011c3 | -3.11011 | -50.21165 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fa5ae1ba-0ed2-36ac-8353-177a9d56a21f | -1.42022 | -51.10953 | 2024-11-13 04:57:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 269b1cfa-de51-3b39-a5b6-ddf57802fea4 | -3.85656 | -49.11661 | 2024-11-13 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f6680ae5-af3a-3dd8-8d6a-8edefcad4f1a | -3.08964 | -54.55789 | 2024-11-13 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 06d20f56-fa39-3bdd-bb6a-99291480fb8e | -1.4202 | -51.11408 | 2024-11-13 04:57:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fada3cc5-854e-3cc9-a820-66a403bc3c08 | -2.19872 | -53.2284 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8010daf4-d9c4-3ad3-bf2c-f288b82128c6 | -2.40178 | -53.73455 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1eace619-77b1-3637-b43d-47dc6c111ef2 | -2.89955 | -53.05225 | 2024-11-13 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3417da47-5a0d-3577-a8c9-16d19fbf2016 | -3.67256 | -54.65948 | 2024-11-13 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1ce99c5b-4384-3465-a887-dadb299c82e0 | -3.95503 | -46.41268 | 2024-11-13 04:57:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 5ca7ef1d-8b75-3f49-ae14-7e811f8e26f1 | -2.20982 | -53.74707 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b5245c13-d02f-324a-b9f5-e6ce056f4ec5 | -1.41859 | -53.47504 | 2024-11-13 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d0c93ce3-2b51-3f87-9811-39fb7864dbd2 | -3.42035 | -51.0563 | 2024-11-13 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5c585c7e-f86d-361f-a722-a875c9fb4c74 | -3.05131 | -50.32584 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4be4d41a-31bf-308a-98be-831730fb6998 | -5.33085 | -46.09719 | 2024-11-13 04:57:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 57758e46-4a11-33f9-b34e-e406ec9bfc0b | -2.62605 | -54.28169 | 2024-11-13 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d1c6dcff-3c3f-3cf6-84a2-dc1551e58691 | -2.15589 | -50.91317 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a3251337-f321-3bc8-b9d0-ac675d765405 | -1.98176 | -51.99595 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6c62b153-b646-3698-92ce-18378ce8a7c3 | -0.16316 | -51.75 | 2024-11-13 04:57:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2392aaf-69c6-380a-abc6-99c0df0e07ff | -2.91717 | -49.25139 | 2024-11-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b6cc95e-6f59-3fcd-a83d-aa89538f4b6a | -2.94302 | -54.10492 | 2024-11-13 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 24e5f181-9164-3e00-84f3-c0fad4d056f9 | -1.62441 | -53.26471 | 2024-11-13 04:57:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 254de918-9d98-3208-a590-7ee2ddd08d34 | -3.53266 | -54.4882 | 2024-11-13 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3f046324-c876-3b10-b0bc-64e4abeedcb3 | -3.03016 | -53.72064 | 2024-11-13 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f72ed37b-dd91-363c-863e-4371a67e5763 | -5.36444 | -43.53266 | 2024-11-13 04:57:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2f619a3-3c90-3d7f-8220-0561122f68ad | -4.81833 | -48.75513 | 2024-11-13 04:57:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca17bbfd-2ef4-3cc8-881d-cba93764f6e4 | 0.15613 | -51.13807 | 2024-11-13 04:57:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 142f41f6-f240-3d55-9b37-082ab6466be4 | -2.20593 | -53.74581 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 270c75f0-7c68-3e2b-a5c8-2fa9a5d7863f | -1.17262 | -53.74238 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0bbc63f4-c6dc-3c6b-9a9b-ae9d2a406d78 | -2.91861 | -49.24174 | 2024-11-13 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b9f7577-2bb4-3591-a857-86fd8dec0d40 | -2.44386 | -51.95614 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a099f54-fb3d-33bc-869d-4e7a410ef3af | -3.93119 | -50.03189 | 2024-11-13 04:57:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4aced65f-8090-37e3-ad9c-bb704658a76e | -3.05661 | -50.33963 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3c303b5b-a70b-3425-b3ed-c3a60ca42392 | -2.48322 | -53.97591 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4257351d-3183-37f7-9eb6-7dfadec6787c | -2.3781 | -53.8646 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c2347054-4008-3453-8dae-ccc89e97012b | -2.29142 | -53.78777 | 2024-11-13 04:57:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 989c44d8-be14-34cd-9138-87dff870b5cb | -2.32298 | -50.67561 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1316aa2c-64a6-3d53-9202-fcc8fd445cab | -1.03736 | -48.85083 | 2024-11-13 04:57:00 | NOAA-21 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5c8e34af-189a-3004-bcb8-1d2e0a11ec9b | -2.45292 | -50.37045 | 2024-11-13 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7394859a-34a0-37e6-987a-4b5f64e61f1b | -4.61109 | -50.91271 | 2024-11-13 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f013b139-d52a-3af7-8493-a043938e79ed | -1.21672 | -51.751 | 2024-11-13 04:57:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f5112667-17d3-324f-919e-ac08e1088800 | -2.81419 | -51.80799 | 2024-11-13 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9e345237-a112-339d-8d0c-59e026bda667 | -3.31602 | -54.91651 | 2024-11-13 04:57:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80c55e1a-671c-3d04-a1ad-5f064f74d72e | -4.05675 | -55.79082 | 2024-11-13 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f98f7abd-64c9-37db-bd1f-68685726e05e | -3.75838 | -51.6451 | 2024-11-13 04:57:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f818e024-0540-33c9-84ca-a486dd50f255 | -1.60634 | -52.40027 | 2024-11-13 04:57:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README31.md)
