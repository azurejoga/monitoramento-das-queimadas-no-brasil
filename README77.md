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

## Dados Diários - Página 77

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b6c2abec-d86a-3136-aa3a-e048ff5051fe | -2.40554 | -51.28893 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd3b2a7e-494a-32ba-8dd2-9e40d4914cdb | -2.40492 | -51.29291 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00c1dfbb-911d-344c-94ec-6f54672f7fb4 | -2.402 | -51.28837 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a35a8e36-4631-3af0-9aa5-859cbedbeed4 | -2.40138 | -51.29235 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2513cb99-c7c6-3a33-900f-f8535727f707 | -2.39972 | -51.27987 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a54db972-e19a-39f9-a327-fba638493abc | -2.3991 | -51.28384 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 30b668a0-39b7-374b-b3a9-899cdc567c38 | -2.39887 | -51.30832 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0d41f0f4-cc60-307e-88ba-781c3c74394b | -2.39847 | -51.28782 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8784ac9-7886-303e-ad5e-f699f51cdee9 | -2.39784 | -51.2918 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8fab23bd-390e-3bde-9799-c2b8c3e7f91d | -2.39721 | -51.29578 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ef0da889-c7f6-3ab6-aae4-f9dde74d2d8a | -2.39556 | -51.28328 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fccfbc82-0ccf-3a9c-ad66-b98317b19eea | -2.39493 | -51.28725 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2d0ac6f9-5441-3fad-8be5-5418599c7f69 | -2.39265 | -51.27874 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f9a90642-34c0-3ca1-8352-1d4b125fba76 | -2.39202 | -51.28272 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 24146fc1-e265-3c44-834f-8db712a3bbad | -2.3914 | -51.28671 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49ed502c-f0eb-391d-8ea0-37f12acb768b | -2.38975 | -51.27421 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b07fba1-b341-3f2b-b5c2-511742b725b6 | -2.38912 | -51.27819 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ac3df78a-6272-3693-8334-0bc7039f1b94 | -2.38849 | -51.28217 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 95a1ec61-2582-3544-a026-61679373cfed | -2.38786 | -51.28615 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2e51cac0-8983-3235-828c-6a0125a2aea0 | -2.262 | -51.0974 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 88101fb9-a9cf-3084-bad7-c385d50156bc | -2.26137 | -51.10134 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b94119bc-e46e-3da9-b0d8-6395f0b9df1b | -2.87727 | -51.67766 | 2024-09-27 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| faed0716-3945-3417-a39d-95f591c6472a | -2.87628 | -51.66072 | 2024-09-27 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5648de43-4805-3d77-b473-a84b04ceaf1b | -2.87433 | -51.673 | 2024-09-27 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| e6bf6590-5bd9-3d23-b392-c6f0c31d650a | -2.87205 | -51.66423 | 2024-09-27 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| c551d8b1-5fc1-36ec-9a3a-ea315900150c | -2.8714 | -51.66834 | 2024-09-27 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| c0c294ab-09f6-3154-b25c-b1a630922b0c | -2.87075 | -51.67245 | 2024-09-27 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| fcbfe483-94d0-314f-a711-357507c09eaf | -2.86847 | -51.66366 | 2024-09-27 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 39279b61-60ac-3ac4-8d46-1b20b02cc5e4 | -2.86781 | -51.66779 | 2024-09-27 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| d5f66e7e-3f32-38c1-906d-4ff3c190a7da | -2.86716 | -51.67189 | 2024-09-27 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 1ebd5fa3-5432-3d69-8a2e-0ee78b1187be | -3.30113 | -50.66383 | 2024-09-27 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6f353821-7ab3-3871-8ee6-badcb373cb31 | -3.88221 | -51.92301 | 2024-09-27 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9aa018e5-5370-3ec7-989c-51c7e9e01b78 | -3.88193 | -51.90196 | 2024-09-27 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb721c2a-1131-3512-b9fa-1ac56e1adb8f | -3.87834 | -51.90142 | 2024-09-27 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d8972e22-70d1-3bde-8151-69e70d558586 | -3.87357 | -51.16809 | 2024-09-27 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 65f1037d-869c-35b4-a0fc-ae60aa64cb4a | -3.77214 | -51.01617 | 2024-09-27 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ca265c9e-7f09-3170-b40a-35a2489dbfd6 | -3.75056 | -51.29928 | 2024-09-27 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 195cecb9-1a55-3f08-a4e4-4d91c9bc5385 | -4.61687 | -50.95935 | 2024-09-27 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8e8e4978-a30f-37cf-ab66-616079fa9fda | -4.61627 | -50.96308 | 2024-09-27 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 95a334f4-6742-3d61-9112-de088700ea69 | -4.14789 | -51.05882 | 2024-09-27 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7ba0a469-aff0-383d-8aa0-b92581769300 | -4.05989 | -51.06032 | 2024-09-27 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 85e8e5a1-2bed-3f20-a179-17f33d032ec3 | -4.05764 | -51.05226 | 2024-09-27 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f2b3e9cf-723f-3b82-b750-9469f84695a6 | -4.04729 | -51.05071 | 2024-09-27 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| adadd8db-3c2f-39ff-bc95-863b6f05badc | -3.88155 | -51.92708 | 2024-09-27 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 811374ec-e587-3aad-a1e2-849f4ea93f49 | -3.87862 | -51.92245 | 2024-09-27 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86fb4c7d-a66a-3e2f-82ea-ef5e2d83655e | -3.87766 | -51.1648 | 2024-09-27 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5f26a91-a1d9-3459-82d0-6cdd8269f1d0 | -3.87419 | -51.16427 | 2024-09-27 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 92d62ec9-e365-3dcc-9263-f23f164cccb9 | -3.82048 | -50.90849 | 2024-09-27 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f60cd4bf-f0d7-3e9f-8f3d-6896a26111e1 | -3.78985 | -52.23942 | 2024-09-27 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 71fe2aec-5077-3a2e-ada5-e659e517092e | -3.77543 | -51.01308 | 2024-09-27 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 85a7ef98-5e79-3e61-82a5-81ea158035f3 | -3.74707 | -51.29876 | 2024-09-27 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7ab896a9-303b-34fa-9da2-83c0d346865b | -3.72145 | -52.22127 | 2024-09-27 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 09638da1-dc47-36f0-8c6b-31c64ee5cfad | -4.15072 | -51.06316 | 2024-09-27 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 172978e1-2249-377a-aff7-c48ac6f5b209 | -4.05537 | -51.04431 | 2024-09-27 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ad936388-03c9-30b3-95f7-47415f8575b6 | -3.95763 | -52.19928 | 2024-09-27 04:38:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 49dd86e7-3506-383d-b9e4-9f6099115dc6 | 0.90714 | -51.9961 | 2024-09-27 04:38:00 | NOAA-21 | SERRA DO NAVIO | AMAPÁ | Brasil | 1600055 | 16 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 286a476f-bd6a-37a2-a5de-9bda5c634188 | 0.90636 | -51.9911 | 2024-09-27 04:38:00 | NOAA-21 | SERRA DO NAVIO | AMAPÁ | Brasil | 1600055 | 16 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 2907949d-b9f1-3c01-a413-cd9ee2824bff | 0.90332 | -51.99671 | 2024-09-27 04:38:00 | NOAA-21 | SERRA DO NAVIO | AMAPÁ | Brasil | 1600055 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 057e3e35-e824-3986-bcfd-61b7221992b6 | 0.90254 | -51.99173 | 2024-09-27 04:38:00 | NOAA-21 | SERRA DO NAVIO | AMAPÁ | Brasil | 1600055 | 16 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 957e6168-5901-34f4-bf29-200cae8b103a | -3.41257 | -53.20633 | 2024-09-27 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56aeab27-9347-3889-956d-1c6d490101a5 | -3.39346 | -53.71807 | 2024-09-27 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04a9a126-eec7-3448-adee-dc408a504dae | -3.39291 | -53.72147 | 2024-09-27 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ff463824-ed62-3911-96d5-dc64fa975956 | -3.38944 | -53.71749 | 2024-09-27 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f0079107-94f7-37b8-88c7-2b37610a666b | -3.32407 | -53.2289 | 2024-09-27 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a7c0459f-ebe7-3334-890f-a451c7f637d5 | -3.30512 | -53.3688 | 2024-09-27 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3f6de5ba-f3ba-376d-b779-6010271cb14e | -3.30508 | -53.695 | 2024-09-27 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7fb7deb7-0914-3116-a014-3edc80150e83 | -3.30451 | -53.69855 | 2024-09-27 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c671eb7b-9c17-34fc-a982-37566c731faf | -3.30107 | -53.69437 | 2024-09-27 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c2847c5e-0055-3089-8136-2c6a50639bfe | -3.3005 | -53.69789 | 2024-09-27 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| def1c8ad-551e-3630-ba6a-a9aeeaf6cada | -3.29844 | -52.98547 | 2024-09-27 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a77aee66-8e1d-349d-a34a-4ec25cef88ad | -3.29649 | -53.69725 | 2024-09-27 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f13631c-3a49-3c11-a040-7eb99ef0618a | -3.29134 | -53.70364 | 2024-09-27 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fc336e1-241d-3921-8c97-bbed03c32b6d | -3.28921 | -52.72971 | 2024-09-27 04:38:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b872b57b-7a17-3596-9003-6fd0bd675186 | -3.28846 | -53.696 | 2024-09-27 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04e83213-85b6-35b6-9ac4-259ce74a6808 | -3.16343 | -52.4483 | 2024-09-27 04:38:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c84b96a-54bb-3965-bcc5-6fe021547f8d | -3.16715 | -52.44889 | 2024-09-27 04:38:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d098e348-4e77-39cb-906c-a189a6779e07 | -3.01436 | -52.18548 | 2024-09-27 04:38:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 38f5e0e8-e204-3d9a-b8ee-0c65e5dcb38f | -2.85813 | -53.3194 | 2024-09-27 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 611b0003-1821-328f-8194-9a420fe7bbf1 | -3.41588 | -53.20355 | 2024-09-27 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d99139c3-53f7-3672-a330-77eafb54b1a8 | -3.39401 | -53.7147 | 2024-09-27 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 42683552-f568-3e46-98c5-ea9c0fe00b02 | -3.38999 | -53.71411 | 2024-09-27 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 731ba395-54ca-3027-b731-d5261fec2e5c | -3.32487 | -53.22401 | 2024-09-27 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 96c152f2-276d-3362-9733-b95094972ccb | -3.3226 | -53.21354 | 2024-09-27 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 088cd23d-414e-3fb6-b16e-234048cbc67c | -3.30904 | -53.36947 | 2024-09-27 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00c19508-e033-36f9-a731-b67bb1041eef | -3.30822 | -53.3745 | 2024-09-27 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8667081d-3663-3c85-ae8c-cfc812b9a55e | -3.30429 | -53.37386 | 2024-09-27 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e22042be-6b36-3e37-935c-a26c6d692da2 | -3.30394 | -53.70211 | 2024-09-27 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 771439a7-eaea-38ec-9155-19b65898f545 | -3.29993 | -53.70143 | 2024-09-27 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 07a62d52-f8ae-3f05-8533-9f8600aa47f5 | -3.29312 | -53.11716 | 2024-09-27 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| af63bfcc-5084-3995-8cc8-cb5028690357 | -3.28789 | -53.6995 | 2024-09-27 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ba1ff10a-a855-3d46-92cd-78bb56c4279e | -3.25697 | -53.31788 | 2024-09-27 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 16c154db-37d1-32f1-8b25-d4d8b5cadd4e | -3.25306 | -53.3172 | 2024-09-27 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a1f362e-0767-305a-8101-b29d4e4d62ff | -2.85964 | -53.31242 | 2024-09-27 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 34eab653-4e37-348e-a082-6bb4791b13fc | -2.85896 | -53.31434 | 2024-09-27 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 01a78e1b-feb5-33c9-9a87-7d6dcfc235fd | -2.85884 | -53.31749 | 2024-09-27 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a8fd712d-484e-3506-ae3b-cfc192ec70e2 | -2.85502 | -53.31372 | 2024-09-27 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7396ccd5-5f20-3df2-a0bb-e0cefefea043 | -2.8549 | -53.31685 | 2024-09-27 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a5cc0884-177e-3d7a-bd41-417d83521468 | -2.85419 | -53.31876 | 2024-09-27 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 536963c6-54b9-3f4a-ad3b-cbb3182be7bf | -4.18921 | -53.82975 | 2024-09-27 04:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f46ccff-bf19-3010-ab19-3916b91e343b | -4.18716 | -53.82972 | 2024-09-27 04:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README78.md)
