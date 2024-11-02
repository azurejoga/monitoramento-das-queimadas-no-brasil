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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 356661d9-474c-301d-9fdd-f2da74c1c316 | -4.05301 | -46.9402 | 2024-11-02 04:12:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 815d795f-b7f0-3314-82d2-6e11b95be0ce | -4.97547 | -46.47054 | 2024-11-02 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94209ab0-7f62-368a-8a83-dacb5d458bd5 | -4.97477 | -46.47488 | 2024-11-02 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6189ba18-fdb3-3841-ba82-547eba896efd | -4.97176 | -46.46999 | 2024-11-02 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d6f358f-a1fa-3896-8c4b-9033331d61b7 | -4.96595 | -46.48241 | 2024-11-02 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46a5ffaf-4bb7-3ef4-aeab-0a5de3adecdd | -4.96308 | -46.50015 | 2024-11-02 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c2974b68-7e87-3457-9ef2-0fd0ceb2ffd5 | -4.96236 | -46.50463 | 2024-11-02 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 63a95d17-b020-3e69-afa8-f7476f6f1bee | -4.96224 | -46.48181 | 2024-11-02 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c32b4e5f-70f6-3acf-9fe3-6330649cd04d | -4.96155 | -46.4861 | 2024-11-02 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3ceb928-c50c-33b4-affc-a981f434b94c | -4.95865 | -46.50406 | 2024-11-02 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 18c0745a-468b-3f7c-9b46-f95c0d0b044d | -4.95784 | -46.48553 | 2024-11-02 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 154c46a4-f020-3d71-9d8e-1a84a9571865 | -4.88008 | -46.70344 | 2024-11-02 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 534da2f8-f7dd-3c28-a525-9a68ab8e2c1e | -4.79351 | -47.13151 | 2024-11-02 04:12:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c3035bec-f4d6-3e98-95a8-afe2759e90a5 | -4.79165 | -47.13398 | 2024-11-02 04:12:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 711c1879-6838-3ea9-b2e3-e597ef279042 | -4.77563 | -46.40991 | 2024-11-02 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd5eda38-8792-3966-b748-ba4b4e407b82 | -4.77492 | -46.41434 | 2024-11-02 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fdfa4162-61a9-36ae-85e1-091ac4b87e16 | -4.77192 | -46.40939 | 2024-11-02 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8df3d206-f20b-31fe-b953-702a84188632 | -4.71246 | -47.20579 | 2024-11-02 04:12:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64c569d4-678b-39d6-b59c-c088b13ad84e | -4.7032 | -46.43448 | 2024-11-02 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cd1a0a9b-8b4e-3f21-ab35-c6365a58d70e | -4.70246 | -46.43894 | 2024-11-02 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8475d402-f950-386b-a4c7-5bc3e5499177 | -4.69948 | -46.4339 | 2024-11-02 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 11fbd90c-5966-3959-a8ae-9a79e4883571 | -4.69875 | -46.43837 | 2024-11-02 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 422e4135-99ff-37a4-8974-8bb8c202f747 | -4.69577 | -46.43331 | 2024-11-02 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a3951b82-e3d6-3ad3-aa09-370720917670 | -4.69503 | -46.43779 | 2024-11-02 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 95649272-9a9d-3c94-9432-c9847f83dd90 | -4.6783 | -46.38762 | 2024-11-02 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 090207d4-6ae2-3775-8034-34f39f38d746 | -4.67529 | -46.38271 | 2024-11-02 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e5b1f4bc-4a17-31ee-9fd3-6b9d6b61b886 | -4.67459 | -46.38708 | 2024-11-02 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| f094e505-df78-3d4a-8a81-98bd7e46061d | -4.66227 | -46.32218 | 2024-11-02 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3bbf9913-838c-3a74-a58b-e454d2e2d3e1 | -4.6593 | -46.31715 | 2024-11-02 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f361cd5-35fe-3e10-8dc5-1d8f6b36e06a | -4.65859 | -46.32159 | 2024-11-02 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b51f9afd-e675-3b2a-a265-c2e4c157aa54 | -4.65656 | -46.60099 | 2024-11-02 04:12:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 10a5ceb2-1491-3655-9321-e113d0e510fc | -4.65604 | -46.38438 | 2024-11-02 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea9a57f4-b0d3-3574-b0c2-73f54cc8fdb7 | -4.65601 | -46.59916 | 2024-11-02 04:12:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 3ef60692-5029-3650-af37-e0a9527ef4e3 | -4.65579 | -46.60561 | 2024-11-02 04:12:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0921647f-2604-3c0a-b95c-7ac83be56140 | -4.65561 | -46.31656 | 2024-11-02 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2bbfb912-74ef-3287-a799-f5cbda6d3d4d | -4.65527 | -46.60379 | 2024-11-02 04:12:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| fffae4a6-32aa-3894-8c79-fd9ad9b9fe79 | -4.6549 | -46.321 | 2024-11-02 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 117ca3fc-4b49-3f13-8bcf-1222cc7cda99 | -4.65281 | -46.60038 | 2024-11-02 04:12:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 49cc5797-8519-35df-b2ab-117a8828054b | -4.65204 | -46.605 | 2024-11-02 04:12:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2fe6b0a4-cd8a-317a-9398-98791bb37b1f | -4.65152 | -46.60318 | 2024-11-02 04:12:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 00450e30-862d-3bf4-8554-4e17a833fa63 | -4.62894 | -46.29449 | 2024-11-02 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 921df8b1-4a92-332a-9bb4-6812351e35f3 | -4.58691 | -46.55128 | 2024-11-02 04:12:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e686b9a-02f1-306f-a327-de3e9c96d687 | -4.51931 | -46.48708 | 2024-11-02 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| fabb59a0-f761-39c8-ab41-ffd585d701c1 | -4.51858 | -46.49162 | 2024-11-02 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| acb98cd0-1cb3-39f2-b52b-855c8c58a02d | -4.50428 | -46.62754 | 2024-11-02 04:12:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 300f9ff2-a254-3139-a4a1-1e6d25559491 | -4.5005 | -46.62703 | 2024-11-02 04:12:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17578e96-1ed0-39e5-b31a-a11cd8ab4248 | -4.3033 | -46.90764 | 2024-11-02 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 468014a6-c887-3e93-9df1-57159fc83b23 | -4.25765 | -46.85864 | 2024-11-02 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 14307f56-cf1a-3fee-86c4-3e472e8dbf90 | -4.25687 | -46.86346 | 2024-11-02 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a105f8fe-0788-32e5-9add-1e5c12246690 | -4.2558 | -46.38553 | 2024-11-02 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dcdcf0f9-54fb-3bde-9bdf-e1af7f09637c | -4.2551 | -46.38995 | 2024-11-02 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7832b356-a796-3554-b278-83c819401654 | -4.25398 | -46.38326 | 2024-11-02 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 853e49fe-977c-3c67-bbef-7c1f83618f4b | -4.25325 | -46.38766 | 2024-11-02 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 97b40056-4147-3be6-8ea2-ee3c562f4646 | -4.25305 | -46.8628 | 2024-11-02 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1dbedcb8-6620-37c9-9603-48f2787f6bdb | -4.25207 | -46.385 | 2024-11-02 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 478af41d-6c9a-314c-bed0-8e64801dd4c7 | -4.25137 | -46.38944 | 2024-11-02 04:12:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c794dd64-4e97-3f0d-bcbe-a0d92b16c1df | -4.2038 | -46.71298 | 2024-11-02 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 033c1ce5-44c4-3a9c-b253-9b11d477002e | -4.20364 | -46.71053 | 2024-11-02 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2de2b39d-419f-3689-bb4c-25a4307638e7 | -4.19916 | -46.6932 | 2024-11-02 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82a8290e-5db3-3c47-ac03-93b6fa6445f9 | -4.19697 | -46.70696 | 2024-11-02 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8bf07472-ae24-318a-921c-24853a15c078 | -4.19317 | -46.70636 | 2024-11-02 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29d784c9-8abf-325a-a978-e11ac0a41ec4 | -4.19127 | -46.80877 | 2024-11-02 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0797b155-7fba-3ca4-98cc-1b41c25df65c | -4.18824 | -46.80342 | 2024-11-02 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0ce08c71-105d-3d3f-b790-91823ad4a56a | -4.16631 | -46.584 | 2024-11-02 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f51243b1-de81-36f6-a5c4-62c45223adc0 | -4.1201 | -46.89253 | 2024-11-02 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b76c347a-4c56-3028-b330-18c48c2b3e2a | -4.10986 | -46.59632 | 2024-11-02 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 18820c0b-e2a2-350d-af54-f6bfbd51a899 | -4.10722 | -47.11934 | 2024-11-02 04:12:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b355d868-6a5c-35a9-8080-d59a0f77d81b | -4.10609 | -46.59567 | 2024-11-02 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ccce0280-d5c1-3bfc-abca-c06b08452ea1 | -4.05538 | -46.93885 | 2024-11-02 04:12:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bca61f50-39b2-3f99-bfb3-d4ec525de3e2 | -4.05152 | -46.93821 | 2024-11-02 04:12:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 36f16c98-dc46-38a1-bb03-ba24f6abe1cc | -3.96008 | -46.3745 | 2024-11-02 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1914a8c5-3541-344d-b4b5-7e2b4b69b416 | -3.88851 | -47.0803 | 2024-11-02 04:12:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 06597a72-cd4b-33a2-a9f7-72d20920190b | -3.88207 | -46.44587 | 2024-11-02 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f72783cf-7e5a-3b3b-bc5e-3a04ff2af14a | -3.87454 | -46.4448 | 2024-11-02 04:12:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 93adc84e-5ce1-3bda-aed8-01182c2b34c3 | -5.50609 | -47.16941 | 2024-11-02 04:12:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fdcd5ea4-860a-3d78-9d89-2f06e5ef48b4 | -5.50227 | -47.16876 | 2024-11-02 04:12:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd06174a-8363-3d04-a393-959683395f21 | -5.40088 | -47.14923 | 2024-11-02 04:12:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1569c99-6a38-3c9d-a612-f951c95325d1 | -5.35532 | -47.35544 | 2024-11-02 04:12:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 64eab3c8-1823-30f7-8fde-25d5c52918f7 | -5.35144 | -47.35478 | 2024-11-02 04:12:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2c2e6565-9db0-3e5a-88c7-cc549c9e9c72 | -5.34837 | -47.34919 | 2024-11-02 04:12:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d126c136-8ad8-3734-bc30-81e1c6431eed | -5.34756 | -47.35413 | 2024-11-02 04:12:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f5da41e-422e-3737-9a02-40fa0ae16f75 | -5.29218 | -47.37506 | 2024-11-02 04:12:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Cerrado | 12.9 |
| a3824eaf-debd-3efa-98aa-41029c79a4fa | -5.29135 | -47.38 | 2024-11-02 04:12:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a1a23d2c-0c41-310c-a9d6-ef3854ebcd61 | -5.29102 | -47.37742 | 2024-11-02 04:12:00 | NOAA-20 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 1fab7621-1d14-363a-a8d0-7e0bc4a7c3fa | -5.21499 | -47.45057 | 2024-11-02 04:12:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aa7e702e-fb9b-30e6-99c2-171ac2859a5e | -5.15276 | -47.70366 | 2024-11-02 04:12:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a6393ef-703e-3f68-814b-fc7d2a5cf65c | -5.14706 | -47.7133 | 2024-11-02 04:12:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7ab4dcc9-e639-38e0-8446-0d607f383076 | -5.14648 | -47.71676 | 2024-11-02 04:12:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8a1db7b8-70ac-37b5-8516-68398f35862b | -5.14538 | -47.69888 | 2024-11-02 04:12:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 761545ac-33a3-30c4-8ca0-4edb6fcd09a0 | -5.14482 | -47.70223 | 2024-11-02 04:12:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10c8f60d-9ec6-3d78-8f57-ee12b33da142 | -5.06493 | -47.72732 | 2024-11-02 04:12:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8904a38a-3835-3e99-9e63-e357087d8a83 | -5.06095 | -47.72658 | 2024-11-02 04:12:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 54c040ea-56ea-33a0-9eca-63582ac4a8ae | -6.13045 | -46.69424 | 2024-11-02 04:12:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dca9741c-c36e-3fc9-8d8c-110480de4132 | -6.12604 | -46.698 | 2024-11-02 04:12:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 49d39678-04f1-38b5-b95b-65c8ca3f8ad1 | -5.5357 | -46.79843 | 2024-11-02 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 20fdd563-16f6-38cb-b520-26ada52568d1 | -5.53496 | -46.80294 | 2024-11-02 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c18576c2-9df3-30cf-987a-fb6df7dddd44 | -5.51249 | -46.82244 | 2024-11-02 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b0e73295-7fd8-3410-8a00-a9d1619ce598 | -5.48689 | -46.86042 | 2024-11-02 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bca38e7d-9c58-3f4c-8a49-e5b3bd23f528 | -5.48687 | -46.85804 | 2024-11-02 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1c031de5-eca3-3190-a03c-632a06c2b33e | -5.48313 | -46.85979 | 2024-11-02 04:12:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README42.md)
