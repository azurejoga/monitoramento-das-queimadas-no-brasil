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
| 6f69d236-dd13-32eb-8537-901bd1fd1140 | 0.93557 | -60.31923 | 2025-03-03 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6a93548f-5f21-3077-9b46-29928a8282ae | 2.02123 | -61.43305 | 2025-03-03 05:33:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 501fa814-e937-3ef9-bde2-6abd525db365 | 1.10095 | -59.69174 | 2025-03-03 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 96d23782-9b3a-39d8-bece-f88f30b39f1e | 1.14376 | -59.5553 | 2025-03-03 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9b015c39-03f3-338e-8825-23a1b396ea1c | 0.70978 | -60.0178 | 2025-03-03 05:33:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f8a9f4ec-6311-3bb1-a5cd-b0c3efec9daf | 0.97094 | -60.52502 | 2025-03-03 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8cd273c1-18ff-38b2-a3cd-768c0c53d0ef | 3.22418 | -60.25322 | 2025-03-03 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fbaec207-f941-3989-b5cd-36ae4516b148 | 1.13389 | -60.07881 | 2025-03-03 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ab003bbb-d730-3132-a36f-6d4fa7a25642 | 1.87282 | -60.3789 | 2025-03-03 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 227fb655-aab7-34b3-bd6d-7ff8b83ecc29 | 2.11305 | -61.82581 | 2025-03-03 05:33:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 12fcb120-3746-305e-8edd-80170c2a89db | 1.73517 | -60.53916 | 2025-03-03 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1e4d02ec-c4c1-3a45-908d-66cc98d4bc22 | 2.22475 | -61.34163 | 2025-03-03 05:33:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cb122fc5-3308-3037-a3e1-515cfee8ca14 | 2.10815 | -61.81606 | 2025-03-03 05:33:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71115773-4ae0-34fd-a9cf-83cfdff59d1e | 1.89689 | -60.57584 | 2025-03-03 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be34e4bc-fb09-3343-a172-ea15bbe623cb | 0.95694 | -60.2267 | 2025-03-03 05:33:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e398b7d6-a0fd-37e3-ba96-60537e0ba4ee | 1.77088 | -60.22515 | 2025-03-03 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 252956a0-f110-34c6-a931-5f27130ff340 | 1.84747 | -60.30559 | 2025-03-03 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f923aa6c-e9f9-3b2b-b3c0-a59fab88e8c9 | 2.10868 | -61.81948 | 2025-03-03 05:33:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bfd85533-3405-39c3-a297-21f30e4d6fe0 | 2.33944 | -60.51085 | 2025-03-03 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7472d3a-d8c3-3a30-8442-a98c7f917218 | 3.20253 | -60.52375 | 2025-03-03 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15b56de5-ec6a-33a4-9cc4-ad3315ac4908 | 0.92257 | -60.36967 | 2025-03-03 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d001fed8-4656-33d8-844b-9ca88101e39d | 0.99757 | -59.43001 | 2025-03-03 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| de830404-3995-3146-9dbe-23b2791b9aa4 | 1.90024 | -60.57532 | 2025-03-03 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b39a61f8-466c-3a7f-b3ad-d4d408ebbdf5 | 0.01805 | -60.66413 | 2025-03-03 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2da23411-4ce4-30b2-a082-4d7ff2ebb578 | 0.95752 | -60.23036 | 2025-03-03 05:33:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b24258d8-11de-3246-9a13-b787d530ff7b | 0.29259 | -60.5848 | 2025-03-03 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3934b3e-66c3-35b1-afb6-37079fe973bb | 0.65773 | -60.57715 | 2025-03-03 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2d0fe1fd-2028-3d53-81dc-43cca8bf1378 | 3.78945 | -59.77176 | 2025-03-03 05:33:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f607810d-7344-380e-a4a5-bbcc8ca7cd5a | 0.92087 | -60.33642 | 2025-03-03 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9901195-87e0-3081-93b3-c27103b05026 | 0.97017 | -59.77811 | 2025-03-03 05:33:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3a5d192a-b77d-3dd5-8030-33f2c9b92cb1 | 2.251 | -60.2987 | 2025-03-03 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 090fb759-07e4-34d3-8a24-3e5274f2b140 | 3.70629 | -60.76245 | 2025-03-03 05:33:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e5bb6330-ed7d-3aab-9c56-e63415d890a3 | 1.7923 | -60.27367 | 2025-03-03 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8c701a4c-d68b-31be-9f79-9066c9586c8b | 1.57285 | -60.19562 | 2025-03-03 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 164d1973-6af1-383d-81c3-75f95549807e | 1.7675 | -60.22569 | 2025-03-03 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 21b741b4-efb5-3697-ab98-006266bc5bc8 | 1.90531 | -60.4544 | 2025-03-03 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| adb33749-b9c7-3736-8f07-eb75e3397992 | 0.96149 | -60.23351 | 2025-03-03 05:33:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6539e950-4ad1-3cd2-b1bf-58a61919f400 | 3.69419 | -60.96589 | 2025-03-03 05:33:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1de81851-dacc-31c9-aa27-3fb87b75fe3b | 1.89301 | -60.39777 | 2025-03-03 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cca0b4e7-f7dc-322b-a178-3022ff1cb19f | 4.22948 | -59.84431 | 2025-03-03 05:33:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a75c5555-098a-3c44-bc58-a758424dbabd | 2.01356 | -61.42719 | 2025-03-03 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| cf3976d7-ab24-345d-88e0-d0d5d5e856c2 | 2.11144 | -61.81556 | 2025-03-03 05:33:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fa381abf-e0fe-3ea3-9f9b-01c64f20aefa | 4.23285 | -59.84383 | 2025-03-03 05:33:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75e8c080-6690-3c76-9bff-b83aa174148c | 2.45269 | -61.31974 | 2025-03-03 05:33:00 | NOAA-21 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 42a38307-4401-37df-8157-a07028ecad61 | 3.52855 | -60.51925 | 2025-03-03 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 884dbc6e-9ac3-377b-886a-ee3ae642a125 | 1.88745 | -60.8623 | 2025-03-03 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76793dac-ffbd-346c-b4e1-f624e449d4aa | 2.39224 | -59.99928 | 2025-03-03 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6964c4a2-a511-387f-988b-9e683f0fba01 | 2.39563 | -59.99875 | 2025-03-03 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e1c8edd-1594-31bf-9e90-1a23483719c5 | 3.69749 | -60.96538 | 2025-03-03 05:33:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8adada37-de5e-3d59-8449-12b62abd0102 | 1.93595 | -60.39503 | 2025-03-03 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| fe0431c9-f8ac-3a1b-81f3-918424cdf7e3 | 1.89089 | -60.81875 | 2025-03-03 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3f46f26-9cdb-3792-93ba-c5e77f760194 | 2.57857 | -60.62497 | 2025-03-03 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a4f342b1-9f6c-3f5d-93e2-9ae05e8dcdd5 | 1.57624 | -60.19509 | 2025-03-03 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24ff8025-4183-3a31-a09f-50d1f792d028 | 0.91293 | -59.35015 | 2025-03-03 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7459aa48-e8f1-3c7a-8c67-f4191d704356 | 2.40184 | -59.99404 | 2025-03-03 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ed4799e-1496-374d-9d6e-5c86c0c08293 | 2.01632 | -61.42324 | 2025-03-03 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 08b6c87b-613e-3d5f-a6d5-69153a3aa1d1 | 2.17201 | -61.83054 | 2025-03-03 05:33:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 656997bd-9821-3cdc-82e2-b3b84f6bff00 | 1.03936 | -60.05936 | 2025-03-03 05:33:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a3cd61d8-4447-3675-aeef-9aaff54e01b6 | 1.10821 | -59.34863 | 2025-03-03 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9663a495-eb49-3516-be48-c3b0267cc176 | 1.12679 | -60.37223 | 2025-03-03 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b62dcf05-f14a-34ee-8ad5-d59af8b636da | 1.31418 | -60.06641 | 2025-03-03 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a1bae16-db52-3842-bf8a-8d8416ac9ade | 1.87562 | -60.3748 | 2025-03-03 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b842af07-5bcc-3266-adfa-b79735d61c7e | 0.96757 | -60.52555 | 2025-03-03 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3aa58a3b-5375-3466-8866-c2d456c3899a | 3.2053 | -60.51973 | 2025-03-03 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 17fb660a-dec2-3679-ac19-9d2aee335ef5 | 0.02538 | -60.6667 | 2025-03-03 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1caf6203-a6a6-38cf-8b60-c87f1b908d31 | 1.58493 | -60.19793 | 2025-03-03 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c2026daf-85c2-30fb-baf6-90fa655bcc83 | 0.83442 | -60.50228 | 2025-03-03 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dca6f505-9f52-3709-83dd-8a6ef8e98ad0 | 0.96082 | -60.5266 | 2025-03-03 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5bfec482-aa46-3bd1-aed6-833cb6e33ced | 1.92853 | -60.7119 | 2025-03-03 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad630957-9d8d-322d-9949-5b8c72b5d2df | 0.29033 | -60.59256 | 2025-03-03 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 39f6cd03-7178-3757-b843-e8801098358d | 1.94212 | -60.39048 | 2025-03-03 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f415497f-9353-3877-bbc7-b26cd47a081a | 0.02876 | -60.66618 | 2025-03-03 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9598bb2f-198c-3aac-9c4e-3468ad723d96 | 1.93933 | -60.39458 | 2025-03-03 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| dda0702e-5b6e-3d7c-bb85-8775a9080635 | 1.58096 | -60.19485 | 2025-03-03 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c4f720df-558c-39e7-9eb5-e42b90794286 | 2.01686 | -61.42668 | 2025-03-03 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 97919da4-6555-3483-925c-13471c3ca10a | 0.96813 | -60.52914 | 2025-03-03 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| abb81c63-b9ae-3678-9e2b-2bc2379bd923 | 2.38501 | -60.5833 | 2025-03-03 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 959872b9-8586-3134-b60b-67ea77f1ea7a | 1.03356 | -59.46903 | 2025-03-03 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da731bce-0fba-31ae-883f-887735ccc525 | 1.79905 | -60.27261 | 2025-03-03 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6e1a0971-0de8-3a91-bb7f-2b7375e7fb94 | 1.02788 | -60.41325 | 2025-03-03 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f5146e45-421c-382b-a9cf-b56851af7bb2 | 0.83386 | -60.49867 | 2025-03-03 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e7d69d73-c047-3564-a035-7d5b0a6eb7c5 | 0.96475 | -60.52967 | 2025-03-03 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd92fdf0-e11d-3f4c-a029-aa118a6a2bbb | 3.22091 | -60.46697 | 2025-03-03 05:33:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 63356083-9d8b-3953-9c98-dc5ac7bd7c7a | 0.87696 | -59.58345 | 2025-03-03 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2d668c48-ac02-397f-9c3b-7e93f8b9668f | 0.76207 | -59.81654 | 2025-03-03 05:33:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 924d3861-9628-3d88-935d-e32ea18abaa9 | 1.79624 | -60.27675 | 2025-03-03 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bbc5a6f6-9e5b-36b0-af02-3e0baf5b3d2c | 0.75443 | -60.235 | 2025-03-03 05:33:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 645d558f-b4a9-3da1-9e4d-63a9beb79c24 | 1.03621 | -59.56372 | 2025-03-03 05:33:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e9e94be-f54d-39d4-946a-af0c64688e2b | 0.87206 | -60.24673 | 2025-03-03 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 21a35678-f427-32b3-8ebb-c7bba72c94c6 | 1.90587 | -60.45795 | 2025-03-03 05:33:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6868560f-ca9b-39fd-9142-04c1c7194599 | 2.39845 | -59.99457 | 2025-03-03 05:33:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2d9ce98b-66a1-3fdc-8c28-45076c0608cf | 0.78195 | -60.41037 | 2025-03-03 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9bb5c9f7-d1c2-31ed-8140-9d721a9d5695 | 2.1933 | -61.8588 | 2025-03-03 05:33:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6a6253c2-1dc2-37af-a5b6-a10d7035a179 | 0.29315 | -60.58842 | 2025-03-03 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5cf460ec-c2e9-3747-aea7-0095adcc23d5 | 1.12321 | -59.98925 | 2025-03-03 05:33:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0a6a974-b1cb-3a43-bea7-1f42f3751ef3 | 1.88636 | -60.8553 | 2025-03-03 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b81678ab-255a-3d48-a74b-4fc1a3857271 | 0.02143 | -60.66362 | 2025-03-03 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 538dc0b4-98f6-3445-9623-9a0775032f74 | 0.76338 | -60.44664 | 2025-03-03 05:33:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83302aee-dd8b-3b9c-9e6c-e36b956dda84 | 1.76694 | -60.22206 | 2025-03-03 05:33:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1ecd20f4-370e-3afe-ac01-0c0ae9b7f06a | 0.82896 | -59.94929 | 2025-03-03 05:33:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README6.md)
