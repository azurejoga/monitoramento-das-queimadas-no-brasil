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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bce723f3-9efe-3208-8a2a-4735b0e177cb | -11.30408 | -43.66307 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ddd60b0-ef33-38d7-8aa8-d30d05aa8c9b | -11.8849 | -46.35118 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 90a397d3-92e0-3ab1-9569-22f32baf990c | -11.90264 | -46.69106 | 2025-08-31 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2096aa4e-f48a-38d9-bf8a-44439971a661 | -14.99294 | -46.70347 | 2025-08-31 04:29:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fb3542b8-3193-3346-990a-f9c16db17ca2 | -9.7004 | -47.04413 | 2025-08-31 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de5de3f2-e8c0-3847-be4f-02fd330dd790 | -13.50842 | -46.97525 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| af7ac07e-a208-3651-9f6c-5a1293cf2b87 | -11.88097 | -46.72048 | 2025-08-31 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 035decf4-060e-3c80-a035-14eca4e37933 | -13.68457 | -46.88939 | 2025-08-31 04:29:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8c365122-48ad-3c8f-bc62-cd10a9ff3f03 | -12.8815 | -49.17862 | 2025-08-31 04:29:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5887b486-7738-3dab-91c2-7ada144515fb | -11.32703 | -43.66188 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 869e15fa-3686-33e3-ba99-de90ffcb5268 | -13.37204 | -46.957 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2277626-4787-35cc-a4dd-992ee14667e9 | -11.29909 | -43.67134 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a86ad96c-3e44-3a49-b8ff-d6738ec84138 | -14.35548 | -51.89211 | 2025-08-31 04:29:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9fc1f653-0ff3-32be-a692-714045b279e7 | -11.94721 | -46.69081 | 2025-08-31 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eefeb95b-8895-3383-8d37-4953a5e42cef | -12.39544 | -46.47842 | 2025-08-31 04:29:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 338beaeb-2123-38a9-ba50-798e5fcd0628 | -12.60572 | -57.01717 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 584dcf0b-23a5-39ac-8ba2-a6ebdf67e801 | -12.91632 | -56.98363 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5be4b864-729e-3c4a-8715-5939b7b9663f | -16.07824 | -43.61922 | 2025-08-31 04:29:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ff67ade6-1f9d-3d5b-8de4-6532b099f74a | -11.01256 | -46.95903 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 04b19af9-8bb3-3449-b26d-89ffabea3e24 | -13.35876 | -46.94413 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 87a33370-c816-3b82-a371-9cd0dfb1a752 | -10.96023 | -50.862 | 2025-08-31 04:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4069bb4d-1cac-376f-ac4c-39a5c8efdc8e | -11.28962 | -43.57846 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d353005a-1279-39cd-a440-34cb053d32da | -12.99245 | -44.85476 | 2025-08-31 04:29:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b202af13-298a-3190-ac86-82c16d7b4470 | -11.31508 | -43.69178 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 45eb6107-6a70-3184-bf6d-2ae5a09cf742 | -12.62973 | -57.00798 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5270b28-ae77-30cc-9b95-8dcd683337ae | -11.07412 | -44.62058 | 2025-08-31 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| b4f20a94-fd33-356c-a3f6-5618234fa46e | -14.33917 | -51.87488 | 2025-08-31 04:29:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0cb01277-3f1f-3431-aaf2-f33a79599e54 | -10.41896 | -50.85997 | 2025-08-31 04:29:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9ab06bc1-f9fa-3437-9549-f0d2f23a1055 | -14.03934 | -44.55892 | 2025-08-31 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1e4d030-8961-389b-a116-0b88ae22706e | -14.03631 | -44.55403 | 2025-08-31 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aaa3b858-bc5b-355e-969f-fe5154566fd4 | -14.35764 | -51.90198 | 2025-08-31 04:29:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 509c20dc-2b3b-3c1e-832a-f9587d1b4c05 | -14.04491 | -44.54641 | 2025-08-31 04:29:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 13c3d4c6-3d77-31ac-9d9a-05b3cb8960d8 | -11.0858 | -52.0314 | 2025-08-31 04:29:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 235c4380-2e77-3804-bcc3-7010a0780346 | -13.46773 | -46.97219 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b18cddd0-4c99-3c77-b248-2a7578106bd0 | -12.63897 | -48.20127 | 2025-08-31 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 31637ae1-c409-3175-a083-1953f89659bc | -13.51793 | -46.98035 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 96f0cbf3-2276-3128-a2e2-eb26caf4f0c3 | -11.07833 | -52.05109 | 2025-08-31 04:29:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4337eba8-1db3-37e7-8b7f-f1d1e4c0334f | -11.82707 | -46.52575 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ac635e3a-2aae-36d5-9980-bf862ba4515d | -14.2275 | -48.065 | 2025-08-31 04:29:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33906c87-8123-329c-9132-2d65f72f25e5 | -13.32083 | -46.94535 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 33452ef3-798b-34a6-bf8f-4c40df5dc019 | -11.29538 | -43.67076 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f963b2e-da1d-3964-a736-2959cfd93edb | -13.39714 | -46.94993 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f4f49720-3c18-3300-a293-54ddab306822 | -10.94765 | -50.84607 | 2025-08-31 04:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 26b32e82-7cfa-3448-98b1-13e5da013899 | -10.09001 | -49.27842 | 2025-08-31 04:29:00 | NPP-375D | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b9be8178-a39f-33ff-a379-d00f346586a6 | -14.50132 | -52.98719 | 2025-08-31 04:29:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d21bd7bb-5780-3e80-b6a2-21c40cf5ce0e | -13.47217 | -46.96569 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef6a0b06-d1a9-359c-aa42-050d17e9308c | -11.85824 | -46.45725 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f85fe45b-2c24-30e4-b542-c6e982387441 | -11.55846 | -47.61408 | 2025-08-31 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d088bfd0-fb98-3e92-9168-e8a641194ec1 | -9.6943 | -47.03955 | 2025-08-31 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 569df7ab-27d2-3163-b155-63c2ecdb2979 | -11.88262 | -46.70978 | 2025-08-31 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e2778035-946a-3b33-ace4-c18932751cb4 | -13.48385 | -46.95666 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bb6ba14d-c7f4-38f5-a170-e4b8771dae91 | -11.89736 | -46.42656 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ef9c96f8-0335-37c4-bfac-ad10782c2a79 | -11.26907 | -44.92757 | 2025-08-31 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ba4f6d97-cce5-3735-adcf-ba81a6d53568 | -13.4928 | -46.96536 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 563c3316-36b9-3945-8ed7-5294f0851e6f | -13.4889 | -46.96838 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f270ad5b-d44f-34e7-b4c2-6f8e54c2c215 | -13.6857 | -46.88208 | 2025-08-31 04:29:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 804b2383-f753-392d-a8bc-543e138f26db | -12.85149 | -48.08269 | 2025-08-31 04:29:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cf880c1b-9df2-3913-948f-64602fbe6777 | -13.46129 | -46.97874 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a474dbf9-42d4-3082-b189-854c99d1c517 | -11.83798 | -46.78685 | 2025-08-31 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 684ed2d0-c6f8-3de6-8cd7-7086a654aef2 | -10.41523 | -50.85932 | 2025-08-31 04:29:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 93daa4ef-bbd6-3189-95f2-2f3ba6045ee1 | -11.36292 | -43.59876 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 76454348-c7b2-3b41-8745-5faf3522e76a | -11.86722 | -46.48806 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 93ce2f74-d88a-3493-846d-079bab568780 | -13.32359 | -46.88317 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9a8c7bd7-0b10-3025-945a-6775d47133bb | -11.0208 | -46.8629 | 2025-08-31 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 82ec7426-7d49-3200-9a25-3f784523ff32 | -14.37277 | -53.05313 | 2025-08-31 04:29:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e124972d-5ee4-3f15-98a6-f9a5a62f9155 | -8.96626 | -50.01117 | 2025-08-31 04:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd32bf99-c9b2-3766-8bc3-ca180c5fae9c | -11.81442 | -46.43952 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 2ff1a4b1-894f-36c5-9ba0-0106da633994 | -11.29838 | -43.57058 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 142d605c-5c18-353c-8724-1ae9020d4396 | -11.88266 | -46.73164 | 2025-08-31 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bc10403a-b952-3351-99a8-94354deecde8 | -10.03865 | -48.0905 | 2025-08-31 04:29:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 371e4d44-898b-30c1-a5c0-38dbfd563e03 | -11.80491 | -46.45649 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 80a84eb8-e03f-3da4-b3d4-4dd4c4c70521 | -13.68293 | -46.87782 | 2025-08-31 04:29:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 956263b1-8977-3f2b-a4b5-bc2fd415d114 | -13.03149 | -56.90729 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6180cc15-7a1f-32b8-8ad8-b1a67a43565d | -8.97066 | -50.02936 | 2025-08-31 04:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04fcd7ac-e7a7-3369-9b6e-aa74cd16601d | -12.92045 | -56.97704 | 2025-08-31 04:29:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8a43605d-0710-37c7-9895-e37c68d36adc | -12.39935 | -46.47535 | 2025-08-31 04:29:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8353498d-565c-3095-989f-638bc5363c6b | -8.95978 | -50.00756 | 2025-08-31 04:29:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 868482cd-d346-341e-8d7f-8aa9f4b2b47e | -13.30683 | -46.88047 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2930fb2b-d80d-3152-9879-912ddc2416fc | -10.60339 | -44.32801 | 2025-08-31 04:29:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c630d659-5e10-342d-9fdb-26dbc41a1e64 | -9.95631 | -46.34423 | 2025-08-31 04:29:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 27da59af-20d4-3860-bc8a-4360f041c3ba | -11.3078 | -43.6636 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 902693de-1a5f-3791-9c5c-1f45f29ad619 | -11.84132 | -46.78738 | 2025-08-31 04:29:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e3dd9fd2-7238-366f-ad5a-215a0137fad9 | -11.01089 | -46.94795 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d0bb1de4-b2e4-3c3c-9ea6-138af38e4d24 | -13.4956 | -46.96944 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 409da322-e3d5-3f37-abb1-0883ad15ad7c | -13.47887 | -46.96674 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 341bd542-4fc5-3483-a7d5-db9909fd07d9 | -11.56179 | -47.61463 | 2025-08-31 04:29:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 29b3f265-d589-32ef-9534-f0d3d24436ae | -11.82129 | -46.42936 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3d30c63f-cea8-31f6-b26f-f754cbdec204 | -11.90433 | -46.70221 | 2025-08-31 04:29:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cc6c0a6a-4a2b-3d04-90d2-c0c2f3523cc8 | -14.53725 | -51.98273 | 2025-08-31 04:29:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4f92f83e-f4bd-34d1-ac6a-092df2eef888 | -11.32397 | -43.65687 | 2025-08-31 04:29:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 31492da1-9071-3ed2-b7ef-64c8aae56a8e | -13.30464 | -46.91696 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e0bb2ba-b548-386c-8905-5be26357abd3 | -13.34698 | -46.86507 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 431c33c3-5713-3b95-8cae-193afe81b87f | -11.80827 | -46.457 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| e0a37304-d3a1-3a59-8d47-14550d001744 | -11.82648 | -46.50734 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ca05d281-39b7-3d82-928d-27603911686b | -10.96468 | -50.85821 | 2025-08-31 04:29:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e6c8652e-868a-3015-a3c7-98188ff308ad | -13.4911 | -46.95416 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1ba908f2-6285-3498-8ef1-8073acd030f0 | -11.00969 | -46.84669 | 2025-08-31 04:29:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c0acd7f-ff37-34f8-888a-0c25487e722e | -10.99869 | -46.93876 | 2025-08-31 04:29:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 28a10efd-31da-3120-afab-00ff66641bff | -13.47941 | -46.96323 | 2025-08-31 04:29:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| baae7e8a-accd-372b-8a67-a04788b33cc4 | -9.6871 | -47.04199 | 2025-08-31 04:29:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README44.md)
