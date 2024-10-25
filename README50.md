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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6c07e7ff-863e-327b-b230-8c6c0160b335 | -7.06737 | -45.22907 | 2024-10-25 04:38:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3cd36cd9-21ae-35d7-aad6-b315c1a0d442 | -7.0635 | -45.22855 | 2024-10-25 04:38:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8f4a0960-6359-38dc-998e-7c94e69a70cc | -6.84582 | -44.7526 | 2024-10-25 04:38:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a76818cb-3f98-3e16-ab06-39a5505393a8 | -6.84187 | -44.75189 | 2024-10-25 04:38:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 00035255-933b-307c-a2d7-835d102a57e1 | -6.84112 | -44.757 | 2024-10-25 04:38:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0eaeec32-b930-37ff-82a5-d0d94b0612d8 | -6.83718 | -44.7563 | 2024-10-25 04:38:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c78e7724-9e8b-315e-bc46-968ea7871d9c | -6.83249 | -44.76068 | 2024-10-25 04:38:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8265084e-28d9-3618-922f-6cc93d3ec7a2 | -6.60188 | -44.18914 | 2024-10-25 04:38:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3dcb8f6a-4bd2-31db-840c-80ff0e42f1cf | -6.46715 | -44.67355 | 2024-10-25 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0fef0047-870c-3291-9875-d570f5fc40ce | -6.46397 | -44.66783 | 2024-10-25 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9867a6c2-d6c6-3ca3-9296-9b6c77318976 | -6.4632 | -44.6729 | 2024-10-25 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3808de43-d10e-3117-adf3-b5ebfa3fb353 | -6.46244 | -44.678 | 2024-10-25 04:38:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 45b7cc1c-26a8-33f1-8c02-09bb3ed4e89e | -8.79631 | -44.71855 | 2024-10-25 04:38:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33da0884-f384-387c-89ef-b69ad276d255 | -8.78964 | -44.73596 | 2024-10-25 04:38:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 75561357-42cf-3459-8ca8-b0807fd1f5ef | -8.78459 | -44.71317 | 2024-10-25 04:38:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7497bd53-ceec-3252-bc19-cec5fb97ec36 | -8.78407 | -44.71677 | 2024-10-25 04:38:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 37d7bbcd-6572-3c3a-8603-805f60733cd4 | -8.78304 | -44.72397 | 2024-10-25 04:38:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 918cfc8d-7476-3fd1-9c36-a5cc869b0051 | -8.79579 | -44.72215 | 2024-10-25 04:38:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b2357372-0d2a-3090-bc34-a1c48105a3bc | -8.78355 | -44.72037 | 2024-10-25 04:38:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 060c98cf-79b7-38c8-8904-d9fe88b661cf | -9.10934 | -45.50226 | 2024-10-25 04:38:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 92e19845-32be-3233-b42b-0ac17322c31e | -8.79171 | -44.72155 | 2024-10-25 04:38:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 120cda6f-bf21-3a0e-b415-4f9fd1d15ea8 | -8.79119 | -44.72515 | 2024-10-25 04:38:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5bd1dc45-46e5-3e5f-a791-f90b198d787a | -8.79016 | -44.73235 | 2024-10-25 04:38:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 825f0408-22b8-312f-8c5d-9c7da9677711 | -8.77844 | -44.72699 | 2024-10-25 04:38:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 83115298-9905-351a-9dcd-7617fcffd9ee | -8.38873 | -44.47405 | 2024-10-25 04:38:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f69ff846-d7f0-3eb5-a2b9-13ff74f46293 | -8.79527 | -44.72575 | 2024-10-25 04:38:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ffc672eb-d051-38a1-9c0d-668e247f9663 | -8.79068 | -44.72875 | 2024-10-25 04:38:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bfaa80fe-7f77-3385-90c9-e994da59b7cf | -8.78912 | -44.73956 | 2024-10-25 04:38:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7819a778-1c39-305b-8f46-19b3f4eee5b3 | -8.77896 | -44.7234 | 2024-10-25 04:38:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 126de0b3-ea94-3d47-b6d9-0e1cfd258c4d | -8.77793 | -44.73059 | 2024-10-25 04:38:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 310e3a37-0ca8-31f8-aa2c-9b59b1797603 | -8.77745 | -44.70479 | 2024-10-25 04:38:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e11c32c3-2e07-3358-b3ed-05cfe40fce34 | -10.44052 | -44.89443 | 2024-10-25 04:38:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 710b2cd7-0fd7-3409-84ba-404759fff2b3 | -10.44001 | -44.89815 | 2024-10-25 04:38:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 228455e5-70d6-38d5-bdff-991ec80f8bac | -3.47287 | -45.65423 | 2024-10-25 04:38:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df22da98-a471-30f1-85e6-f02b357b7cea | -3.47224 | -45.65834 | 2024-10-25 04:38:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 20bb84fb-3ed0-352b-889d-278b8860c212 | -3.46927 | -45.65367 | 2024-10-25 04:38:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5f037f01-e6e1-340c-a50a-d3019d17f98a | -3.46864 | -45.65779 | 2024-10-25 04:38:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 691823ad-f843-3af7-b559-385fd846f1da | -3.11504 | -45.70747 | 2024-10-25 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd4b61aa-023f-38e7-a0b3-8dc73bcd1bee | -3.11146 | -45.70692 | 2024-10-25 04:38:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b1d36a6a-550c-32df-95db-b3dd89d0b86c | -3.08781 | -45.90856 | 2024-10-25 04:38:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 358cb1b9-222d-3ddc-ad89-42c2eac4ac57 | -4.0987 | -46.0374 | 2024-10-25 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6edf36f4-bf32-311d-8e4d-b2dbeb7745ba | -3.78344 | -45.74416 | 2024-10-25 04:38:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9e13eba0-e02d-3498-a798-eaf4397f7a8a | -3.78281 | -45.74827 | 2024-10-25 04:38:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34d901c3-c402-3179-9e9c-54f99c9d7ca8 | -3.78048 | -45.73951 | 2024-10-25 04:38:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 17.6 |
| f89954ab-cbd4-3f2b-b2b5-69264bbff765 | -3.77985 | -45.74362 | 2024-10-25 04:38:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 11305f7f-58f2-30ae-8f1e-570c06c05752 | -3.77921 | -45.74773 | 2024-10-25 04:38:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 22ba9f61-9fcf-3edd-aa75-bb8fb61bbdcf | -3.77751 | -45.73486 | 2024-10-25 04:38:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fc2108a4-8d44-3928-bcaa-d0e0fa542ad7 | -3.77688 | -45.73896 | 2024-10-25 04:38:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 4f26bde0-fdf1-34ce-bed0-2395253c300d | -3.77625 | -45.74308 | 2024-10-25 04:38:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 796b2e70-c32d-3bc4-8d76-90147286e57e | -3.77562 | -45.74718 | 2024-10-25 04:38:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 298c6844-36ba-3dd9-bc3f-f8a4d8aaa346 | -3.77499 | -45.75129 | 2024-10-25 04:38:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| de06d612-26a3-3d81-9668-d05b30bf2a51 | -3.77391 | -45.73431 | 2024-10-25 04:38:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f9d449c-2c1f-3b72-8627-eff2d7bda63f | -3.77328 | -45.73842 | 2024-10-25 04:38:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 159.8 |
| e221eb27-6cfa-30fa-8e29-49cabd10c718 | -3.77265 | -45.74253 | 2024-10-25 04:38:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 159.8 |
| acabe23c-bbdb-3cf8-b1b1-a4ef16a8ee24 | -3.77202 | -45.74663 | 2024-10-25 04:38:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a45943fb-3fb9-3798-aef0-816d53be07ab | -3.77139 | -45.75074 | 2024-10-25 04:38:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 382631f6-845d-3f7a-b228-17e616709175 | -3.77031 | -45.73376 | 2024-10-25 04:38:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15f03962-49e1-325a-9e41-6a7d731b181e | -3.76968 | -45.73787 | 2024-10-25 04:38:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 159.8 |
| 080af59a-8100-39ad-89dd-25b59b1b7dc8 | -3.76905 | -45.74198 | 2024-10-25 04:38:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 159.8 |
| 8517be1c-e215-34f8-bcd4-2f71d7b8862e | -3.76842 | -45.74608 | 2024-10-25 04:38:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 90caad9a-afef-3473-8f28-82221d99d11c | -3.76779 | -45.75019 | 2024-10-25 04:38:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1f003340-43e5-355f-a887-a3d06ebfc50a | -3.76608 | -45.73731 | 2024-10-25 04:38:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7164b498-e3d3-3e3a-bf4f-592bebb9f6f4 | -3.76545 | -45.74142 | 2024-10-25 04:38:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eca78028-56e4-3889-8c19-6c4db7b6bb8c | -3.76482 | -45.74554 | 2024-10-25 04:38:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 051add1d-f56a-301f-9e17-4f808d58a507 | -3.75965 | -45.80334 | 2024-10-25 04:38:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1e15a77b-6649-3733-8e1f-041ce8dfde93 | -3.75607 | -45.80278 | 2024-10-25 04:38:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4f05af75-0be2-33b8-adba-1cca6623390a | -5.0289 | -44.98888 | 2024-10-25 04:38:00 | NPP-375D | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ad66f446-02f2-395e-b43a-377fd80718be | -4.94586 | -45.73968 | 2024-10-25 04:38:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2d0d5bd8-02e4-3ceb-8d1e-386f31e2f983 | -4.94523 | -45.74386 | 2024-10-25 04:38:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 178b188e-eab1-3da0-a57f-86ff1abfd158 | -4.9448 | -45.54665 | 2024-10-25 04:38:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dfba0a16-9622-370d-a8ac-1c9dcbb3ea6c | -4.87088 | -45.76937 | 2024-10-25 04:38:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 064cee33-8247-3200-b007-65f9ae993d01 | -4.86726 | -45.76876 | 2024-10-25 04:38:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ace922db-6444-3deb-a31b-f1a115de86f9 | -4.86556 | -45.82836 | 2024-10-25 04:38:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c4fed5d-fa1a-3e75-8d51-255cfd06ca43 | -4.85074 | -45.04053 | 2024-10-25 04:38:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8f801e0e-4c0c-3b7b-9373-8e0892feccd2 | -4.84695 | -45.03995 | 2024-10-25 04:38:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3aa7cb0f-472e-3987-86cb-287f8e0f3ff2 | -4.71234 | -45.73334 | 2024-10-25 04:38:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c70c56e-0a66-3889-aecf-f59d173ff338 | -4.69524 | -45.87156 | 2024-10-25 04:38:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 449c4e9e-9edd-3130-ac99-8721e24c86ea | -4.68232 | -45.80811 | 2024-10-25 04:38:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9fd11059-23ca-37a5-ac99-cad39dc85456 | -4.67869 | -45.80761 | 2024-10-25 04:38:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fed377cb-8933-3d57-b294-01151819f34b | -4.65685 | -45.68375 | 2024-10-25 04:38:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d105b2e-b76c-3200-9c6c-5bdc4ccdf67a | -4.6409 | -46.07467 | 2024-10-25 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4acf462d-26c9-3c87-aa13-d6a1864e13f9 | -4.60322 | -45.81664 | 2024-10-25 04:38:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc417a36-2455-3b04-8769-e14e65f274b2 | -4.54959 | -46.03581 | 2024-10-25 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f76b89c-f8b7-32b3-952d-292c1a1debfc | -4.54819 | -46.03499 | 2024-10-25 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 749ed05e-1eaa-3bd4-9307-5a3272092491 | -4.54757 | -46.03906 | 2024-10-25 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46fbf180-ad87-3197-826a-c09e27717173 | -4.546 | -46.03529 | 2024-10-25 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ac9f8332-d9ff-3258-bf71-e7ce97fa0d34 | -4.54537 | -46.03936 | 2024-10-25 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f8aa0926-a907-3205-902d-a7cd1d6113ad | -4.54461 | -46.03445 | 2024-10-25 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 43b472f6-6ef2-3aac-aba7-aa21c303b59d | -4.54399 | -46.03854 | 2024-10-25 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e7f12e7-867b-34ce-9a0c-34251a63b4ee | -4.54243 | -46.03476 | 2024-10-25 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4bfac5ea-58bc-3fdc-b5ab-6d4cf60e3529 | -4.53885 | -46.03421 | 2024-10-25 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d95f6316-5453-3ffe-8ae9-7cf5e4551232 | -4.43282 | -45.78478 | 2024-10-25 04:38:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 808bfda6-2251-3384-820b-3218da5bc6cd | -4.43219 | -45.78892 | 2024-10-25 04:38:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e7d84d6a-077d-3be6-805a-0d8ed8639c3e | -4.42561 | -45.78353 | 2024-10-25 04:38:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9773d7df-0fba-325a-93ee-42d5ac6ac920 | -4.42497 | -45.7877 | 2024-10-25 04:38:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 80bb49e6-076b-3390-96ec-f45b96907760 | -4.422 | -45.78291 | 2024-10-25 04:38:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bfe85c10-bc3f-338b-8a89-9eebb1edfa2f | -4.42137 | -45.78707 | 2024-10-25 04:38:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bdd45527-2fe0-3286-9698-b6437dabac9f | -4.34882 | -45.97369 | 2024-10-25 04:38:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a00b286b-e62e-34f8-8a35-87104a465845 | -6.26124 | -45.83129 | 2024-10-25 04:38:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 47d8ede0-8389-3b66-981b-b25c8a60d2a1 | -6.25097 | -45.43909 | 2024-10-25 04:38:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README51.md)
