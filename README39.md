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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3b49ede8-faeb-32bd-8197-a005a5f4098e | -2.26555 | -46.10262 | 2024-10-30 04:19:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 698ec24e-5fc7-386e-b705-8bf10450073e | -2.2618 | -46.30444 | 2024-10-30 04:19:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bfcdd168-d968-3f33-b48f-4fdc33bd9bc9 | -2.22783 | -46.69963 | 2024-10-30 04:19:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 45b22cbd-99d1-3580-83fa-29484ecaa330 | -2.19333 | -46.98698 | 2024-10-30 04:19:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5c98abda-1514-3e53-b76b-f6c25088895b | -3.29641 | -47.03016 | 2024-10-30 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 15430e3c-19e0-3baa-9741-ed9bcfd54676 | -3.22427 | -46.50222 | 2024-10-30 04:19:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3f10a335-7f03-3194-b4d7-6ce91870bd75 | -3.16726 | -46.61011 | 2024-10-30 04:19:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e9f9f7d-be00-3e5f-962b-8a68ad38d9f9 | -2.85908 | -46.65324 | 2024-10-30 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b44d8c8e-efd0-3bb5-bdb9-ab52e516cc4b | -2.72296 | -46.68644 | 2024-10-30 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aff86468-96ae-3977-bfcd-ad0d26c3bb2b | -3.93675 | -49.74836 | 2024-10-30 04:19:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fe47fb0a-accd-3570-9879-0dd337d8b1dc | -2.72035 | -46.70253 | 2024-10-30 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f1112308-8d47-355b-95c3-00fddd0b9560 | -2.7197 | -46.70655 | 2024-10-30 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d67a2db-323b-3dbf-a1cd-d6f8fe54e968 | -2.71941 | -46.68587 | 2024-10-30 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7127a51c-1bda-3a15-9747-81d41a9abc20 | -2.71745 | -46.69794 | 2024-10-30 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5bec59a3-5199-32a0-9c1b-eecd77742241 | -2.7168 | -46.70197 | 2024-10-30 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 594fef7e-86d8-34a5-bc26-ff367e80decb | -2.71633 | -46.68554 | 2024-10-30 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ab0a21ff-b687-39b8-967e-2bc9afc6e016 | -2.71615 | -46.706 | 2024-10-30 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f7c3de5-9292-39b7-884f-53ef400b95ce | -2.71585 | -46.68532 | 2024-10-30 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a2df335a-b18f-3c6c-afee-f344f89d105f | -2.7157 | -46.68957 | 2024-10-30 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4dc1fc04-e5c6-34e9-b45c-29d7c5c287dc | -2.7152 | -46.68934 | 2024-10-30 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7386d5ad-0f21-35ca-944a-96af1ebed29e | -2.71507 | -46.6936 | 2024-10-30 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 674b8076-abc5-3c04-b284-0daeb9ebe252 | -2.71455 | -46.69336 | 2024-10-30 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 35d5a9a8-6855-3494-8efb-20557edae101 | -2.71444 | -46.69762 | 2024-10-30 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 72f543d8-d1ae-36c8-be30-8e7d93379f29 | -2.7139 | -46.69738 | 2024-10-30 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 94534e74-da58-30c9-8fdf-42c91c38ecba | -2.71381 | -46.70166 | 2024-10-30 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 67e98cbc-f005-3df6-9d9a-b85a5c628e59 | -2.71324 | -46.70141 | 2024-10-30 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69a7b3bf-39c3-36ee-9e7d-e174526b7c74 | -2.71317 | -46.7057 | 2024-10-30 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9d118fc2-2539-35f2-92f9-13805c5b8195 | -2.71259 | -46.70544 | 2024-10-30 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fa451b55-7e3f-39e6-bb73-9b45f218ae9b | -2.68025 | -46.72946 | 2024-10-30 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8f2f80a1-ce8c-35ea-8c28-6b4e9cc4f336 | -2.67962 | -46.73348 | 2024-10-30 04:19:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 06016305-a1a4-3f31-af79-7100b8349e17 | -4.42929 | -46.43483 | 2024-10-30 04:19:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f5edd7d4-e2a5-3339-99d1-345ebd1ad6bb | -4.36584 | -47.4787 | 2024-10-30 04:19:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9fe3c24b-d0bf-3385-aa55-e2fd15c69451 | -4.34536 | -46.3672 | 2024-10-30 04:19:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4788058-6079-3c1b-87d4-c94d7e459765 | -4.23733 | -46.86099 | 2024-10-30 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e9ea5a63-268f-39be-bf4d-6f2417c05f44 | -4.19887 | -46.71455 | 2024-10-30 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 49bbc718-a70b-3e0a-93bb-4ed8c3b0828d | -4.19537 | -46.71398 | 2024-10-30 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1dda0951-11b7-32a0-9df7-74964c813159 | -4.19186 | -46.71349 | 2024-10-30 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 492c6729-c1ea-3054-bb49-f4d6b4f836c0 | -4.15349 | -46.84046 | 2024-10-30 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 80e85a73-b25e-3c37-bcf2-bb9af311a550 | -3.95955 | -46.40452 | 2024-10-30 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cbe54150-6568-3f5b-b265-2e3cbcf12d70 | -3.95895 | -46.40821 | 2024-10-30 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fd7515e8-bde1-3c5a-a4d1-d53140b9b43f | -3.95656 | -46.40851 | 2024-10-30 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3008d6f0-7869-3ec0-addb-52db73b44748 | -3.95549 | -46.40765 | 2024-10-30 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d8569fe1-f08e-3102-bd36-085173f7271f | -3.87331 | -46.6407 | 2024-10-30 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b75f914b-a01a-3196-8961-93a887820ac8 | -3.82927 | -46.93898 | 2024-10-30 04:19:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b2604806-54e3-3126-884a-9151a532cc4c | -5.08672 | -46.86291 | 2024-10-30 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1433ba91-7905-33db-b6b4-f8f67723f7b2 | -5.03741 | -46.93916 | 2024-10-30 04:19:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9307c646-5144-3415-9732-e75dc9b35c35 | -5.03389 | -46.93864 | 2024-10-30 04:19:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15d9ef76-ad6f-3856-ae9c-d92c38bd4528 | -5.03326 | -46.9426 | 2024-10-30 04:19:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf4b4337-7789-30ac-864b-4ea4cce6453b | -5.00699 | -46.46967 | 2024-10-30 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4c51e802-35c0-3412-b059-faa2d0a170f9 | -5.00112 | -46.48439 | 2024-10-30 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 95c0ea91-2095-3b20-a188-0f2f6a81e5ab | -4.98915 | -46.47089 | 2024-10-30 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0818e835-799a-3a76-b865-2d5a0c0228e0 | -4.96021 | -46.49718 | 2024-10-30 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 08e76071-ca21-3256-9d1b-02e2368a57d4 | -4.85194 | -46.89514 | 2024-10-30 04:19:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d1c1d2e-c4df-39d7-bead-eea607f51b3c | -4.84805 | -46.87437 | 2024-10-30 04:19:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ed3ebc69-d2ba-3545-a69b-0efc90461fe6 | -4.84455 | -46.87377 | 2024-10-30 04:19:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2b9bdb5a-25fe-3ac3-932b-94b57df4c3f9 | -4.73781 | -46.65845 | 2024-10-30 04:19:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| afd755e5-3d83-3ac9-8deb-4cc2732a5980 | -4.6416 | -47.09889 | 2024-10-30 04:19:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97e4a058-a8fc-334f-af05-5d85895df15a | -4.62337 | -46.53843 | 2024-10-30 04:19:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 895285dc-e1ab-3a4f-b237-9a8ed69b9781 | -4.62137 | -46.50688 | 2024-10-30 04:19:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ca00b1b5-5f12-33c6-b976-215296b940c8 | -4.58948 | -46.5722 | 2024-10-30 04:19:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6d64a4d0-b7ef-3c03-9f3d-5c31f71be9fd | -4.49908 | -46.45726 | 2024-10-30 04:19:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 9.7 |
| ac7722bb-cbf6-3309-84f8-ed360df7c8e4 | -4.49562 | -46.45675 | 2024-10-30 04:19:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6b52769e-8f6c-3624-a6aa-f4c7977c15cb | -4.44922 | -46.46532 | 2024-10-30 04:19:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 12a99446-4f0f-3a5d-b928-b91e619f3ba2 | -4.42767 | -46.42289 | 2024-10-30 04:19:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76e5bb68-da90-370b-897c-5a13dcc0872c | -4.42299 | -46.42996 | 2024-10-30 04:19:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 802a61ba-7571-3b18-8267-226632342494 | -4.41954 | -46.4294 | 2024-10-30 04:19:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6e33d627-9898-3d27-8c7e-46969c8c69b8 | -4.35213 | -47.31315 | 2024-10-30 04:19:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb6b7996-6047-30a2-946b-42891cc646dd | -4.23798 | -46.85698 | 2024-10-30 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5590b3a3-84e5-3c69-9f32-4c273332dbdc | -4.23316 | -46.86442 | 2024-10-30 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 217857f5-cab6-3e64-afda-f3845db0b09e | -4.19825 | -46.71844 | 2024-10-30 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4420cdf1-c22c-3b25-8158-2ab5e1aade24 | -4.19474 | -46.7179 | 2024-10-30 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6185b338-0b81-3589-ba3e-f1de863057e0 | -4.19249 | -46.70956 | 2024-10-30 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c5f77b07-dfda-33e9-a595-fede961d91a9 | -4.15284 | -46.84451 | 2024-10-30 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4b57966e-af66-3eb7-a96b-4903020197d2 | -4.14931 | -46.84397 | 2024-10-30 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb3d08ec-48a0-32b4-af60-9cb3566c2a9a | -3.96968 | -47.10096 | 2024-10-30 04:19:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c54579b-fb3f-36ce-8199-6360bb71c5bb | -3.95489 | -46.41135 | 2024-10-30 04:19:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 09ea7220-bd31-3b9c-86d8-17e8ded84cf1 | -3.78566 | -47.11977 | 2024-10-30 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 161c7cd6-7394-3310-b941-9cc474ed07cc | -3.61904 | -47.29471 | 2024-10-30 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f4a7409a-0789-34dc-bb24-e58531a848ce | -3.61497 | -47.25123 | 2024-10-30 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8a3548dc-878e-323c-81ae-0858acbbe303 | -3.61204 | -47.24648 | 2024-10-30 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce2e315a-d9d0-306c-86e4-ceed0385a2df | -3.61767 | -47.30315 | 2024-10-30 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bc262635-b56f-3517-aefa-dfd2dddd28af | -3.59954 | -47.30025 | 2024-10-30 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5397dbe2-eb70-376c-a4d0-b8fc723ee2ea | -3.59848 | -47.30067 | 2024-10-30 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 24bf1e56-da92-3c98-8238-e98aa2a3ba29 | -3.59592 | -47.29964 | 2024-10-30 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 54f1725e-bf45-342e-b6d2-66632c1c6441 | -3.58894 | -47.29044 | 2024-10-30 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a56f6e2-6275-3bd3-bfb3-7492ef741da7 | -3.57557 | -47.37497 | 2024-10-30 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2b1c98ee-8857-3b1c-b68e-5751e5117033 | -3.5749 | -47.37923 | 2024-10-30 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b44ec970-036e-3cf2-b4ce-2ad21263cd44 | -3.57423 | -47.38348 | 2024-10-30 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8f9773b6-63b5-399d-8a13-55a4d46e18c6 | -3.57193 | -47.37439 | 2024-10-30 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 92cad1d5-1919-3751-b783-8a65a8eae2c0 | -3.57126 | -47.37864 | 2024-10-30 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 7c182444-30c7-3d63-beb1-e6a2e0d754d9 | -3.57058 | -47.3829 | 2024-10-30 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| c6d1bc8b-8130-325d-968b-e623ecc1d962 | -3.56828 | -47.37382 | 2024-10-30 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 26a2ddf4-d8ca-39cc-af3c-7b57d6e1461e | -3.56761 | -47.37807 | 2024-10-30 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 7affdd90-cb9a-3521-b53d-085c9d53b28e | -3.56694 | -47.38233 | 2024-10-30 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| 99a3fa7c-234d-3e51-8587-01e26b88f0dd | -3.56626 | -47.38659 | 2024-10-30 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7c2af0de-2cf5-38eb-9f23-73fef112945b | -3.56396 | -47.37751 | 2024-10-30 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 981091b1-1ce9-34c2-8334-216e0248eedf | -3.56329 | -47.38176 | 2024-10-30 04:19:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b656778-61af-3a2b-976f-3710addf2d53 | -6.50913 | -47.04416 | 2024-10-30 04:19:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0eea1d95-54f3-3ed7-a158-45a1b6b1cfd4 | -6.20961 | -46.87574 | 2024-10-30 04:19:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 93f46e46-2334-3e8e-b097-1850bf98eb4c | -6.16818 | -46.95557 | 2024-10-30 04:19:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README40.md)
