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

## Dados Diários - Página 127

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| aa4a1918-143c-3464-8194-cbe56771713e | -13.40698 | -61.92549 | 2024-10-08 05:25:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 11742054-2d85-32f9-8dca-3a6d345d0b45 | -13.40643 | -61.92902 | 2024-10-08 05:25:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f924df42-7439-33b9-95f4-bda1ab13507a | -13.40588 | -61.93256 | 2024-10-08 05:25:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b9400581-79ea-3988-b75e-5982952be9de | -13.40368 | -61.92495 | 2024-10-08 05:25:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ffeab6d-ed1b-38a8-b8a5-8dec1eb6140a | -13.39485 | -61.938 | 2024-10-08 05:25:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0117d3cc-3b7d-3046-8c2d-a41cf0f0d4f0 | -13.39209 | -61.93393 | 2024-10-08 05:25:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2734b0f5-d645-3a49-966c-4478c6e8c5bb | -13.38934 | -61.92985 | 2024-10-08 05:25:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d74f0cdc-b438-388c-ac3d-e03d60a41352 | -13.38878 | -61.93339 | 2024-10-08 05:25:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 55ac6abc-c905-3560-96d7-701edda9c41e | -13.38603 | -61.92931 | 2024-10-08 05:25:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c1ae36fe-b400-3c60-bfe7-b7fad266a57f | -13.38548 | -61.93285 | 2024-10-08 05:25:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f072892f-e73b-365c-9198-534ae2ed5241 | -13.37996 | -61.94643 | 2024-10-08 05:25:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5105f37c-43ed-35b1-9f60-f116ba9dd1e6 | -12.39674 | -61.50199 | 2024-10-08 05:25:00 | NOAA-20 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dda742b6-68bd-3537-b3b2-53154725d6ab | -12.39343 | -61.50146 | 2024-10-08 05:25:00 | NOAA-20 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c1265e65-644f-3e48-81b4-0ec82695c5cd | -12.81773 | -60.97193 | 2024-10-08 05:25:00 | NOAA-20 | CORUMBIARA | RONDÔNIA | Brasil | 1100072 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8492334f-a6e5-3ad0-bea7-f5f6a2f2d404 | -12.04182 | -63.13245 | 2024-10-08 05:25:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6bae5760-000e-3f70-9555-7ae2b2175c37 | -12.03284 | -63.135 | 2024-10-08 05:25:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26e681be-74c0-315a-a5a9-5677c24643db | -12.03006 | -63.13079 | 2024-10-08 05:25:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4efbd995-8a37-38d7-a411-0ffbd1fcd6ac | -12.02948 | -63.13444 | 2024-10-08 05:25:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 98b19068-25fc-320f-994f-d7f4e7b5c1e2 | -11.90232 | -63.24823 | 2024-10-08 05:25:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 79c9b6e6-d7b4-3395-9b29-95146357c90c | -12.99442 | -62.75046 | 2024-10-08 05:25:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f65a7110-dd08-35ae-900c-d4f088239a3d | -12.9911 | -62.7499 | 2024-10-08 05:25:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3f5defad-3e9e-3d70-8854-49e17fd9483a | -12.98845 | -62.72386 | 2024-10-08 05:25:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dd180c73-1858-3e44-8abb-fd63b0f75a43 | -12.98591 | -62.67595 | 2024-10-08 05:25:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e6fad11e-1f27-3ade-81a2-75577381cfaf | -12.98513 | -62.72331 | 2024-10-08 05:25:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4468dbcb-68ee-3183-8988-c61b86b688e5 | -12.98316 | -62.67184 | 2024-10-08 05:25:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51e828e0-68df-3115-ba91-0e256743d5bc | -12.98259 | -62.67539 | 2024-10-08 05:25:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa7ee045-1cbe-33c0-8909-ca6e7e8e2ee4 | -12.97966 | -62.67509 | 2024-10-08 05:25:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d381176e-b904-32ba-9a2d-f000745763ef | -12.97909 | -62.67865 | 2024-10-08 05:25:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d5e77371-68f3-39be-aa6c-d857aa3ae4bb | -12.97853 | -62.68221 | 2024-10-08 05:25:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| bc2620ef-ed93-3f2d-bee9-8dbd31b523aa | -12.97701 | -62.79513 | 2024-10-08 05:25:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21aa5341-ed53-31b4-990d-9a9998cf0acb | -12.97368 | -62.79457 | 2024-10-08 05:25:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 780c95e4-a913-3677-89d8-9b0fd55d9a00 | -12.97351 | -62.69233 | 2024-10-08 05:25:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4324348c-45ef-3f0c-8fb5-ec42e2cd0e3f | -12.97181 | -62.70301 | 2024-10-08 05:25:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dfe096db-bb3f-386d-b7b5-2a4f43f72df4 | -12.97132 | -62.68465 | 2024-10-08 05:25:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 224f513e-041a-3bc8-bf54-6f3b5a3e34e4 | -12.97075 | -62.68821 | 2024-10-08 05:25:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2098ccd2-1530-3dca-bc59-eff00994e139 | -12.97067 | -62.71013 | 2024-10-08 05:25:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f431d1d8-9f55-3abd-a10f-6bd79b11698f | -12.97019 | -62.69176 | 2024-10-08 05:25:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8641fb5a-f488-3557-9ffa-b1fc6c603886 | -12.91515 | -62.73746 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a204714f-cbf7-3845-8271-07a7d0ffac5b | -12.90631 | -62.72868 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2a687bb5-7fe4-3965-8bbc-02cb5cebc388 | -12.87217 | -62.79253 | 2024-10-08 05:25:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2679b73b-6e03-3c33-a2e2-984cd2c7323c | -12.8677 | -62.79912 | 2024-10-08 05:25:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 244ff96e-c46c-395a-92bb-a168423a039d | -12.86219 | -62.79087 | 2024-10-08 05:25:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| dc65dba6-2a7b-3a2e-bf73-1c4a00773695 | -12.85381 | -62.80048 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ff5e00bd-793d-3c46-850e-9b738fddc261 | -12.85041 | -62.80345 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 99b7745f-a3b7-3241-9644-6a946c42ca8d | -12.84708 | -62.80289 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a3b54ca4-8023-3ad3-9486-01ea54fdd290 | -12.83005 | -62.46078 | 2024-10-08 05:25:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9c79b4e1-c59f-32d3-9e86-80cf82c0e1b4 | -12.82674 | -62.46024 | 2024-10-08 05:25:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 44a64eac-c955-3f12-939d-e931f517d513 | -12.58885 | -62.56689 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 034fbea3-12de-333f-9a37-0c6c13668cf0 | -13.05013 | -62.31579 | 2024-10-08 05:25:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df33d7b2-8974-3124-a253-6970d148b9bb | -12.88645 | -62.4483 | 2024-10-08 05:25:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 58dcc1ea-78cb-3bff-98c2-80bde9660af1 | -12.8837 | -62.44422 | 2024-10-08 05:25:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 39ad1bef-9131-3867-9145-49422b1e63b0 | -12.82343 | -62.45969 | 2024-10-08 05:25:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4dd38d58-6d60-39ef-833a-50a7489e439d | -12.82286 | -62.46323 | 2024-10-08 05:25:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e1f38460-030e-3bbf-8fdf-e29d37b82d3f | -12.81955 | -62.46268 | 2024-10-08 05:25:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 557167dd-db78-36ee-a50e-eaf2bf380220 | -12.75214 | -62.2674 | 2024-10-08 05:25:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 8501364c-e9cd-3d94-8088-abfd4291f2a7 | -12.75133 | -62.07929 | 2024-10-08 05:25:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aa3571e5-2b5a-3da7-ba16-fa9bf0c33702 | -12.74883 | -62.26686 | 2024-10-08 05:25:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 8848d800-9793-33af-82f2-18d2bbad7922 | -12.74827 | -62.27039 | 2024-10-08 05:25:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7574c0a9-a351-31b8-b8a2-03725d1adfdd | -12.74787 | -62.0785 | 2024-10-08 05:25:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e9cd747-2e8b-34b4-bf94-3bde5b956d08 | -12.74771 | -62.27391 | 2024-10-08 05:25:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a89b5403-e1a8-3307-81d4-9b0d4bed6522 | -12.74552 | -62.26631 | 2024-10-08 05:25:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 702d05df-dfbd-3ff4-b48d-03bafa01b08f | -12.74496 | -62.26984 | 2024-10-08 05:25:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 550ed583-7255-3034-bf1d-733e9fb9ea3f | -12.74457 | -62.07795 | 2024-10-08 05:25:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f569f79-04e6-33c0-bff2-810b967e34a0 | -12.81834 | -63.00421 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d092e35c-62aa-36fc-a3e9-d4512a229a4a | -12.81501 | -63.00365 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8cde986f-c57d-3fce-acfe-153071b64420 | -12.70813 | -62.94972 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ffadd20e-6213-3bf2-b093-e7d29a633cf2 | -12.70756 | -62.95332 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d98d9003-076e-398d-bcf1-8581cc2cf334 | -12.70583 | -62.9641 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 47050577-9515-335f-9519-fd8b92fed3de | -12.70422 | -62.95276 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fae515de-69c6-30b0-a50d-cea917a471f3 | -12.70364 | -62.95635 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 46efd6dd-76d1-3ac9-90d0-b44a73e83fe2 | -12.70307 | -62.95995 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 94fb023a-1950-3801-b89a-3c4de54b61b9 | -12.70088 | -62.9522 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c993741c-695d-38dd-a1e9-c2893ab631fe | -12.70042 | -62.93367 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| caa03958-33d6-3f41-a64d-2004abbc16fc | -12.7003 | -62.95579 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86ab7c6d-ec30-3645-b031-f3c51c2b0acd | -12.69973 | -62.95939 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 170d055f-d05d-308a-b01a-b1138c47d542 | -12.69915 | -62.96298 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 095a6e76-342c-3ce4-afea-72ebe820eb1b | -12.69709 | -62.93312 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78e2c1a5-35c7-3aac-b1c1-bd6b2e890820 | -12.69697 | -62.95523 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5668dfe1-092b-34e6-9362-70fbbcc3727c | -12.69651 | -62.93671 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79323e4f-96e1-3ac4-b4f4-2eed5bcb35eb | -12.69639 | -62.95883 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 57836863-8220-35cf-b882-a39d724a5bd7 | -12.69581 | -62.96242 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 073dc202-00dc-35bb-8bd2-b6daf06287cb | -12.69536 | -62.94389 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dfb4d5ee-1665-3d81-b90a-34b7beaa0392 | -12.69478 | -62.94749 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ee64c541-4808-35c5-a8c9-2532ac8c493e | -12.69421 | -62.95108 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 03b8a1a1-73bd-31a5-8ac7-d2461e684f8a | -12.69363 | -62.95468 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 74832fa0-fd53-3a33-a276-bc0d6a5331f8 | -12.69317 | -62.93615 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d03d9d41-9aa8-3603-a202-54afd6c32aa1 | -12.6926 | -62.93974 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2c565ffb-0627-3f3e-885b-422dbfad0128 | -12.69202 | -62.94334 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2038be63-162e-3628-8693-37674a3c19fe | -12.69144 | -62.94693 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 50e82925-60f3-3f73-9749-f86e2d22c9f6 | -12.69087 | -62.95052 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 153fe4eb-496d-37d9-9258-b863ab8805b1 | -12.68065 | -63.07831 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b2dcf455-bde5-3056-be75-f6f5e343c772 | -12.67614 | -63.08497 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc7d2c79-6c26-3f61-9fe0-ee20f79b5019 | -12.67556 | -63.08859 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 44157f14-2907-3c3d-8d7a-550d41e2ff06 | -12.67279 | -63.08441 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f8fd8a1-4171-3cb9-8b12-49f899e51f37 | -12.67221 | -63.08802 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71524d22-0711-348c-a961-e466ddf45282 | -12.66886 | -63.08747 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf56a219-1773-3bab-974a-682deb35efa3 | -12.65373 | -63.09607 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d827ef6b-862c-3845-9567-6656759148b3 | -12.65038 | -63.0955 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d8f1e1ce-1673-3b2a-9337-f51169d017a5 | -12.64703 | -63.09494 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| dfead2cb-2e40-3f46-9914-a94431bf3646 | -12.64368 | -63.09438 | 2024-10-08 05:25:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README128.md)
