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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ccf60383-a437-3aba-b922-a90620cedd97 | -9.66369 | -56.96133 | 2024-09-30 04:32:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c80221da-8743-3558-9a8d-8b7f49f0ef9a | -9.66176 | -56.95103 | 2024-09-30 04:32:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c651a272-beec-3a43-9d6e-40dc321ed56c | -9.66123 | -56.95398 | 2024-09-30 04:32:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 36cdc0ac-6e42-37e9-8cb1-902097e3c86f | -9.6607 | -56.957 | 2024-09-30 04:32:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e5538928-a66c-392b-a568-0385c649b272 | -9.66031 | -56.95146 | 2024-09-30 04:32:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2748bfe-17ee-3718-ad63-ba739882cd0b | -9.65976 | -56.95441 | 2024-09-30 04:32:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a22e7dd-6385-3804-ac27-9d6cdce37229 | -9.6592 | -56.95742 | 2024-09-30 04:32:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1aae24ba-3bb6-3704-a1a4-9b5b9d3c58d6 | -9.65084 | -56.97431 | 2024-09-30 04:32:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a3f6e049-220d-30e7-af9b-0b44682054eb | -9.65029 | -56.97725 | 2024-09-30 04:32:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f17f7802-c813-3f28-88be-4efe10aa15d4 | -9.64795 | -56.97001 | 2024-09-30 04:32:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cbbaa99d-8bc4-31c4-a9a6-789764dd02f7 | -9.64742 | -56.97297 | 2024-09-30 04:32:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f1986656-6203-378a-ac2b-1bc1aa4447fa | -9.64689 | -56.97593 | 2024-09-30 04:32:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d894a0dd-ee43-3ecf-a320-50aa82c5cfe2 | -9.64636 | -56.9789 | 2024-09-30 04:32:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2aef6107-718a-3b3c-a937-4ca47f6ade4f | -9.64634 | -56.9704 | 2024-09-30 04:32:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6d5503a9-e800-38cd-884b-fae8a4688bbb | -9.64579 | -56.97335 | 2024-09-30 04:32:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 67bffa26-74f0-396c-a046-f1a5871b18c9 | -9.64524 | -56.97631 | 2024-09-30 04:32:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d38829cf-1798-3b07-93f8-0448ea1a9318 | -12.40876 | -57.79284 | 2024-09-30 04:32:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe4ef70a-0c2f-3416-afa6-9b3fa98b65ac | -12.40423 | -57.78894 | 2024-09-30 04:32:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0fc84637-248f-3704-86d8-cdd0571639fd | -10.69337 | -58.53333 | 2024-09-30 04:32:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a0761ec-60c7-385c-a553-c170cfa87433 | -10.69266 | -58.53704 | 2024-09-30 04:32:00 | NOAA-20 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ec40102-94b6-3f6f-8449-347e3aa69af5 | -11.79059 | -45.44553 | 2024-09-30 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e8a5cd1c-3c68-3ac4-ac4c-858de959a0ef | -9.25705 | -40.82299 | 2024-09-30 04:32:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| cf5eac5c-3c3f-39ea-8546-a3e7a20b3074 | -9.25227 | -40.82235 | 2024-09-30 04:32:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 86874da4-59d8-390c-83b8-6cda2a02ba70 | -11.78569 | -45.45353 | 2024-09-30 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c1cd51eb-2e7d-3adc-b459-5ae94f639c18 | -8.68644 | -41.06466 | 2024-09-30 04:32:00 | NOAA-20 | AFRÂNIO | PERNAMBUCO | Brasil | 2600203 | 26 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 4e18227b-5ae5-37a3-abcb-37b88cd5fc49 | -8.43373 | -41.93264 | 2024-09-30 04:32:00 | NOAA-20 | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 56838d8a-38e2-3fe2-8498-4fd625d28d41 | -13.75572 | -42.60705 | 2024-09-30 04:32:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b67e798e-5f70-3227-9af8-cc060adffd49 | -13.75181 | -42.60192 | 2024-09-30 04:32:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8d0161ee-0cda-3e42-a3bb-981209331af2 | -13.75119 | -42.60659 | 2024-09-30 04:32:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a174bf2f-4a81-3806-b5ba-5877f126d4b0 | -13.87267 | -43.56677 | 2024-09-30 04:32:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| be7f55ca-7813-3a14-b365-0090d654024f | -9.28868 | -43.50722 | 2024-09-30 04:32:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 109992e1-4c4e-3961-9276-f26c73cd63a5 | -9.27972 | -43.51297 | 2024-09-30 04:32:00 | NOAA-20 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c41ce11c-1293-3c9c-b530-737898a86f82 | -10.26169 | -43.55624 | 2024-09-30 04:32:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 31264566-cddb-30df-a3c3-4b0c0388cb02 | -10.25716 | -43.55926 | 2024-09-30 04:32:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f97fd03-7a7a-34e4-b231-a8fdf1365b58 | -9.91189 | -44.07637 | 2024-09-30 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4bf911b0-1458-30fd-a95f-4ed3825f5906 | -9.91096 | -44.07462 | 2024-09-30 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6e34a533-ecce-32fa-91f8-f091d23a3954 | -9.48516 | -44.06685 | 2024-09-30 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d0f3fee6-3d83-393e-81ca-2b8c31512aeb | -9.48379 | -44.06405 | 2024-09-30 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b5da6610-ef52-35b4-9318-9145f8fb61fc | -9.48131 | -44.06618 | 2024-09-30 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dbd79491-8ead-3446-a0c6-2ba1a66b384a | -9.47995 | -44.0634 | 2024-09-30 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 546fad2b-f94e-39cc-9c94-3506baf2679b | -13.44019 | -44.02586 | 2024-09-30 04:32:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac27a482-b74b-3b6e-b227-dd0483d3dc6f | -13.43611 | -44.02526 | 2024-09-30 04:32:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1409f427-42ff-3311-aeb2-2d73afb7c17a | -13.43101 | -44.03208 | 2024-09-30 04:32:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8f7b3fce-3c89-322b-8366-01f7179e2980 | -12.95123 | -44.84673 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ac8a8316-335f-35bd-866a-4ebe5c50779c | -12.93479 | -44.86737 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 10634ca6-18d7-37ba-8cf1-55951b847f0a | -12.83863 | -44.27095 | 2024-09-30 04:32:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be8d042c-683d-3127-97d0-f8c8913b0601 | -12.83416 | -44.27389 | 2024-09-30 04:32:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 88335cfa-4018-3f92-b9cc-1a47625d66ae | -12.79934 | -44.81074 | 2024-09-30 04:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9c831124-c011-39ce-b61c-43c9223c6907 | -12.73014 | -43.48296 | 2024-09-30 04:32:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9f30338f-a9e6-352c-8e5a-db03900f90a2 | -12.72962 | -43.48687 | 2024-09-30 04:32:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 28ac79cc-0bd8-3b81-a05b-5e7fd9c28f63 | -12.7249 | -43.4902 | 2024-09-30 04:32:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 412d681f-18ca-32c5-aed0-b8e53246541c | -12.72437 | -43.49412 | 2024-09-30 04:32:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4480f2c2-77f4-3a3d-b0af-2d417d7b2939 | -12.72018 | -43.49354 | 2024-09-30 04:32:00 | NOAA-20 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 4a2066ed-83a5-31be-917b-7d08052ef2ab | -14.527 | -44.98387 | 2024-09-30 04:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb4357e9-80d8-38c5-a889-00bf0c96b303 | -14.52631 | -44.98898 | 2024-09-30 04:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 839bdd0e-a6b9-3b77-855b-8fe2a0a39863 | -14.52612 | -44.9866 | 2024-09-30 04:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5f734e93-6eb8-3fbe-93b1-0d72b53db2aa | -14.493 | -45.24987 | 2024-09-30 04:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b33f2434-c2a0-3e7f-a69b-c479a9186138 | -14.49232 | -45.2547 | 2024-09-30 04:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a1baa53a-cb92-319e-8e29-680c958ace8b | -14.49171 | -45.24723 | 2024-09-30 04:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bf6f42b9-5a91-391d-b646-07e750f8ed37 | -14.49106 | -45.25207 | 2024-09-30 04:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| da3b8ad6-bd1a-37d4-82b7-4628bb8c351d | -14.48916 | -45.2493 | 2024-09-30 04:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f7579029-6073-3b64-abda-f70f2aecabea | -14.4891 | -45.26656 | 2024-09-30 04:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e88bd800-97b3-3a7a-a542-25f3f446201f | -14.48286 | -45.23845 | 2024-09-30 04:32:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| afe6e557-1b73-367d-8f7a-e231b18fabb5 | -9.28744 | -45.63732 | 2024-09-30 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 8d8a6e8b-703f-36c0-81de-812c839a11f0 | -9.28391 | -45.63674 | 2024-09-30 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d941f216-2079-3eb7-9371-a459b13955f6 | -8.89389 | -45.63503 | 2024-09-30 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9a05a995-cfcb-3636-ae65-d8817c23c707 | -8.37747 | -45.43981 | 2024-09-30 04:32:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| be1d7d0e-1f0b-3c4d-9879-3d861ed9a1ff | -7.87692 | -45.33256 | 2024-09-30 04:32:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f8b33659-7581-3569-97dc-3d41784ae729 | -7.8763 | -45.33658 | 2024-09-30 04:32:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 15460399-2ac1-331d-988f-4b98720b9966 | -7.87338 | -45.33203 | 2024-09-30 04:32:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68087394-1232-39bb-b1c9-cead8ea44173 | -7.86984 | -45.3315 | 2024-09-30 04:32:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ddd8a581-0bfe-33b8-95ff-7a7238890235 | -8.89555 | -44.09314 | 2024-09-30 04:32:00 | NOAA-20 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 098b1396-82c8-3ef6-9e50-082022005520 | -8.64173 | -44.05569 | 2024-09-30 04:32:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7e7fd588-b58a-37bd-bde4-3eb5d2aee8c2 | -8.07234 | -44.01641 | 2024-09-30 04:32:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 319f7dee-9d03-3c15-af17-fedf7754aea1 | -8.07204 | -44.01382 | 2024-09-30 04:32:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1152b2d9-43be-3605-828d-94c06cb39f78 | -8.87558 | -44.85975 | 2024-09-30 04:32:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b5e0c614-d026-3e4c-868e-2995021df9ce | -8.81993 | -45.21029 | 2024-09-30 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 09a0be8b-939e-30f7-8b84-55401bf98afe | -8.80704 | -45.12322 | 2024-09-30 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8d003100-6d24-3d9b-9cbe-ef9596ee73bf | -8.80405 | -45.11851 | 2024-09-30 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 159cb758-c264-3555-a366-84e5537c5b69 | -8.80105 | -45.1138 | 2024-09-30 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d52b0d21-a1ff-3231-a35e-45ba038ebb61 | -8.79744 | -45.11325 | 2024-09-30 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 055a2cb3-3b1b-3149-bb15-ebb8ffe05f86 | -8.76446 | -45.15232 | 2024-09-30 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4be8ba46-3711-39ce-bc1c-76713c98f439 | -8.76383 | -45.15649 | 2024-09-30 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 917660fa-e21d-33eb-a646-c97e39a0ef3c | -8.76164 | -45.21966 | 2024-09-30 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5049e54b-fac1-30c5-afe2-8cc1137f3a82 | -8.76024 | -45.15593 | 2024-09-30 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 53064db2-3e77-36e6-81ff-65a4b2d71933 | -8.75961 | -45.1601 | 2024-09-30 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 790fa55d-2fb9-3c2c-820d-319d4f0e1ae0 | -8.75898 | -45.16426 | 2024-09-30 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df433912-6397-3831-bfe9-48bfac2477f4 | -8.53114 | -44.73906 | 2024-09-30 04:32:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 82b29ee3-6eeb-310b-9039-6ec99462151a | -8.5281 | -44.7342 | 2024-09-30 04:32:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c4ca16c4-e506-39d5-8399-e49062732788 | -8.52747 | -44.73851 | 2024-09-30 04:32:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 53f65b7c-28a2-3768-8a32-28e5a743c2c6 | -8.52506 | -44.72932 | 2024-09-30 04:32:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 097671fb-0f97-31e4-9c95-1f7bb101d394 | -8.52328 | -44.71577 | 2024-09-30 04:32:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| dee6aac4-a210-3768-865a-3f0e7e34ebca | -8.52265 | -44.7201 | 2024-09-30 04:32:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1b48af54-7543-334b-9de0-ca3a80220f84 | -8.52252 | -44.89979 | 2024-09-30 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 40909238-ab1c-397d-b5f9-4bc9101c8380 | -8.52202 | -44.72444 | 2024-09-30 04:32:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e93c534f-e773-33c3-b5ed-4804fc43d15a | -8.52051 | -44.71231 | 2024-09-30 04:32:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 232769ba-afad-34db-b164-05acb7fb994e | -8.52024 | -44.71085 | 2024-09-30 04:32:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1b1aee5c-df5d-343b-b30e-b52e0d99cbcd | -8.51986 | -44.71664 | 2024-09-30 04:32:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e4dc6b38-e673-3a8f-992f-80592ab1420c | -8.51961 | -44.71519 | 2024-09-30 04:32:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 64274168-34fe-38f1-ac34-c3ed0195004d | -8.5175 | -44.70741 | 2024-09-30 04:32:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 10.6 |


[Clique aqui para ver as próximas entradas](README33.md)
