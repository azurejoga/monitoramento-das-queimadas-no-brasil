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

## Dados Diários - Página 126

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3df05f2e-e6bf-39d0-8b3e-4553c55f11a3 | -3.25968 | -54.1863 | 2024-10-09 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e413a2c9-9ab2-3d82-b1e6-17b05c12c9c9 | -3.25923 | -49.10766 | 2024-10-09 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87459335-001a-3d3b-9b0c-5abe6699823f | -3.25907 | -54.19005 | 2024-10-09 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 62b301ca-9f4d-3035-8a2c-026eb799ab8c | -3.25868 | -49.11113 | 2024-10-09 04:38:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f96e13e-87d7-38f5-ae4e-a9a9998379e2 | -3.25848 | -51.23758 | 2024-10-09 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| db7be560-7407-3e2c-a4fd-500ac026c7bf | -3.25847 | -54.19382 | 2024-10-09 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a730aa66-52a5-3e93-a417-746b312bf58a | -3.25784 | -51.24157 | 2024-10-09 04:38:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e553a0c5-39e2-394e-a33e-1f7e6990a11f | -3.25677 | -51.59261 | 2024-10-09 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 36eadb9e-23a3-3447-b000-c3e45d5289b5 | -3.25549 | -54.1855 | 2024-10-09 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 282721e2-1fbe-373b-a92c-cff9bf0a8ce5 | -3.25488 | -54.18925 | 2024-10-09 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a741fcb-fdeb-36b2-a9fe-54f657d30493 | -3.23049 | -50.84747 | 2024-10-09 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1484c32-c265-3d7a-a1bb-57140e6c84d8 | -3.22988 | -50.85132 | 2024-10-09 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3b9667f0-4a21-3c48-88d2-a8dd4eee8f00 | -3.22175 | -50.92478 | 2024-10-09 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1a35218c-4f19-33cb-b052-1a9d52033af8 | -3.22043 | -53.00908 | 2024-10-09 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3a37a7a-67b3-3b78-b06d-2d9c35dd6302 | -3.21887 | -50.92038 | 2024-10-09 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 35a89f80-b24e-366e-a0e0-f570fa798dcd | -3.21654 | -53.00841 | 2024-10-09 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 878cf6e1-a115-3868-8529-ba1f51e22829 | -3.21538 | -50.91983 | 2024-10-09 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cdb832df-d6c3-325d-b297-682e03f5b4ee | -3.21188 | -50.91927 | 2024-10-09 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96ce559f-8df2-3fbe-9a04-5b3e0bb5bfb3 | -3.20901 | -50.91486 | 2024-10-09 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fedba9d1-9334-3374-9042-c19f009e2a5a | -3.20839 | -50.91871 | 2024-10-09 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e9604a3-3216-3c8b-9d46-5a53ae396fbb | -3.20802 | -48.81251 | 2024-10-09 04:38:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4f74270b-e7f7-3f19-973b-102804e3a411 | -3.20552 | -50.9143 | 2024-10-09 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b340b4ac-7c9d-3852-9ec0-6c7a892ad11a | -3.2049 | -50.91815 | 2024-10-09 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c7df7b19-21f2-3312-93c3-d7c9bb063551 | -3.20203 | -50.91374 | 2024-10-09 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 195427d6-5472-3984-9171-f7d771d41a77 | -3.20141 | -50.9176 | 2024-10-09 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2feed6d2-1e7b-37c0-9a35-82748fe476cd | -3.19915 | -50.90933 | 2024-10-09 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f95f9c92-0b65-3cc8-be58-303fff7274bd | -3.15451 | -54.56443 | 2024-10-09 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9618fb0b-a52f-3589-9431-ffa4550a7122 | -3.14582 | -51.19637 | 2024-10-09 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a419614-f1ed-335a-ad4a-c402c91a5d23 | -3.14519 | -51.20031 | 2024-10-09 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8edeee25-8630-3548-832f-b89393984e04 | -3.14229 | -51.19576 | 2024-10-09 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eb1a7091-b201-3dd1-9755-f8f8ebd4f448 | -3.128 | -53.7406 | 2024-10-09 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 16d095c3-3a6e-3227-87ad-cf222fd221b8 | -3.12449 | -53.73631 | 2024-10-09 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 75cc2816-56db-37d4-a439-90b59cb52376 | -3.12391 | -53.73994 | 2024-10-09 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 99fd0413-e4e6-32c8-a101-3549572ebe55 | -3.12378 | -50.42285 | 2024-10-09 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f11e9223-ad9e-3bf8-a68c-b1deeb4d4816 | -3.12098 | -53.73202 | 2024-10-09 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8edc7300-1e45-3201-8b7c-7523dec5bc07 | -3.1204 | -53.73564 | 2024-10-09 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d6aab12-73c1-3591-8148-0708897f433f | -3.11689 | -53.73137 | 2024-10-09 04:38:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 12c045f0-2850-3092-9616-c324cf70ddb6 | -3.10904 | -50.38264 | 2024-10-09 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6ca38dc8-5952-3405-9a95-cc12faed5c51 | -3.10845 | -50.38637 | 2024-10-09 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 223cb97d-5bea-36fd-b72e-ec0bd9ed2036 | -3.10562 | -50.38209 | 2024-10-09 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5bb8fe79-248f-39f0-b3b7-644f878d647b | -3.10503 | -50.3858 | 2024-10-09 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 47fc143d-4457-39a9-808f-65900157e7f9 | -3.10444 | -50.38952 | 2024-10-09 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e1be8f4b-3a40-3936-9604-253a108cabba | -3.10219 | -50.38154 | 2024-10-09 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dcc1372a-3e5f-34e7-9abd-6c010720f17c | -3.1016 | -50.38525 | 2024-10-09 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c57a311-dd79-3286-95c1-8754c527a8cc | -3.09959 | -50.46463 | 2024-10-09 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4bc26891-f874-3067-b8f2-dbf3e38dc1e6 | -3.09901 | -50.46834 | 2024-10-09 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e5a9c002-4a5c-37ba-bdc5-b40d9c876854 | -3.09724 | -50.47952 | 2024-10-09 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3aac1c19-77c1-374a-8fbc-6c50e7c713d7 | -3.09615 | -50.46409 | 2024-10-09 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 95e02ded-2c19-300c-a448-6a5007d472d0 | -3.09272 | -50.46354 | 2024-10-09 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7e31034f-3dd2-3b0b-b360-490711808ba5 | -3.08261 | -54.53306 | 2024-10-09 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 434a8f21-3f4d-35d5-b8d2-99d37efa7876 | -3.07677 | -61.0646 | 2024-10-09 04:38:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a0af0a20-a81b-3ef2-b62b-3c18356074e5 | -3.07543 | -50.48366 | 2024-10-09 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bb328c69-6604-3999-9841-d1153e57a96a | -3.07484 | -50.48739 | 2024-10-09 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67d33e8a-c1d7-3cdd-ba22-df186e4adea2 | -3.07199 | -50.48312 | 2024-10-09 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b7eae57b-3df7-3b31-a035-1116763608f8 | -3.06628 | -54.77331 | 2024-10-09 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 64bf8ab9-ae0f-3eba-8101-679f5c060728 | -3.06561 | -54.77748 | 2024-10-09 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4a807c45-fd08-34cf-bf4e-95af592de981 | -3.06121 | -54.77681 | 2024-10-09 04:38:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db1194fe-bded-35fe-9bbf-e0d1446c9087 | -3.05006 | -51.09771 | 2024-10-09 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b3c2b29-ff1d-34f3-acde-22728a37bdf1 | -3.04955 | -51.14588 | 2024-10-09 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ef8e7845-e357-327f-afff-33fc04abd6df | -3.04734 | -53.0382 | 2024-10-09 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9ee990e5-7f6b-35de-95ff-cae4bb35c112 | -3.04654 | -51.09713 | 2024-10-09 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0bddb8de-8998-3080-a518-531b77601a13 | -3.04601 | -51.14532 | 2024-10-09 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a69ce61-affb-3d05-8390-270f26303801 | -3.04599 | -50.29778 | 2024-10-09 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd568937-96d6-3de4-8f40-81c3b9fde5c2 | -3.04549 | -50.29716 | 2024-10-09 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e4eefe4-67cd-3d77-91cb-86f3155e27b6 | -3.04538 | -51.14927 | 2024-10-09 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e182545-4b64-3be2-95ce-8ae27bd87bdb | -3.04356 | -53.0409 | 2024-10-09 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cd597203-b6a0-304f-aa6d-e853816bb56d | -3.04278 | -53.04588 | 2024-10-09 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fc6b35d8-9065-335e-941c-77f4936ce34e | -3.04262 | -53.04247 | 2024-10-09 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 77ef76ce-f56a-355f-b61a-5e9c653fe11c | -3.0418 | -53.04744 | 2024-10-09 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 74943af5-d617-30cd-9018-f80c8ddbfd4e | -3.03887 | -53.04522 | 2024-10-09 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f6b83ef-b417-38f7-981c-b2e990adb0cc | -3.0387 | -53.04185 | 2024-10-09 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f0edd735-1de2-339f-9950-6b76f9d48790 | -3.03573 | -53.03966 | 2024-10-09 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a9aa7e38-8e3d-35e3-a00a-1dd609a8c2fe | -3.03495 | -53.04459 | 2024-10-09 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6280679a-2586-32b9-80b1-dadd8dcae6c4 | -3.03478 | -53.04124 | 2024-10-09 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 153029a8-91e9-360c-a330-b77904efdc29 | -3.03427 | -52.53113 | 2024-10-09 04:38:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4cf31063-550a-3e92-9d87-2466a655474f | -3.03405 | -51.10732 | 2024-10-09 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 77964a31-43c5-3be8-ade9-d7a4f78b1aa1 | -3.03352 | -52.53574 | 2024-10-09 04:38:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ee5cf7e3-e69f-3fc0-9d36-8d88d83aea4e | -3.03116 | -51.10283 | 2024-10-09 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 970435dd-3d14-301d-9550-d1b8e748f3b3 | -3.01936 | -59.10252 | 2024-10-09 04:38:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 484fae0d-0400-38c7-87d5-4329b5746023 | -3.0177 | -59.10029 | 2024-10-09 04:38:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 44f2d567-c140-3f75-8d52-0a2e6793add5 | -3.01698 | -59.10448 | 2024-10-09 04:38:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8b2a7b9b-bc9c-3d58-994c-55882de7f542 | -3.01351 | -59.10131 | 2024-10-09 04:38:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 308e9e50-266e-38d2-939a-cba45beeecc4 | -3.01281 | -59.10555 | 2024-10-09 04:38:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 895718c5-40c9-3757-a969-15d1c8c0ba6b | -3.0121 | -59.10985 | 2024-10-09 04:38:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 749e24c5-0ead-3a74-be30-ecbb737cfa0d | -3.01111 | -59.1034 | 2024-10-09 04:38:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7beba2b9-ab18-3313-967d-c2977fbe4028 | -3.01037 | -59.10769 | 2024-10-09 04:38:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 510744c6-e201-3dab-8a01-4366a81b0f41 | -3.00964 | -59.11197 | 2024-10-09 04:38:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6279317e-f420-3f9c-840e-4561a9f468a5 | -3.00619 | -51.43819 | 2024-10-09 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 86464d28-636c-38d6-a046-1cb61e20b2fd | -3.00553 | -51.44226 | 2024-10-09 04:38:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83ca8675-df78-33ee-9438-2d28f9ec26c9 | -2.97772 | -53.71589 | 2024-10-09 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6f079121-0d92-3de7-b4f3-572756ca0d81 | -2.97714 | -53.71946 | 2024-10-09 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 06859b9f-fa1c-3737-851c-1de75badd753 | -2.97655 | -53.72308 | 2024-10-09 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 6a663551-07f0-3e2a-861b-e00169b13021 | -2.97363 | -53.71518 | 2024-10-09 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 5a588008-659d-38c5-b306-10ef5bad1090 | -2.97304 | -53.71879 | 2024-10-09 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8f2f5b3c-ed71-3dff-b9cc-137d85720923 | -2.97246 | -53.72241 | 2024-10-09 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a4feb988-463f-3043-b404-baa6311c3351 | -2.97064 | -51.02913 | 2024-10-09 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9087645e-d97a-307c-8a76-fb5b995ba310 | -2.96867 | -51.10919 | 2024-10-09 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5b094a0-1c06-39c2-b502-1bfc6a2ed8d9 | -2.96836 | -53.72175 | 2024-10-09 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 426a12ac-bbed-39dc-b211-de098a0fd1ed | -2.96805 | -51.1131 | 2024-10-09 04:38:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 50374509-86cc-383d-97cb-824fb2a3f3f0 | -2.94967 | -53.70757 | 2024-10-09 04:38:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README127.md)
