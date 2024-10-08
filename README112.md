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

## Dados Diários - Página 112

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cbb9f6a5-9a79-342d-9a57-c9cb334511ee | -19.38584 | -51.70407 | 2024-10-08 05:23:00 | NOAA-20 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d299abbb-b101-370d-9987-5698c8323bb8 | -6.44777 | -49.87834 | 2024-10-08 05:23:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8936dea2-7d9b-34b0-aea6-062074340d63 | -6.44126 | -49.88206 | 2024-10-08 05:23:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9e255b92-f2c8-3c0a-91fd-f8622c2f5e7c | -11.32684 | -51.08352 | 2024-10-08 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c2f60f46-86ac-363f-a238-9f6ab6e5db8e | -11.32545 | -51.34291 | 2024-10-08 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3502866d-dd3f-36d2-8189-08b9686779cb | -11.32427 | -51.33992 | 2024-10-08 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 33ba4191-2663-3db8-b587-11becdca6bdc | -11.32376 | -51.34392 | 2024-10-08 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a6006cd1-99e1-3612-b3d0-2b985e9216b9 | -11.32102 | -51.0828 | 2024-10-08 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3980d4fc-4a08-352e-ac53-d61df13ce795 | -11.31973 | -51.34216 | 2024-10-08 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c3b91ebd-aa9b-36ab-99d4-1f6b7b963a5f | -11.31926 | -51.34617 | 2024-10-08 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 64d8cc02-854c-3ec1-a253-b7427dd1a94e | -11.31754 | -51.34721 | 2024-10-08 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b837b90-8c18-3f82-ac77-9d752264e3a2 | -11.3152 | -51.08207 | 2024-10-08 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e7870d8c-caf0-3308-97b5-e0ea1fc7012c | -11.30508 | -51.06813 | 2024-10-08 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2a13064a-6d8b-38f6-9f05-fe3999a7129c | -11.30458 | -51.07229 | 2024-10-08 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6ab5557d-2797-3ef0-8862-c8a3f2c1b2e4 | -11.30407 | -51.07645 | 2024-10-08 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 716e04eb-1b98-3afb-b975-ac2274e643ba | -11.29925 | -51.06745 | 2024-10-08 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0e4373ea-b343-3df4-add3-13c1ee96d731 | -11.29875 | -51.0716 | 2024-10-08 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0281eee1-5862-32ef-98ef-96028abb050f | -11.29825 | -51.07572 | 2024-10-08 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1d39757b-c75c-3144-be35-b989ce9b86bf | -11.20244 | -51.36911 | 2024-10-08 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4ae2375-ef64-31b0-ade4-d01630d8e588 | -11.20194 | -51.37306 | 2024-10-08 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b1aa9e05-35b1-3bf7-9986-e8ec66d57e35 | -11.19723 | -51.36442 | 2024-10-08 05:23:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 225a48e1-1d2c-38ed-bfc0-ae1065b76ffd | -12.62862 | -52.43623 | 2024-10-08 05:23:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dbf42074-3ee6-3612-a3e9-b3612674164b | -17.77841 | -53.05355 | 2024-10-08 05:23:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8bb7406d-5fee-3eb5-92f0-f9adad50b063 | -17.778 | -53.05739 | 2024-10-08 05:23:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce4f5ca5-5b5e-3780-bda3-be052fe45dee | -17.6699 | -53.02475 | 2024-10-08 05:23:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dce17ce6-a917-3e7f-b0f3-6e4b55d1dd37 | -17.6695 | -53.02857 | 2024-10-08 05:23:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b1624ce4-1793-3cc9-87c4-05746161534e | -17.66435 | -53.0241 | 2024-10-08 05:23:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4e9d4459-b62a-3778-b918-1d06acf20414 | -17.66394 | -53.02798 | 2024-10-08 05:23:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f9939429-002e-3fab-97f3-000ef85b70a2 | -17.66353 | -53.03186 | 2024-10-08 05:23:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4cb39335-81d3-3aa2-a3ab-35316324c301 | -17.65796 | -53.03138 | 2024-10-08 05:23:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a60a0985-bae7-33c1-a99b-6813510a4251 | -17.65755 | -53.03525 | 2024-10-08 05:23:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 00865267-6ab6-37fd-b3af-a143b941cfdd | -17.65197 | -53.03484 | 2024-10-08 05:23:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 658761b7-9e72-3890-9b26-9d696ac9f3ce | -17.65157 | -53.03868 | 2024-10-08 05:23:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5c0ae230-2526-38fd-8ac7-969d2e9b637a | -17.81375 | -53.76458 | 2024-10-08 05:23:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 55cbc7f3-a4da-31cc-b142-b0c207023059 | -17.81334 | -53.76839 | 2024-10-08 05:23:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7393a55c-47f4-3b81-9108-63054ef2fb4a | -17.80921 | -53.75693 | 2024-10-08 05:23:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8bc48f25-1bcf-3300-bc70-5eb1edf323fd | -17.80428 | -53.75278 | 2024-10-08 05:23:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 02eed586-d099-34fe-98a7-98e2563deac2 | -17.80383 | -53.75694 | 2024-10-08 05:23:00 | NOAA-20 | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a8bb1013-cc2e-3107-83fc-5bac88df386a | -18.55189 | -52.63334 | 2024-10-08 05:23:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2872ebf1-0cc6-3d54-a0a6-1694c38392dc | -18.55147 | -52.63753 | 2024-10-08 05:23:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3c5173a7-9ac8-3f2e-a7e3-70f0d0df3350 | -18.55105 | -52.64172 | 2024-10-08 05:23:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1ecbba5b-8238-3590-be03-808fff2eac6e | -18.54572 | -52.6368 | 2024-10-08 05:23:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9f868b29-bd09-3307-a031-276bc21dcdd4 | -18.49656 | -53.44559 | 2024-10-08 05:23:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5f169eba-0004-3be7-84ae-57a6e3aec590 | -18.49617 | -53.44925 | 2024-10-08 05:23:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c338f659-9a76-3deb-ad97-38793ccf7433 | -18.49578 | -53.45291 | 2024-10-08 05:23:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bca63df9-09db-30ca-8f0f-6481ed3db712 | -18.49539 | -53.45659 | 2024-10-08 05:23:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b3f69ef3-2021-39f6-ae7e-d989a9855c77 | -18.495 | -53.46027 | 2024-10-08 05:23:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 0a15d66c-71b9-3257-8b80-19772bdd805f | -18.49461 | -53.46399 | 2024-10-08 05:23:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7b54e718-958d-3d65-b4cd-c7be18fd7026 | -18.49148 | -53.44134 | 2024-10-08 05:23:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 043f054c-32d9-30b8-a6b5-24f6f4103c57 | -18.49108 | -53.44509 | 2024-10-08 05:23:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6036f06c-b049-3a3c-8b0a-858f2005dd06 | -18.49068 | -53.4489 | 2024-10-08 05:23:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 6.7 |
| dedd21a8-26de-3f17-915b-3b9e1db916bc | -18.49027 | -53.45273 | 2024-10-08 05:23:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dde4e7d0-0757-38db-a8ab-98cafd755969 | -18.48988 | -53.45643 | 2024-10-08 05:23:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a9c7a2a5-237b-336c-ae55-359944d041af | -18.4895 | -53.46001 | 2024-10-08 05:23:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 04035e5d-2b59-3159-813d-3813771f0154 | -18.48612 | -53.49193 | 2024-10-08 05:23:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2029eedd-8c42-320f-b87d-98ac950f89e3 | -18.48563 | -53.44432 | 2024-10-08 05:23:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7ca0ab8e-060a-3af0-b72d-5360a4d24d2f | -18.48523 | -53.44815 | 2024-10-08 05:23:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0a29de01-3800-3784-bdc3-6aa6a939ab89 | -18.48482 | -53.45203 | 2024-10-08 05:23:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 34ee50b8-46c4-344c-9fab-f07b27f785be | -18.48442 | -53.45575 | 2024-10-08 05:23:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5e687ace-f8ad-3a14-b8d2-2fe33ea16dbf | -18.48405 | -53.45935 | 2024-10-08 05:23:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6cae1ab4-af35-3fd0-8638-61475709e7cb | -18.48367 | -53.46292 | 2024-10-08 05:23:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c33ad33e-cbb6-39e8-8e3c-c688e8822964 | -18.48066 | -53.49139 | 2024-10-08 05:23:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 139a93b1-7e6b-3996-ab60-2bf3db7bb2e0 | -18.47986 | -53.49892 | 2024-10-08 05:23:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c5c1451a-5e42-313b-872f-5ea24b0ff176 | -18.47948 | -53.50254 | 2024-10-08 05:23:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 15713e72-c7ae-3c1d-aec2-3f9768b70b7c | -18.47443 | -53.49823 | 2024-10-08 05:23:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8bb68c60-ee4d-3b83-b284-e4abb74b8fdd | -6.42075 | -51.70974 | 2024-10-08 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a3373b19-6816-3b73-8507-907d7892e3e3 | -6.42031 | -51.71286 | 2024-10-08 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ba410875-ff4c-3db7-9a36-9737aca5614f | -6.41641 | -51.74083 | 2024-10-08 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9cb4e7e2-b9ea-3f2a-8e3f-3c01c52ff7e7 | -6.41551 | -51.7092 | 2024-10-08 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 683d8134-d5fb-3f21-b779-1622f583085f | -6.41506 | -51.7124 | 2024-10-08 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 677fd9fe-6f94-389f-9ac9-95bca7402a24 | -6.41164 | -51.73699 | 2024-10-08 05:23:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 85596054-efd9-3403-a78e-812648645a8b | -12.63101 | -53.11581 | 2024-10-08 05:23:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 480406e2-db27-3710-a500-98617c5090b2 | -12.63062 | -53.11897 | 2024-10-08 05:23:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77e3c78e-15af-3278-9917-62c993e167ce | -12.63023 | -53.12214 | 2024-10-08 05:23:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6636a708-bbad-39fd-87c1-afb20dd93dcd | -12.62506 | -53.12144 | 2024-10-08 05:23:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a394d9bf-f939-352d-a190-d782b9ba9a7d | -12.62467 | -53.12465 | 2024-10-08 05:23:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| badd32c1-1ff4-3eb4-9891-d2b0b605b8f3 | -12.60361 | -53.12505 | 2024-10-08 05:23:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2c06ad9a-f371-3053-bace-f57f016ad099 | -12.60323 | -53.1282 | 2024-10-08 05:23:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5a598f54-65b5-3ae4-a3db-ae0da0df15c8 | -12.60285 | -53.13137 | 2024-10-08 05:23:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f9b1daf7-d6a6-35ac-9351-3bbab9c467f9 | -12.60214 | -53.12431 | 2024-10-08 05:23:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d3f24dc6-36d8-3175-9681-d3a2454bdd9f | -12.60174 | -53.12746 | 2024-10-08 05:23:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3de76577-04bb-36b0-bb91-dd8c11cfa4f9 | -12.60134 | -53.13062 | 2024-10-08 05:23:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8cb49572-ef1d-300f-914c-8f0bb4c35b13 | -12.60093 | -53.13378 | 2024-10-08 05:23:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3634beb5-864e-3f59-b497-87f2fa7199a7 | -12.60053 | -53.13694 | 2024-10-08 05:23:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f03737ae-6fe0-37c2-a712-6e3f1aff9aa2 | -12.59845 | -53.12432 | 2024-10-08 05:23:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e33d732c-d793-3218-9611-cd25b0e93c7c | -12.59807 | -53.12747 | 2024-10-08 05:23:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 679e4a4e-b428-3f8b-b2a1-ed031ca571c0 | -12.59731 | -53.1338 | 2024-10-08 05:23:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec17d066-cce3-36cd-8941-d44b6d433926 | -12.59658 | -53.12674 | 2024-10-08 05:23:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 285555b2-062d-34d0-bc96-0dba152df458 | -12.48168 | -53.14747 | 2024-10-08 05:23:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8901f14b-05e4-3b9a-8ed0-48ce9418e3cf | -12.47693 | -53.1436 | 2024-10-08 05:23:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69550101-3a1a-39db-b5e4-0c7ea742534f | -12.47652 | -53.1468 | 2024-10-08 05:23:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5ec591db-254b-364e-9af8-679b1d568811 | -12.57785 | -53.0667 | 2024-10-08 05:23:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| e95ba2d9-48ef-3d72-916b-8f79091462c5 | -12.57745 | -53.0699 | 2024-10-08 05:23:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 8c522787-a673-3879-a174-b0b3b25cabc8 | -12.57307 | -53.06274 | 2024-10-08 05:23:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 3c6eb022-acb3-3e88-8e8c-44c6c4de418b | -12.57267 | -53.06598 | 2024-10-08 05:23:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| d40f6e83-d294-3f1d-9f3b-f94b3fef9998 | -12.57226 | -53.06923 | 2024-10-08 05:23:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 70ae1108-5b9a-3c95-ae02-2e0584837083 | -12.56749 | -53.06527 | 2024-10-08 05:23:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5da3ab3e-323a-30eb-8e3a-0acecfca86f7 | -12.56708 | -53.06853 | 2024-10-08 05:23:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 02425079-ce54-310c-9c50-1e6aeb1d0027 | -12.5619 | -53.06784 | 2024-10-08 05:23:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ccafc884-9f01-339f-9347-883329ec5229 | -12.55712 | -53.06386 | 2024-10-08 05:23:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README113.md)
