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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 962c97d2-66ee-3ab5-8b58-ce6c2965372f | -11.3073 | -48.64325 | 2024-10-25 04:17:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0cb4ac95-7d72-349c-a3d7-38f03c1db5c9 | -11.30683 | -48.48382 | 2024-10-25 04:17:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0ddfc5bb-c6d1-38b9-95eb-dd354895bbb2 | -11.30302 | -48.48312 | 2024-10-25 04:17:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 35c7b632-8c4c-3a66-83a9-b51d5281687f | -11.30221 | -48.48784 | 2024-10-25 04:17:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 688ed565-24dc-34bf-b6b0-615446454edb | -11.30047 | -48.63673 | 2024-10-25 04:17:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a7bbc639-481b-3293-b0e1-4b8f4abb9f73 | -11.30001 | -48.47773 | 2024-10-25 04:17:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| faadb2fd-aa55-30b7-a6c3-9dcb992a42e7 | -11.2984 | -48.4871 | 2024-10-25 04:17:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 824ed88c-ae60-378c-abc0-116631780ceb | -11.29761 | -48.49173 | 2024-10-25 04:17:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| d2c085ea-49a0-3342-b7e2-d1d302437920 | -11.29744 | -48.63122 | 2024-10-25 04:17:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| abca57bb-d119-3058-8ee8-1e4d51952372 | -11.29665 | -48.63586 | 2024-10-25 04:17:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 90bf3e35-ecb4-3deb-a609-ac9547407cf1 | -11.29539 | -48.48176 | 2024-10-25 04:17:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b9ade63c-0777-3207-86d0-ad461076af38 | -11.29459 | -48.48639 | 2024-10-25 04:17:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bf05dee4-4301-3831-bc10-6e2a30a8d1a7 | -11.29379 | -48.49103 | 2024-10-25 04:17:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5386ec36-1a8e-3e60-b2e3-4598529f9fc4 | -11.28997 | -48.4904 | 2024-10-25 04:17:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8ab626e1-cd10-3198-8320-99f9468645bb | -11.28915 | -48.49512 | 2024-10-25 04:17:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 580a251e-4707-3384-8c5d-696d2699b7bd | -11.28695 | -48.48508 | 2024-10-25 04:17:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 91925295-003b-3ee2-85be-978b477d43a0 | -11.28613 | -48.4898 | 2024-10-25 04:17:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 16de606b-8b63-345e-bed3-2b621aedf8e1 | -11.28311 | -48.48454 | 2024-10-25 04:17:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 177bce3a-0f00-3b32-becc-c5cddcbef31e | -11.25255 | -48.73039 | 2024-10-25 04:17:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f3f9dc9b-8eb5-3b63-95fb-fd851878579a | -11.24996 | -48.69917 | 2024-10-25 04:17:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 235a4923-0efb-386e-9c6f-888b36b66926 | -11.08007 | -47.89603 | 2024-10-25 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1737ab21-7322-3480-ab94-673407ba17cc | -11.0793 | -47.90059 | 2024-10-25 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 43282490-5e5b-329e-9bac-5440f7b50cf9 | -11.07636 | -47.89542 | 2024-10-25 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b60477ae-b57f-3ea0-9252-1b784149677b | -11.07559 | -47.89999 | 2024-10-25 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8791c7e0-a67e-38b8-a94f-1cad6a57bea1 | -11.01986 | -48.27381 | 2024-10-25 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9843ac94-f2b7-30e2-be66-ff6ee9ec98bf | -10.94635 | -48.04193 | 2024-10-25 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| d6657783-02ca-39bf-a269-0dcf6eaab028 | -10.94561 | -48.04628 | 2024-10-25 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d329ca3e-6a2d-33e8-a4e1-181f4ac8d120 | -10.94336 | -48.03685 | 2024-10-25 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3bf14482-66dd-31e9-b27c-a2e497cccdc3 | -10.94189 | -48.04548 | 2024-10-25 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 455e406e-a87a-30ab-9458-0cf4343ab437 | -10.93964 | -48.03606 | 2024-10-25 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3d855af3-c030-3582-a906-fe6dc7270ff2 | -10.93818 | -48.0447 | 2024-10-25 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4e7de70e-1387-3096-bd09-3c5a17972481 | -10.92074 | -47.96675 | 2024-10-25 04:17:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 26ea00da-4c76-3011-832a-2b29ffba244a | -12.61401 | -48.50896 | 2024-10-25 04:17:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 22774345-f85c-3ad7-82c1-fa0b55d1c87d | -12.6132 | -48.51365 | 2024-10-25 04:17:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bbd2d9f7-9fb5-398d-8d73-044358eda115 | -12.61026 | -48.50827 | 2024-10-25 04:17:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 422d1c62-8893-34ad-9ff1-9a7c242fab7b | -12.60946 | -48.51289 | 2024-10-25 04:17:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8bdf9922-cc6d-30e2-b58b-6cf9727aa69c | -9.44175 | -48.88673 | 2024-10-25 04:17:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d72ca2ae-e66a-3630-9742-a0574f30c641 | -9.43771 | -48.88613 | 2024-10-25 04:17:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2f9bd5d7-87bc-38f6-bb77-ba0517872a24 | -9.43366 | -48.88556 | 2024-10-25 04:17:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 35c50cc0-da97-304f-9ff9-4dc2b788777b | -9.43267 | -48.88533 | 2024-10-25 04:17:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f1f93545-0f81-38fb-b83f-cb00a44235c8 | -8.97997 | -48.81786 | 2024-10-25 04:17:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 859d983f-1218-3d4b-883d-f966d4465d4e | -8.97935 | -48.82147 | 2024-10-25 04:17:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4e940b09-511e-3f04-ab67-4d97d363e9db | -8.97874 | -48.82508 | 2024-10-25 04:17:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 108d8633-ffe5-3c3d-96bc-1002a352023a | -8.97469 | -48.82442 | 2024-10-25 04:17:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 592f2dc1-e848-3b72-9d2d-9be96bb33754 | -8.8903 | -48.82785 | 2024-10-25 04:17:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 692d7bb5-5383-37f7-b169-690f33b4baf8 | -8.8897 | -48.83141 | 2024-10-25 04:17:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c60a7d4c-12f0-325e-b683-a26367c1948e | -8.81435 | -49.6346 | 2024-10-25 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54396373-d9e5-37ba-a227-54b9af104134 | -8.752 | -49.78873 | 2024-10-25 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 816f9209-2b6c-3bc0-88c9-7291b328ced7 | -8.71954 | -49.40342 | 2024-10-25 04:17:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5ccc5c7b-ed02-38e4-b79f-12db7ca639a8 | -8.68137 | -50.0351 | 2024-10-25 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 8632767f-4393-362b-a637-561a369b52fe | -8.68136 | -50.03468 | 2024-10-25 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| ca849aec-d099-3eb3-9b87-dfb24350a102 | -8.68063 | -50.03943 | 2024-10-25 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 1187984e-bedc-3bf1-9230-915d747837d0 | -8.68059 | -50.039 | 2024-10-25 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 245b5b32-56ad-3018-8c61-f4cd304c5b08 | -8.67779 | -49.09156 | 2024-10-25 04:17:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c0ae5a6c-9de1-352b-91fa-51aa46747c3b | -8.673 | -49.09465 | 2024-10-25 04:17:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a6974224-83e3-3e99-bf10-6d7a5ab11c28 | -8.67235 | -49.09843 | 2024-10-25 04:17:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b6c2dede-7652-3fb6-9293-29f3d3c2167d | -8.58393 | -49.22891 | 2024-10-25 04:17:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5356f917-3e4c-3b5c-8e73-67a40156d030 | -8.58327 | -49.23277 | 2024-10-25 04:17:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bb2b4a07-de05-35ad-9d32-4d4edc0d5c0f | -8.58042 | -49.2243 | 2024-10-25 04:17:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a81f79d7-856e-38e0-ae81-0c269842f391 | -8.57976 | -49.2282 | 2024-10-25 04:17:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ebc21798-eb1a-34c6-b89d-1d29ce7e5238 | -8.54282 | -49.54741 | 2024-10-25 04:17:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2284b167-ffac-3ba0-a305-a7476d109d60 | -8.54212 | -49.5515 | 2024-10-25 04:17:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ddc448b5-95c0-372f-a7f0-df940faf3f65 | -8.54142 | -49.55561 | 2024-10-25 04:17:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b8302ade-705e-3498-ba01-e486b0022baf | -8.53856 | -49.54663 | 2024-10-25 04:17:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 431c054d-c563-347f-81bb-e1be892c4d07 | -8.53786 | -49.55075 | 2024-10-25 04:17:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 3de9cca5-eb86-3080-95da-55c714ce9e80 | -8.53151 | -49.56218 | 2024-10-25 04:17:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ccb3858f-855b-31d2-abb3-3089c007f5f8 | -8.52428 | -50.0271 | 2024-10-25 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2e92c0cd-0f8b-3701-a2b2-e14ea825d093 | -8.46161 | -49.4379 | 2024-10-25 04:17:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f864d2e7-10fd-3a36-b457-5362a0326087 | -8.46096 | -49.43827 | 2024-10-25 04:17:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 73e9f90d-5c0f-3ba9-849f-7f5e8eeac230 | -8.45737 | -49.43715 | 2024-10-25 04:17:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2227b19a-0ff2-397f-88df-f98ed01500fe | -8.41802 | -50.09171 | 2024-10-25 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1ef59bf0-1faf-3661-8bcb-fc2508cd094f | -8.41359 | -50.09092 | 2024-10-25 04:17:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d500eced-7695-347b-85ca-15bf468b613f | -8.35933 | -50.04107 | 2024-10-25 04:17:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ee8d267-6c1c-343e-b171-9abc54d3d0ce | -8.35851 | -50.04072 | 2024-10-25 04:17:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2331259-2d54-387f-b84e-729cf5b3f3dc | -8.35341 | -49.63235 | 2024-10-25 04:17:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7979c10c-73bd-3fe3-9fbe-3c96b4c48498 | -8.34467 | -48.93412 | 2024-10-25 04:17:00 | NOAA-21 | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de0713b0-31f7-307f-8d81-7d0905b07b85 | -8.13081 | -49.79058 | 2024-10-25 04:17:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b12c6f10-227a-3428-a66a-78b2c331edd4 | -8.06258 | -49.37867 | 2024-10-25 04:17:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d5047947-d207-34c9-9b11-7ec869774eb3 | -8.02691 | -49.6341 | 2024-10-25 04:17:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 47e47fdc-89f7-338b-9608-1e81eaff8736 | -8.02618 | -49.63829 | 2024-10-25 04:17:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d24d150d-e6d2-3559-8b1f-c55a25ee73aa | -8.02257 | -49.63339 | 2024-10-25 04:17:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3af040a2-3759-3a5c-ae17-ffcadb3efd65 | -8.02184 | -49.63758 | 2024-10-25 04:17:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 678fa218-c06d-3f19-9f88-8aeab4cd4707 | -8.0175 | -49.63687 | 2024-10-25 04:17:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9a0fa6e1-74c8-37d7-9dcc-7c4fa4176b76 | -8.01317 | -49.63614 | 2024-10-25 04:17:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75db574e-21bf-3190-9706-6934e2f268b7 | -9.58685 | -49.64518 | 2024-10-25 04:17:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4a5c2f13-8c30-3436-8c42-6f78229a3536 | -9.58617 | -49.64909 | 2024-10-25 04:17:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 73ac8376-5a59-3a4b-bba9-dc95e28a6269 | -9.58331 | -49.64052 | 2024-10-25 04:17:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b44d83f6-f068-37b0-9f83-d7adf5266578 | -9.58263 | -49.64444 | 2024-10-25 04:17:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fdc3514b-50c1-39c9-9f3f-5ab69a64121c | -9.58195 | -49.64837 | 2024-10-25 04:17:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b8eb665e-ddaa-37ef-bd5d-9051f9baef3f | -9.57949 | -49.56276 | 2024-10-25 04:17:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c3507787-ae04-3c10-842c-908fa4ee462c | -9.94467 | -49.81292 | 2024-10-25 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b7fc8644-f8be-32d2-80bd-7a63ddb66009 | -9.8262 | -48.98452 | 2024-10-25 04:17:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b18be58f-0584-386f-a432-475c485f8d5f | -9.82217 | -48.98383 | 2024-10-25 04:17:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 57b71122-a83f-39d7-95e5-fa6b0d3d12c6 | -10.51445 | -49.46179 | 2024-10-25 04:17:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd5c15f7-2976-3746-91c8-bd829878cb85 | -10.37479 | -49.91672 | 2024-10-25 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 69d2bee2-cd12-3eeb-955a-a9ab6b52915a | -10.37408 | -49.92073 | 2024-10-25 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea714781-6f5f-3cbc-811e-7e4874f3a5c0 | -10.33055 | -49.35938 | 2024-10-25 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ecfd5de6-c26e-38c1-abec-870fb396cd52 | -10.20023 | -49.14773 | 2024-10-25 04:17:00 | NOAA-21 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c6988293-5b5e-3185-b80f-45c8d5d0dc11 | -10.19619 | -49.14703 | 2024-10-25 04:17:00 | NOAA-21 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d0bcf7d-28cc-31ce-8934-d64b0d26ee46 | -10.17675 | -49.50347 | 2024-10-25 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README45.md)
