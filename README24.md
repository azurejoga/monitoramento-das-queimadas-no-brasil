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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a4a9fdd-8ed8-3f10-a931-1d6d42891682 | -11.66398 | -58.26791 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7bbad232-21c5-392e-ab49-48d960338639 | -15.97062 | -57.16469 | 2024-12-11 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 89df586e-0a9c-3269-b433-616455d234d7 | -12.54312 | -58.33861 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3a6a1cf3-3da3-3786-9e4e-d2577dfcc370 | -12.54186 | -58.36754 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6c39193d-9ee6-3f0e-b104-8df3079121d1 | -12.70678 | -54.97179 | 2024-12-11 04:59:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3233dce2-e784-3596-b0d4-1224bee1bdf7 | -12.71291 | -54.97644 | 2024-12-11 04:59:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 41d4d60d-91bc-3cbb-9af1-f765c7d1b870 | -12.54894 | -58.36877 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 655af120-146a-3a8e-99e0-bcb6df0a4c8a | -15.08334 | -59.63997 | 2024-12-11 04:59:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3a1976dd-ec6b-3bf1-a2ca-88fd24829324 | -12.53113 | -58.3449 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bbdc1789-0eb1-37a6-a458-d4cb938e72b7 | -12.53846 | -57.72332 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96091da8-69a6-3f31-96b7-1d1d170369bd | -12.55453 | -58.35726 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 08a8aa05-1823-3fca-8587-f759474f8ca5 | -12.55956 | -58.37064 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7f0c77ec-0225-395d-b2de-54f73be9f199 | -15.15932 | -56.47738 | 2024-12-11 04:59:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| be4f6fc4-c6d8-30be-a469-8fecd341a547 | -15.15599 | -56.47682 | 2024-12-11 04:59:00 | NPP-375D | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ac92fcc0-496a-3705-8b25-23df4cbece30 | -12.55602 | -58.37001 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a66e8bb0-bddd-3643-8ec6-23e24bfbfac3 | -12.81997 | -59.03985 | 2024-12-11 04:59:00 | NPP-375D | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9ee73850-b574-387a-858a-8eec1a99de19 | -12.8474 | -59.02941 | 2024-12-11 04:59:00 | NPP-375D | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1a7b20cc-b1da-3e77-91c8-73adff3dfaf6 | -11.03796 | -57.99124 | 2024-12-11 04:59:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 44a07955-a63c-38e3-900b-83199549ff04 | -15.08409 | -59.63557 | 2024-12-11 04:59:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ac1ef7c-2c68-3ea2-88fb-66ea4dd0bc9e | -16.07848 | -60.08912 | 2024-12-11 04:59:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4016b9cb-2d31-3ee1-a947-f700f06a0f50 | -12.56024 | -58.36658 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b34cc1d2-cafa-3d13-a601-96caff351d37 | -11.72206 | -57.4407 | 2024-12-11 04:59:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1355a948-48b8-37a8-8e73-f80f12cd923e | -14.57301 | -56.71455 | 2024-12-11 04:59:00 | NPP-375D | NORTELÂNDIA | MATO GROSSO | Brasil | 5106000 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e94e731-fcd9-3e68-9b7b-bbce460ad6be | -12.53477 | -58.36634 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 33533157-ba26-38ef-99e6-e9e3dd3092c5 | -12.53591 | -57.7386 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3f19f161-3003-3316-ad2f-c4192f738e51 | -12.84764 | -59.03138 | 2024-12-11 04:59:00 | NPP-375D | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e8bf5f16-7565-3817-9e2e-613fbe48e2d6 | -12.54951 | -58.3439 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 2d2d5408-8fb6-3c24-a3cb-ad815cd71e3e | -15.97672 | -57.16946 | 2024-12-11 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 211cd417-37d9-32c5-b9a4-76977f0664f6 | -16.87863 | -57.51376 | 2024-12-11 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 9d9468b5-0177-350b-ab0d-7facbfbacb2d | -15.96728 | -57.16411 | 2024-12-11 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0aac7887-3588-398b-a435-9ed1b6bb6ac7 | -17.74128 | -54.21338 | 2024-12-11 04:59:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 38fae793-f07a-3dea-9536-7adc2228326d | -15.08258 | -59.64435 | 2024-12-11 04:59:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c9ebea5b-52e8-3af4-a7d0-dbecc324e918 | -12.53071 | -58.35391 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| dec16ff6-d8a6-325f-b594-bfd6233c2466 | -15.0196 | -57.62434 | 2024-12-11 04:59:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b5e8faef-a047-32ad-b196-15d2da470c2e | -12.55236 | -58.34858 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 3a87ea9b-1b95-31b7-ba75-822a01ae2b6e | -12.53272 | -58.34177 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 45850a33-cd15-341b-bd09-d6df8cacad77 | -12.54217 | -57.74366 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 77ddfe24-70a8-35e3-abd0-6fdef5778da5 | -12.53626 | -58.34236 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 6909b9be-82d2-380c-96b3-fd1b25f69495 | -12.52975 | -58.35298 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c62540d6-858d-3f3b-834f-95c72c2d152b | -12.54392 | -58.35537 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 09b20fd5-ae66-376d-98b5-98b73ac49c8c | -12.53559 | -58.34643 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f7a68cc1-b03c-3849-b8f2-2879321f507a | -14.57635 | -56.71512 | 2024-12-11 04:59:00 | NPP-375D | NORTELÂNDIA | MATO GROSSO | Brasil | 5106000 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f02abd98-d729-3b0c-8b37-e8ae535460aa | -12.54175 | -58.34669 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8d7eaf5d-d19b-39c1-bca8-4a31bc13e905 | -12.53192 | -58.36167 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d85d7546-a617-3165-b1c7-7e88e1e902cd | -13.37219 | -54.24904 | 2024-12-11 04:59:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 71562c19-140d-35a2-a52f-a18715c61792 | -12.56317 | -57.76701 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3b83d6d8-08e5-359b-8fd3-2663d4e6fc84 | -12.54882 | -58.34793 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 57f771f5-1b27-3c87-a1ab-7fad47486728 | -12.57072 | -57.76436 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7f178b3f-ad03-3570-b7d4-90e3519dd079 | -12.71012 | -54.97233 | 2024-12-11 04:59:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b46b72ef-2520-31b0-8af3-1a1dfde5b701 | -16.02647 | -57.58297 | 2024-12-11 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 76dd2228-da2c-37d7-bb70-7d230937dae4 | -12.55521 | -58.35324 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0b926b62-9cea-3ce0-b233-e50210bdf99b | -12.56663 | -57.7676 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 09557cd7-cfc6-3ca1-a5d7-63a11cd2f9bc | -12.53693 | -58.3383 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b30f8de1-c967-3a7a-8e3b-aab588bc72a9 | -15.0885 | -59.63186 | 2024-12-11 04:59:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49aab5e1-a121-3a1c-8bf9-3681be727344 | -12.53969 | -58.35882 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 0b786dba-695e-300e-be8c-c28e14c9e03e | -12.5333 | -58.35357 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5d330a45-ce4e-33db-ac95-bf88a433f402 | -12.70957 | -54.9759 | 2024-12-11 04:59:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 185febf5-f64e-3b61-8ee2-0ee3734a2dc2 | -17.24041 | -54.44654 | 2024-12-11 04:59:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4a50a4bf-3c7b-3c7c-ae40-05b403b0734c | -12.53684 | -58.35416 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 36f670f5-e13c-33f2-a7e9-e8db9739e76a | -12.53753 | -58.35012 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 0caebf5c-3c2f-3827-8a33-7cb4baa69d56 | -16.0519 | -57.18181 | 2024-12-11 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| c722aff6-35e8-3ce1-8067-53ed6f1dbeb4 | -12.55739 | -58.3619 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b59caaea-e839-3547-9584-4a6580a63963 | -15.08925 | -59.62748 | 2024-12-11 04:59:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a189048a-6536-3252-888e-b1fbf363bee8 | -12.54597 | -58.34327 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 977f5faa-0a12-3430-bcc0-09c1ebdddf33 | -12.53359 | -58.35856 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f3c53f82-3c27-3145-b2b3-81426bef33f0 | -14.28737 | -57.46243 | 2024-12-11 04:59:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8a7ffd83-51c0-3351-8d2d-79aa08c01b26 | -16.0777 | -60.09361 | 2024-12-11 04:59:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9368ca44-0c5b-3f35-9488-e3376afa0ce1 | -11.77942 | -55.12928 | 2024-12-11 04:59:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 194753fd-4647-3cea-b49f-e8fe21820ce2 | -15.97004 | -57.16832 | 2024-12-11 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4fc6eba3-37a5-30b2-ad22-6e6017b15672 | -12.53493 | -58.35046 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 0dd53350-bccd-329d-9ff3-0715deff604f | -12.55317 | -58.36533 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| c7c21612-8347-36d8-9215-1e534ecd1d75 | -12.54746 | -58.356 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 3e0e8451-73bc-3091-b8a8-ddbded7c4a88 | -16.08217 | -60.08982 | 2024-12-11 04:59:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7fa719d0-4dd2-3f4e-841a-94c8f5c821b0 | -15.09353 | -59.64639 | 2024-12-11 04:59:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 75a92f80-c137-3948-a7f9-8a60ab896caa | -17.74011 | -54.22161 | 2024-12-11 04:59:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7548afab-79b6-32f3-a786-1accc09ed5b4 | -12.55807 | -58.35789 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 31b41008-3de1-39a8-89e6-e920357b6705 | -12.53831 | -58.36694 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d2fc4289-e6fa-3532-846e-ddaa96b37eb6 | -12.53292 | -58.36263 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6e1b6d53-ecaa-3948-adc6-adeeb8feda78 | -12.55827 | -57.71093 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0754869d-8b66-3dd2-9753-3d2c6ab4954e | -12.53936 | -57.73921 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8d442bbd-7b7e-3440-8ed3-b416c156c036 | -12.71346 | -54.97287 | 2024-12-11 04:59:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bc864c68-7288-325b-8297-97e9ff5d346e | -11.36579 | -57.79897 | 2024-12-11 04:59:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed032b7b-8193-3da8-a660-fa273132b798 | -15.08485 | -59.63118 | 2024-12-11 04:59:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2776023b-ae2f-36ae-b736-bcf8fa6a250d | -12.53437 | -57.72652 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fbcd42fb-6d71-378e-9a05-69c4ed4ac635 | -12.55875 | -58.35386 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6094b01d-d683-3712-8aac-e7574bed5699 | -12.54814 | -58.35196 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a65fd119-c097-3684-bfab-8ecab290dc0c | -14.97154 | -44.4061 | 2024-12-11 04:59:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 820110fd-90ff-34b2-8980-7c7ca2549b96 | -12.54323 | -58.35942 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 695c7802-bcf5-37a6-88cf-40b84743898c | -12.55671 | -58.36595 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 978f3a52-324b-385a-bb4a-30d3ed618ac0 | -15.9667 | -57.16774 | 2024-12-11 04:59:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 73ff3768-1488-3ee6-9274-97ed47a258f8 | -12.55589 | -58.34921 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 90fbacc9-02cb-349d-ae03-502745d94ad6 | -12.55019 | -58.33987 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3525f352-93b3-38bb-a5c9-992c0a56c2e8 | -12.55031 | -58.36065 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| a3a10578-a42a-31fb-b6f4-ef7626cf0053 | -12.54609 | -58.36408 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a8a626a8-af29-36de-a97d-286a944f267c | -12.54677 | -58.36003 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 71126ada-7b25-3ce2-9ee4-ba2a1f6c3921 | -12.53261 | -58.35762 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f789c350-fb32-3c34-b30e-77416c5fa0a0 | -12.53398 | -58.34953 | 2024-12-11 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5ae87d7c-9ebe-32b2-8cbc-b92c6ef2a6e3 | -13.48674 | -60.34785 | 2024-12-11 04:59:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6e3398c5-56d3-3a5c-b341-bde4c6d13604 | -11.36229 | -57.79834 | 2024-12-11 04:59:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 054ba8d8-afdb-39d5-aec8-80a86155803b | -14.81645 | -46.95689 | 2024-12-11 04:59:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README25.md)
