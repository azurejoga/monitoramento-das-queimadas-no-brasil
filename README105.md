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

## Dados Diários - Página 105

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 08fda4bb-d864-34af-a490-bca3c516e558 | -12.76287 | -62.26289 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2a7a3153-426d-3d5e-9415-b3c4b34ba365 | -12.76011 | -62.28107 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 49b1e01c-2af5-3d6c-87ad-360d1086e136 | -12.75956 | -62.28471 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2347e343-a592-3150-bd8d-9c0787eac6bb | -12.72404 | -62.23479 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b8f089f2-8cf4-355c-855f-fd74de7cd2e7 | -12.72068 | -62.23426 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a05aefa3-f08c-37e7-a788-820405c14b9b | -12.72012 | -62.23789 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da6e1255-4c29-36c0-b1d1-889f98bc3414 | -12.71901 | -62.24517 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5c848ec1-5666-3500-b717-1251e51dbd59 | -12.71676 | -62.23737 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26c52a93-b70a-35eb-b8c8-93f55b53ca53 | -12.71565 | -62.24464 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ed07112a-db71-3b04-bcd4-6061b35887ac | -12.93279 | -62.72889 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e1064a86-70ae-3855-b64c-44e7fe6353e8 | -12.93244 | -62.53034 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| be031a57-9063-3460-b58b-b4703505c90a | -12.92946 | -62.72836 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7c5af2ee-6c85-372f-942c-d63b396a10fe | -12.92891 | -62.73193 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2435a6e2-604d-37c6-a3ec-a4c3826a6597 | -12.92836 | -62.73551 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f75e7664-d36e-36cd-9d30-f5844ed6b629 | -12.92781 | -62.73908 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd1d82e0-ee76-3660-acfa-8388593f2496 | -12.92235 | -62.50663 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| f373d3bf-cabe-34ef-aacf-955e7f8d6f97 | -12.91901 | -62.5061 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99d47504-86f6-355e-82c6-45397e24dfa6 | -12.91846 | -62.5097 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5ca2f5e-8fcc-3dde-83a7-b1c7c4084eb9 | -12.89164 | -62.51308 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 46b1fcf0-56ea-30fb-99b0-d6d1c703d5d2 | -12.88853 | -62.79498 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d389471-6775-3f4d-9a6c-5b067f198149 | -12.88411 | -62.80158 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4c136c76-4c47-3406-84bb-d2563cacc934 | -12.88023 | -62.80461 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5cc77a7-5708-34ad-aa63-27d8e7901d05 | -12.82603 | -63.00366 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7333e12-dce3-3507-bd07-a004ca1edda9 | -12.82548 | -63.00721 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a04f2b1f-f9d0-32d7-b2a0-0d72468b914f | -12.82381 | -62.99604 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4f3fbfec-3b06-370e-ae88-e15ceb1f04ad | -12.82326 | -62.99958 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c0a58e3b-e178-3bf2-9b60-ec3024a0f721 | -12.8205 | -62.9955 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 337892d5-a543-3be0-99e1-373dc685078f | -12.81663 | -62.99852 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70554075-f6ff-349b-91cf-bd89accd8e2a | -12.81131 | -62.45604 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 08405aad-d6af-3887-a968-4709596b1b42 | -12.7326 | -62.86124 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5bc4c0a3-f56e-3c95-86c7-c1c396cc57a5 | -12.73205 | -62.86479 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eab71882-8a07-3e8e-9efe-d4e6e3805d5e | -12.70227 | -62.96906 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a4445b94-c8e8-31f1-9ace-9f425359c6d1 | -12.70117 | -62.97615 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed711524-c209-3903-94bf-8b9ad368fc23 | -12.69785 | -62.97562 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e5154da-95ed-3a01-9768-5ac858e7c964 | -12.59139 | -62.60889 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db860041-eeeb-3344-9bf4-c1d41ac2fb07 | -12.5891 | -62.57925 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a013893-b3c9-307f-98bf-427776ff2531 | -12.58806 | -62.60836 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2441aff4-c3a2-3507-882c-eb57740c385b | -12.58751 | -62.61193 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 81a63898-8c43-361f-9bbd-417eb65b87ef | -12.58522 | -62.58229 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e67c87f-03c0-3368-a589-0c8259fabe3c | -12.58309 | -62.61855 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ce2cf1af-2663-3bde-863b-dabedec0f14a | -12.58254 | -62.62212 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cf984c03-24b3-399d-8f32-232568f2db85 | -12.57866 | -62.62516 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 83c1ee4a-7e22-373b-b27b-b9746db71935 | -12.57588 | -62.62105 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dbbd3121-7579-3849-b419-9b2605463338 | -12.48755 | -62.99617 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f414213-966d-33fa-ab39-0eebafad76b1 | -12.487 | -62.99971 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 30314715-3d11-36c7-b744-a6e173a9c9ba | -12.48645 | -63.00323 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1c305350-e46f-32c6-a3f2-28f425c98a05 | -12.4859 | -63.00677 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 810b4f82-067b-392e-b993-a5e0e78f37c4 | -12.48535 | -63.0103 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 88e3d8f5-4f93-31cc-ac52-60f31698ae5a | -12.4848 | -63.01383 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f97e4fb9-e717-375c-87cb-a7fd0b5d17f8 | -12.48424 | -62.99564 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a45df32-eab4-339b-9836-1e9a4f6cae73 | -12.48369 | -62.99918 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a622189-c74e-33c4-94e7-7ed48bb3e0fc | -12.48314 | -63.0027 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 764223c6-4bb2-382a-8cc2-8e23cf1e830a | -12.48259 | -63.00623 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 9.6 |
| b38fa972-f7c2-3977-978a-f065de597f9f | -12.48204 | -63.00977 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 36ba61d0-cb96-3cac-80d2-135cf883942f | -12.48149 | -63.0133 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ddcfb0e1-a732-3c36-ab44-fe5e5db8762a | -12.48037 | -62.99865 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1478871f-dc84-3427-b6e6-ed02c5b36437 | -12.47982 | -63.00217 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b395feff-ad2c-31cd-ad11-eccc14045b45 | -12.47927 | -63.0057 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 277a9edf-202a-36e3-80d1-8d72d6d3c374 | -12.47873 | -63.00923 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 9c62cad2-63cd-334c-8b85-f88b265dd088 | -12.47818 | -63.01276 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b28baeb7-4913-31b4-b9fb-65e77daffd7f | -12.47763 | -63.0163 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f327bafe-258d-3db3-be5f-ba4293b36484 | -12.47706 | -62.99811 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0fb2c47d-6c7e-3f84-9a72-78e944d6199b | -12.47651 | -63.00164 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 556b657a-ba25-3198-8b2f-64b7949f6f0c | -12.47541 | -63.0087 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2ed06549-c8eb-3bb5-b96c-fde986c7516f | -12.47486 | -63.01223 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f2b1bbc6-0754-3cc7-9bfd-13f7977eaafe | -12.46712 | -62.99651 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8840c646-cac5-353f-a449-dd51f99ef585 | -12.4638 | -62.99598 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3336648d-5ff7-3085-af46-00633fd1d328 | -12.46104 | -62.99192 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 521b5ffc-e783-30c6-8950-ba917c305265 | -12.46049 | -62.99545 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 946d3644-b1a9-3ef6-9a54-48855aba69ae | -12.45827 | -62.98785 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1e80a9ff-ee43-3cab-9ac1-2d0ed871b50d | -12.45772 | -62.99139 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dbf215cc-087e-3d7e-ad72-5ce20a50b110 | -12.45717 | -62.99492 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 428d3a5e-f758-360d-b206-e4597f8af0e9 | -12.45663 | -62.99844 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11a33ead-b88a-3a1a-aee4-1cd341998961 | -12.4344 | -62.72697 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| d9cdb3fb-4c10-3597-9b3e-3e5ccd03a57c | -12.43107 | -62.72644 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3b4cf0cd-cb67-318d-a2d2-242bb3188fad | -12.43052 | -62.73 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| af8026fd-66f5-37f7-8539-de62c0d00d59 | -12.37655 | -62.9682 | 2024-10-13 05:29:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4fa7083b-e62c-3359-86f6-e5cb960c1d4b | -13.01371 | -62.46932 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 16275fe7-162e-34c6-b8bc-e6366013e6f8 | -13.0126 | -62.47655 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e0d9a1e4-8889-38c5-bb25-496a56d47540 | -13.00925 | -62.47602 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 48f2b733-4eaf-3ac7-b342-e95da09e15f3 | -13.00145 | -62.48222 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 09ddc07a-5786-380e-b5a6-43c03d8b45e8 | -13.00006 | -62.73181 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f2d3ba65-9ecb-3ed2-9632-90a1129f546c | -12.99951 | -62.73539 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fdbd6ca8-200a-39c5-bb83-d381beb26ef1 | -12.99921 | -62.47444 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13456246-9447-39ef-b24a-5ad1f6cdf98b | -12.99866 | -62.47807 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| abacd73d-684e-38a1-94f3-89569edc4289 | -12.9981 | -62.48169 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cdeb69fb-987f-3164-a33e-349c824ec6d8 | -12.99754 | -62.48531 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4ddc9c1-b6e0-3381-a04e-ad241ecfb2c6 | -12.99564 | -62.73844 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 266adab3-a312-3d94-83af-b73704590104 | -12.9934 | -62.73075 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 69e7c7fb-fd78-35e4-b2af-b434cdb44b38 | -12.9918 | -62.76346 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c8214b17-ba50-3ace-8bb2-50354dff20d1 | -12.99144 | -62.50278 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 3c03f4bd-0320-3207-8564-e86d5944a832 | -12.98793 | -62.76651 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 300af865-83a6-38a1-a893-cca790a87774 | -12.98679 | -62.75168 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 18b51ef7-433d-371d-be70-33b1e4f199c7 | -12.98674 | -62.72969 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 11c081f3-f7c0-32d6-902b-75b32593341b | -12.98619 | -62.73326 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b4c56048-bc36-3b4d-adea-666b904faaf1 | -12.98405 | -62.76955 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9af33850-434a-353b-91d1-28260a780391 | -12.98291 | -62.75473 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7e8c77dd-875c-3e02-bc55-b2622a85342b | -12.98286 | -62.73273 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2ceeacc9-6223-3b67-95cf-c9c3b9ba7da3 | -12.97496 | -62.72097 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6adde3e8-f691-3585-8eed-cb83218a00d3 | -12.9744 | -62.72455 | 2024-10-13 05:29:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |


[Clique aqui para ver as próximas entradas](README106.md)
