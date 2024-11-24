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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 20165f1a-360e-3869-8c22-6ebbb3c38dfa | -1.5312 | -54.1957 | 2024-11-24 00:00:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| d107154b-fb86-3619-ad06-efbdf9489613 | -0.8724 | -52.7483 | 2024-11-24 00:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| b9e4003f-ac6b-32a9-bbf7-55b94dc56e6d | -4.2419 | -48.7193 | 2024-11-24 00:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| d5c8667b-d1bd-3729-b08a-95c3980f9f15 | -3.5158 | -53.8333 | 2024-11-24 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 93a91b24-4180-3b28-88fb-a0dd9535f06f | -2.8606 | -51.8143 | 2024-11-24 00:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 69216af3-a009-3e6d-b494-021a267f8f7f | -3.5343 | -53.8126 | 2024-11-24 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| e69ea3d1-8833-34e4-9398-afe36eb716a2 | -1.4547 | -46.036 | 2024-11-24 00:00:00 | GOES-16 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 85.8 |
| a97a262e-aba2-3865-abee-f05382c01181 | -1.6042 | -54.415 | 2024-11-24 00:00:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| e084132a-0a19-3251-bf66-86431bb9e424 | -0.8907 | -52.7685 | 2024-11-24 00:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 228.9 |
| 207c815d-8792-30c1-9691-fb1760aa717a | -1.4732 | -46.0357 | 2024-11-24 00:00:00 | GOES-16 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 37cbfd8f-b388-3797-b7cb-95af64c42115 | -1.4546 | -46.0582 | 2024-11-24 00:00:00 | GOES-16 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 5be15534-eb7f-39d4-880e-e318a789ec5f | -2.7149 | -46.2713 | 2024-11-24 00:00:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 75.8 |
| a9bd0b82-d25b-3ce1-b3d7-239ac2a04a80 | -5.0078 | -42.9466 | 2024-11-24 00:00:00 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 0e3cd5d2-3fd6-3499-995c-5fdeb4567787 | -3.242 | -53.2751 | 2024-11-24 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 5f367058-9149-3bc8-8a7f-0729b4a1d563 | -2.4455 | -49.1029 | 2024-11-24 00:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 340d3bcf-91b9-399f-a8f3-8377d5cae1f6 | -1.5129 | -54.1759 | 2024-11-24 00:00:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 108.8 |
| 7acfb06d-7d43-3a98-b9ca-29f16a3053a7 | -3.2569 | -54.2226 | 2024-11-24 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| afbeacf9-75ee-31e1-9c81-45e71fbd858c | -3.5995 | -47.5142 | 2024-11-24 00:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| c500233b-f5a9-37bf-9e76-137346a4b2bc | -1.6225 | -54.4148 | 2024-11-24 00:00:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 4362e170-9122-3cba-95da-11c5ce9d4d99 | -1.8239 | -46.6265 | 2024-11-24 00:00:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 25045627-cbb4-3db6-badd-b89c2799e38e | -3.1107 | -54.0054 | 2024-11-24 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 80af52b2-bd70-3773-a2a9-5fd13d2aa0d8 | -4.2605 | -48.697 | 2024-11-24 00:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| ff52bd85-71dd-38bf-8b10-ba934a325be8 | -0.8907 | -52.7888 | 2024-11-24 00:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 736ba02c-8b36-3b9b-b62d-3ae7f82e8fa1 | -2.4456 | -49.0816 | 2024-11-24 00:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 02c875a0-9d66-35f3-9149-fd1eb0cc92fd | -0.8907 | -52.7481 | 2024-11-24 00:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 100.9 |
| ac2bed0f-2314-39d1-a3ca-fa19ee331b98 | -3.2386 | -54.223 | 2024-11-24 00:00:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| b62cbd0c-50e9-33cc-bc36-c3a6618d9f8d | -3.2604 | -53.2746 | 2024-11-24 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 60.0 |
| efdbc01e-9628-3547-9670-cc3e80845b7d | -4.242 | -48.6978 | 2024-11-24 00:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 140.4 |
| 3ce3344a-9390-305d-be7c-913b62578219 | -4.2424 | -48.6334 | 2024-11-24 00:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 33.6 |
| eaaae996-1955-37d0-bbd0-7b22d199bd49 | -0.8723 | -52.7686 | 2024-11-24 00:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 171.5 |
| 144d1cbd-ce69-3ee2-85ad-a85e34f176e5 | -2.6963 | -46.2719 | 2024-11-24 00:00:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 55.4 |
| f8d5366a-82fc-34d7-be7b-e322e9e71984 | -1.5129 | -54.1959 | 2024-11-24 00:00:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 163.6 |
| 924180c6-9911-3c9a-b6b8-cf8e65c2acf7 | -3.78 | -52.3006 | 2024-11-24 00:00:00 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 857b6615-6381-3a21-b03f-d5984f870696 | -3.2212 | -53.922 | 2024-11-24 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| b92053fe-2a83-3ef2-ac35-c68d05bd20a9 | -3.1638 | -45.5195 | 2024-11-24 00:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 65.4 |
| fadf3c69-12db-3e89-a57b-9fdd4d9f887d | -3.0354 | -49.4688 | 2024-11-24 00:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 0458ebf9-667c-3f66-ba1c-7601835131ee | -3.5159 | -53.8132 | 2024-11-24 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 128.1 |
| 4b70ca80-63e9-3beb-93c0-6b15264b45b3 | -3.0582 | -53.2192 | 2024-11-24 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| a1a59ff3-fa33-3406-84f9-e6c1a31455c0 | -4.0848 | -50.36 | 2024-11-24 00:00:00 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| a7f485a7-3151-3ef2-8472-abd149d5af1c | -3.0355 | -49.4476 | 2024-11-24 00:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 717f0108-3c8c-3c56-87e3-fa96bda806b2 | -4.1033 | -50.3592 | 2024-11-24 00:00:00 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 0a6e07c9-5c70-3d6e-9d68-74aac4a27aa9 | -3.1068 | -45.7903 | 2024-11-24 00:00:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 94ae2bed-6d28-3ca1-900f-648c62387b0e | -2.5842 | -51.8829 | 2024-11-24 00:00:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 8b8f8db5-334c-364a-8d21-d9456b078c98 | -4.5403 | -42.9066 | 2024-11-24 00:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 5f458fe7-f967-335d-a6f2-b5d602abf3f4 | -1.4732 | -46.0579 | 2024-11-24 00:00:00 | GOES-16 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 9ebff09e-9931-3001-8a45-0ed8a783adf8 | -3.0766 | -53.2187 | 2024-11-24 00:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 4b1c7e5f-91ec-3dd5-ba30-c4733c37f6c8 | -5.0998 | -43.151 | 2024-11-24 00:00:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 545f1f4e-4d9d-3231-8603-9e03c4c6a124 | -3.1637 | -45.5419 | 2024-11-24 00:00:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 91.2 |
| 7d05bd0c-9838-328c-8673-4175a3247b06 | -3.516 | -53.793 | 2024-11-24 00:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| d83bc0d5-4b30-3e37-a09a-32e98a925f50 | -3.9562 | -50.1969 | 2024-11-24 00:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| de91e5ef-82c8-3376-b73e-a4ef85f549d3 | -3.6181 | -47.5134 | 2024-11-24 00:00:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 5bc9585e-fffd-3956-8173-36a6fc64e667 | -3.5159 | -53.8132 | 2024-11-24 00:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 73b1a6e6-c7a1-3a36-8c5e-96853ee8cb17 | -2.7149 | -46.2713 | 2024-11-24 00:10:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 96ccc547-14be-3e92-8aa4-dec4bbcc6c04 | -2.7148 | -46.2935 | 2024-11-24 00:10:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 7f8ebbab-ac4d-37db-8090-7e1b57390241 | -3.2386 | -54.223 | 2024-11-24 00:10:00 | GOES-16 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 68879ed1-1147-3280-9b31-f7a15b5be307 | -2.8606 | -51.8143 | 2024-11-24 00:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| e46ba1fd-9d4d-35e4-bf5a-255eb031a210 | -0.8724 | -52.7483 | 2024-11-24 00:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 107.5 |
| bc60ccb0-387a-3e19-ae7b-5d4ed431de66 | -1.6042 | -54.415 | 2024-11-24 00:10:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 5dff3230-30cb-327a-9bff-81efe02e71d8 | -3.6181 | -47.5134 | 2024-11-24 00:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 96104dd8-8e0d-34f0-b5a4-e4d71972b740 | -1.3666 | -53.8362 | 2024-11-24 00:10:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 0f1bee5d-df7b-329c-a81f-4a50b1251542 | -4.2424 | -48.6334 | 2024-11-24 00:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 37.1 |
| b8924e89-3284-36af-a73a-17a4299962f6 | -1.4732 | -46.0357 | 2024-11-24 00:10:00 | GOES-16 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 80.4 |
| c1f2cf02-145c-39b6-b231-db3e438a3e5c | -3.0355 | -49.4476 | 2024-11-24 00:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 57.0 |
| 47ad29ce-e50f-37d3-ab80-a8e92ef9a540 | -3.0582 | -53.2192 | 2024-11-24 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 760f4cee-7e94-301f-aaa5-6b3f467e73d1 | -2.9229 | -45.3712 | 2024-11-24 00:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 3a42c2f7-85f9-38b2-92ff-b8d8da678fe7 | -1.5312 | -54.1757 | 2024-11-24 00:10:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 7310885a-cc7f-3185-9874-41535751bc03 | -1.4732 | -46.0579 | 2024-11-24 00:10:00 | GOES-16 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 62.9 |
| e2f7a2d2-3791-3752-9b01-0d76361502dd | -2.464 | -49.0811 | 2024-11-24 00:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| af5dd407-f1aa-3b23-ae08-33c992db893b | -2.6963 | -46.2719 | 2024-11-24 00:10:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 58.2 |
| d803ab8b-9ed5-331b-a791-99d3ae463ffe | -4.242 | -48.6978 | 2024-11-24 00:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 132.5 |
| 4f68d5b0-5def-3b99-9139-48d7470afeac | -5.0998 | -43.151 | 2024-11-24 00:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 586b5e2f-9a90-30f4-b456-4ff9b7edb266 | -1.5129 | -54.1759 | 2024-11-24 00:10:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 130.1 |
| 0a0796e7-9679-32e8-a11a-0290c5ff97eb | -1.5312 | -54.1957 | 2024-11-24 00:10:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 9463defb-55da-3519-b555-9b43f3bd1305 | -1.8238 | -46.6486 | 2024-11-24 00:10:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 80.2 |
| d39b4283-5bad-3491-9ac7-b03713c12d70 | -4.5403 | -42.9066 | 2024-11-24 00:10:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| d6f08e37-3c89-388f-8621-f8d8d893178e | -3.1637 | -45.5419 | 2024-11-24 00:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 2cadb9a0-a91e-3ff4-bc73-b88e03787a7d | -2.5842 | -51.8829 | 2024-11-24 00:10:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 0940b62f-eeb2-3ead-886e-4bb24e2a95ad | -0.8907 | -52.7481 | 2024-11-24 00:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 5b102b97-83f5-3a69-9990-fbb93b95e716 | -1.8239 | -46.6265 | 2024-11-24 00:10:00 | GOES-16 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 122.5 |
| aacd97c8-638e-340e-a8e7-fbc8946d6354 | -4.0848 | -50.36 | 2024-11-24 00:10:00 | GOES-16 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 792249fa-7c14-3d3c-a75e-c47d422791e7 | -0.8723 | -52.7686 | 2024-11-24 00:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 233.5 |
| 26a3d3a8-af1c-3b45-bc1d-135ae67bc13d | -3.5995 | -47.5142 | 2024-11-24 00:10:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 24a09c6c-30a8-3fc7-8b1a-808640028e0e | -5.0078 | -42.9466 | 2024-11-24 00:10:00 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 617cdbeb-a110-332d-85f6-1450743cb535 | -3.242 | -53.2751 | 2024-11-24 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 0aad50a4-8b62-3ebf-b191-a746aa903718 | -0.8907 | -52.7685 | 2024-11-24 00:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 160.3 |
| 7fe432d8-5295-3902-8c5d-30779a637649 | -3.2604 | -53.2746 | 2024-11-24 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| f7d91cb5-af75-3781-9a65-ecc0529c6872 | -2.4456 | -49.0816 | 2024-11-24 00:10:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| dc42aabe-785f-3cb7-8370-a5ae1abfe4a8 | -3.1068 | -45.7903 | 2024-11-24 00:10:00 | GOES-16 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 637721dd-d9fd-3667-ace2-c6bac7826168 | -4.2419 | -48.7193 | 2024-11-24 00:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 4294f850-5219-3403-8351-502f5528e40f | -5.1185 | -43.1497 | 2024-11-24 00:10:00 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 8727ae23-67fb-3be6-baf8-e63110836ce0 | -1.6225 | -54.4148 | 2024-11-24 00:10:00 | GOES-16 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 910d7b3a-567f-36b5-90c1-232e05de44aa | -1.5129 | -54.1959 | 2024-11-24 00:10:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 159.8 |
| 0884a8f2-5d04-3b14-b556-fa04d53bbd98 | -3.0581 | -53.2395 | 2024-11-24 00:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| f005134c-6fcf-384f-a3e1-8b95418356cc | -2.7149 | -46.2713 | 2024-11-24 00:20:00 | GOES-16 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 4d34441b-cc2f-3728-a305-207b1c56dbf8 | -1.5129 | -54.1759 | 2024-11-24 00:20:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 912cdb8d-4950-33d3-a45a-2f530acc50ea | -3.0581 | -53.2395 | 2024-11-24 00:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 0d89536a-2fcc-3e67-a1ba-7dbd8f41ad45 | -5.1185 | -43.1497 | 2024-11-24 00:20:00 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 101.0 |
| ac2df7dd-2e7a-3415-802d-945bc3736712 | -1.4732 | -46.0579 | 2024-11-24 00:20:00 | GOES-16 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 0ec4d55f-c039-3629-8061-c21ef700b78d | -3.5995 | -47.5142 | 2024-11-24 00:20:00 | GOES-16 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 31906182-2dc5-3327-a2ff-a108ccf0f74c | -1.8053 | -46.6269 | 2024-11-24 00:20:00 | GOES-16 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 154.4 |


[Clique aqui para ver as próximas entradas](README2.md)
