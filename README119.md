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

## Dados Diários - Página 119

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 85627dc9-660a-32a0-9900-d513027e0fb9 | -12.98396 | -53.5055 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46a80d1f-cf8e-36db-bfb4-c88952cf7a02 | -12.95941 | -53.49615 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad166d37-ddc2-39e5-9cef-146912f52813 | -12.95904 | -53.49914 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1dae63ed-f991-37ca-9440-fa1fd97b7ce3 | -12.95867 | -53.50212 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c48a85a9-3dc6-3790-9f7e-b06e9eda6bcf | -12.9583 | -53.5051 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 825817dd-a3c8-3791-a738-2f2a012bf136 | -12.95399 | -53.49846 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef50e2c4-68a9-3b9f-a9c4-e106105a2603 | -12.95362 | -53.50143 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8242c43-1a83-3dd1-8532-aa64554e7400 | -12.95324 | -53.50443 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b8c8287b-6ab6-3c9c-9d1d-b1f8458ba191 | -12.95288 | -53.5074 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e6f5c17d-fab8-37a9-8d97-0c7210d376b4 | -12.94893 | -53.49773 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a97e215f-a5dc-32bb-84f1-69670bb240c6 | -12.94856 | -53.50072 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2e017cca-13a7-3471-8cb4-cb70da887d4f | -12.94819 | -53.50372 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ba79b8ba-3f75-3403-8622-262561a3241b | -12.94782 | -53.50671 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 02c45dd8-0e3a-315a-bf42-84bb9e450fb5 | -12.89452 | -53.49001 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 128a55ff-f889-3e93-a8ac-690c72ac9631 | -12.89414 | -53.49298 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 01e8266f-a272-3d9b-8010-66c561c26791 | -12.89357 | -53.49744 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b13dbab4-1220-382e-b6ff-59a5575d0b4e | -12.89282 | -53.50333 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d042bc14-1390-33a1-b56d-c7772f765a74 | -12.88852 | -53.49673 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d7f38e3-674c-3ad8-a4c9-6ba3d8945958 | -12.88777 | -53.50262 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79ae9ee9-ba65-3755-846a-6b343e41762d | -12.88272 | -53.50193 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b2afaec-e3b6-3e78-a2e1-453bae9b30fe | -12.88197 | -53.50785 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 07e29575-b1b2-3e13-9d70-dda90f8cab7a | -12.87766 | -53.50127 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da1c3b16-f64e-3fb3-ad0d-8c56ed81d6da | -12.87692 | -53.50714 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0b6b9183-bdd9-3c73-80ff-39c2b829fde6 | -12.8726 | -53.50064 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2cbfa543-2aa2-3efc-a4c2-bf38eda13b8d | -12.87187 | -53.50649 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 019b2377-a499-3acc-bcf8-8f3629139321 | -12.86681 | -53.50588 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee4f6972-6206-3ac9-b688-9cc3867dfebc | -12.86175 | -53.50528 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 29eb7b1c-4868-3ca2-adee-d3949c799f46 | -12.85669 | -53.50463 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 512884e4-d354-3a37-b74f-c2ca7c984bfd | -12.83577 | -53.50779 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6f2b75e3-288b-3f1e-b1f0-88166eae64c5 | -12.83145 | -53.50121 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f92fa580-c01e-3ef3-a4e0-b1b22ecdf239 | -12.83072 | -53.5071 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 98ffe604-237c-3172-911a-5f49f5d2df3a | -12.82786 | -53.48863 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7bff66e8-2f46-33b6-8fa2-0d9c965b1e57 | -12.82713 | -53.49458 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7c041275-87f0-396f-bf57-7ffa6e13a559 | -12.8264 | -53.5005 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 08088729-337d-3bc5-8739-db4e0574d73e | -12.82567 | -53.50639 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3587a436-64a9-3b40-9b6a-5ca0d1671304 | -12.82454 | -53.48792 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4fa9eda8-7259-3506-a939-e97e03268e8a | -12.82376 | -53.49386 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 430a01e5-f9a6-3e33-9837-97f1422a1dc5 | -12.82372 | -53.48046 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 91501549-5c02-3d91-96f1-0caf4447b70c | -12.82335 | -53.48344 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c1d84354-00c7-32d0-b7bb-4973203aa010 | -12.82299 | -53.49977 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4130580f-51f6-3ac8-a91e-4723b7877321 | -12.82281 | -53.48791 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 20c78e75-0e67-3757-a832-e1271966fef1 | -12.82223 | -53.50566 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 11ead7ca-0544-3e8f-87d2-d8842ed90f4a | -12.82208 | -53.49386 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c574538b-e7aa-32f8-a657-fd9de96eee3d | -12.82135 | -53.49979 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d91691af-6c27-3fea-8aa6-07af35337fbb | -12.82063 | -53.50568 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2b78a4cc-9858-30ee-94a9-cf06d51b7687 | -12.81949 | -53.4872 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ef0af98a-c8b3-34ea-b2fa-1164b9c48c7f | -12.81872 | -53.49314 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f9e360d3-206e-3a24-bd00-13264b7e09f8 | -12.81795 | -53.49905 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 75e8d893-6cf0-3755-bfeb-5e17a675825c | -12.81776 | -53.48717 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 27ce7d69-296d-39b2-8899-eea681b26755 | -12.81718 | -53.50494 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9d242a64-27ad-3488-bbb1-a5164bceb872 | -12.81703 | -53.49312 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0eb71f1c-9a55-3e52-8d7a-fbedb921cd53 | -12.81631 | -53.49905 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8288216c-6aaf-3422-9476-f213b2f61b7d | -12.81559 | -53.50495 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4b47a0c5-5a3e-36f1-ac3e-b15a1831011d | -12.81368 | -53.4924 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f6d69d0b-2c2c-3045-96aa-be12888ad530 | -12.81291 | -53.49832 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0efea280-5dd0-33ca-8b15-f1d2d7f29193 | -12.81215 | -53.50422 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 075adb86-5851-3da2-a927-3cf13ccebf5b | -12.81199 | -53.49237 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c50559e5-b4b6-3cd7-8886-0a19599070f8 | -12.81127 | -53.49831 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| de7e3aa5-8bee-3c4d-afe2-2a16a87ff2a3 | -12.81055 | -53.50422 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1e5761ad-19dd-3f3a-af0e-e8a86474c80f | -12.80864 | -53.49165 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9d51ed98-fb1d-37c9-8652-c234b01eaf68 | -12.80787 | -53.49757 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| de2272e8-8ce6-30d0-b4ad-4bc87d32cf37 | -12.80711 | -53.50348 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| fa3c6a29-b30b-317e-905b-2f5a2b99feaf | -12.80623 | -53.49754 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| bab35e75-2199-3e23-abce-9cc7fd1ba6d4 | -12.80551 | -53.50346 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| d59103fd-8fa4-3bd5-a82f-17ad0b33fd9a | -12.80207 | -53.50274 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18186069-b071-3eff-9103-27dcb3949905 | -12.64064 | -53.10805 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b8b951c4-6840-341b-830b-41ae54f8af24 | -12.64002 | -53.10666 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82d0fa5e-b9f7-309c-87d0-4335d28e16d9 | -12.63962 | -53.10978 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9eedc02f-3512-3118-b20a-f086bba66612 | -12.63547 | -53.10738 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32e98418-b145-3b5e-bdd4-5a63491ff991 | -12.63444 | -53.1091 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f5da8e3-b70d-39c0-9213-ef689c11ceba | -12.59139 | -53.07489 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d37a169f-caff-3870-87d0-1dba9815eae2 | -12.58622 | -53.07417 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 58cd6abc-ca26-3488-9260-c0ef995d3709 | -12.58143 | -53.07031 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1d114e89-a100-3768-b06e-b7f752fc86ed | -12.57664 | -53.06645 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0bd304fa-0b7c-3750-b833-1cc7784368cc | -12.57625 | -53.06962 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68ada525-5c5b-3a87-8359-c2774222bd2a | -12.57146 | -53.06571 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a135d63b-ff8b-34ae-acae-7cb87e4d377a | -12.56949 | -53.08173 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 91646ee8-745c-3a66-b835-5b78a4c868e5 | -12.5691 | -53.08489 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dd264f48-73ad-3889-bcef-b8d5671c92ea | -12.56872 | -53.08804 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f03b1833-9c82-37b9-98a1-d877d98089fd | -12.56628 | -53.06498 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d8fbb675-191a-39f8-a4f1-089a9a22bb68 | -12.56509 | -53.07467 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 46994bb1-d2e0-3919-b20b-18fc6f28f23b | -12.5647 | -53.07787 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68556b51-7484-33b8-a85a-7a5077bfe9d3 | -12.56431 | -53.08104 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a65d4dd2-3e2b-3428-bec5-495f6e0ee32d | -12.56393 | -53.0842 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1dbc547e-1b97-3313-bf60-f8e7c03c8e14 | -12.98865 | -53.50916 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d602fa97-1c9d-384a-ade3-3ebe0f4b42cc | -12.98827 | -53.51214 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 30d556d0-ea3f-3783-aba4-261caff1c1aa | -12.98359 | -53.50848 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c4f2ddfc-08f5-3a56-b82f-72a459d0330d | -12.9718 | -53.52044 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f846cdff-2d01-3685-bc3f-3b9d059390ce | -12.96749 | -53.51388 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9c82a42e-8965-34ff-9ba6-fe6be6a8fb01 | -12.96675 | -53.51978 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6cb3ce29-96fc-3b62-8134-8d0ba91a114e | -12.96243 | -53.51321 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 37cf5e44-dc53-3de4-9a06-432de1d1a308 | -12.96169 | -53.51913 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 45bd1b45-7298-3286-9a6a-d380f8d26199 | -12.95738 | -53.51254 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| eed4dcd6-eff3-3d86-9603-c3e0693452d7 | -12.95664 | -53.51845 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6bfe30d9-dce8-3146-a96a-b2736b9b6fad | -12.95232 | -53.51187 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d61bf2c6-3cb3-3b92-8e7d-90e71325d68e | -12.95159 | -53.51777 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b055c61f-b194-35f6-a725-420bd37142c5 | -12.94727 | -53.51118 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3a4308ce-a7f6-33e3-9f01-08247ac3108a | -12.94654 | -53.51708 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f2b10964-840f-317e-9bc4-2e785c3e5bdb | -12.89206 | -53.50929 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bb58a598-43b5-3907-86bc-60e95b6df98d | -12.8913 | -53.51525 | 2024-10-12 05:25:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README120.md)
