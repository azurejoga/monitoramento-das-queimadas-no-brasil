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

## Dados Diários - Página 123

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 96c2f4fb-2ecd-3b84-b587-886d04f9da18 | -16.42271 | -57.36467 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| d4413a0d-f6a3-3055-9a3c-15d55cc204c0 | -16.42002 | -57.35606 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| efaaec54-7ed7-383b-b0da-2d16cb36337b | -16.4193 | -57.35995 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 35ffe9af-97e9-3758-8edd-d9c628b83d70 | -16.41858 | -57.36383 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 61ee416c-bfa1-341f-9645-7d54c0665627 | -16.41445 | -57.363 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 92bf739a-76f7-3019-80dd-834ccbe5ae32 | -16.41425 | -57.3871 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 4f3de7e6-13c2-377a-92db-eb065720e3f8 | -16.41033 | -57.36216 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| c8a604ca-bc61-3a91-959e-9069f2b6ac8d | -16.4062 | -57.36132 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| fe43dd7c-6bd1-364f-b718-902f2519030d | -16.40281 | -57.35658 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| c2d088c2-ad80-3b0a-962c-0763d27e472a | -16.0699 | -57.5281 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2b7cd497-ae71-37af-863c-942f2d3bd42d | -16.06911 | -57.53238 | 2024-10-05 04:40:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d72d5b8f-d893-300a-9a04-f48abef5dbe1 | -15.57839 | -57.45382 | 2024-10-05 04:40:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6c372f2f-bcf8-30cb-935c-b32ddd757dc1 | -15.57418 | -57.45297 | 2024-10-05 04:40:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cd8ed647-a1c2-36ec-b25f-3019a01f1e8e | -12.63259 | -63.11805 | 2024-10-05 04:40:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 81b0a3e9-9018-35f3-8de3-15ba6fbb48d5 | -11.98867 | -63.52848 | 2024-10-05 04:40:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fc720404-a137-3446-bd16-a1b6d740e8b9 | -11.98744 | -63.53447 | 2024-10-05 04:40:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c5ebe60b-06f7-3e72-a16b-39ee3a21759e | -11.98092 | -63.53275 | 2024-10-05 04:40:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e4763cba-9280-3cc3-9806-2212b7da0a09 | -17.06281 | -56.80445 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 2e43ac2e-b879-3993-a5c0-cf80c3408ebe | -17.05195 | -56.79679 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 9321a358-57dc-3346-941d-91370a14c1ad | -17.048 | -56.79601 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| ffdfbf1a-f0c0-3a92-8f1b-a05935e101c9 | -17.04557 | -56.79428 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| e6f014f9-349a-3aae-9c50-7e0a389a0dfd | -17.04162 | -56.7935 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| fe5ccbfc-4739-3b0d-9712-aff76855286b | -17.04011 | -56.79445 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| b5f3fe67-51d2-31fb-af28-c4c0bf46ea9a | -17.03768 | -56.79271 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| eddb49b7-6c0a-3b31-a588-8e8994de8eaf | -17.03674 | -56.798 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 8c85d8f9-12d1-36f5-8939-d68ef213428d | -17.03616 | -56.79367 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 1498bae2-a374-3f12-874a-b2d113901ced | -17.03518 | -56.79895 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| a97b5cf5-40a5-358f-9934-930c4de838b1 | -17.03373 | -56.79192 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 87f99fd8-407a-39c9-877f-f59a03fc904a | -17.0332 | -56.78761 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 1f80e53d-d117-3d3c-ac1a-5204d52e9195 | -17.03279 | -56.79722 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 6bb85642-9c9d-38d6-9488-feabc2b482fe | -17.03222 | -56.79288 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 20cdb270-5a58-3736-a50f-f22c4d893b9d | -17.03124 | -56.79817 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.8 |
| ef886a4b-f851-3349-9e91-11b65cfa26f4 | -17.02978 | -56.79114 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.8 |
| 62bb5683-1326-35e4-8564-54649243ef19 | -17.02925 | -56.78683 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| bb3ecc0e-ece5-3122-bc99-19a38656999a | -17.02884 | -56.79643 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.8 |
| c1b0ae41-9955-381e-94d9-f23e0f586b1d | -17.02827 | -56.7921 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| ccb16b6b-f25b-37b4-8f7d-fd9fc20ebb96 | -17.02729 | -56.79739 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 16.8 |
| b5604944-2962-332b-8d38-cc1cdc0797f1 | -17.02584 | -56.79035 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.8 |
| 6a0c3ef1-c3a0-3060-842d-23da37be86c0 | -17.02489 | -56.79564 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.8 |
| 581c1bba-1d7a-3b27-9bcb-da20bcd2185b | -17.02189 | -56.78956 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 27.2 |
| da0e455b-17c3-328a-9809-b73fac993fe3 | -17.02094 | -56.79486 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 27.2 |
| 944237d0-fab7-3e03-9932-f33069cb3fef | -17.01795 | -56.78878 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 27.2 |
| a8505ec4-a855-3aed-b11b-fa89e00506be | -17.01699 | -56.79407 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 27.2 |
| 309aef90-5694-320d-945d-ac3e3092faba | -17.014 | -56.78799 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.8 |
| 6869335d-41e0-361a-bd0c-429fbf4060fd | -17.01305 | -56.79328 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.8 |
| 04a1ee53-f5a2-3a7b-acb0-6898c1970a26 | -17.01005 | -56.7872 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.8 |
| 77c2c893-00ff-3892-bb16-7c292fc789cd | -17.0091 | -56.79249 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.8 |
| 8d14da91-25e1-3af2-a011-c465a30c45d1 | -17.00678 | -56.73738 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.0 |
| 649aa925-fb95-392c-8b3b-d4957525ab8d | -17.00583 | -56.74265 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| c8ae00a2-21b5-38a5-b87f-d8c03080c2a8 | -17.0019 | -56.74187 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 0b0da4cd-afbc-3a0c-b1ef-6ee359df5fca | -16.99891 | -56.73582 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 00ac1c1c-3bfc-3dc6-95b9-68ad17b86eda | -16.99796 | -56.74109 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 5bf5ba78-1e16-3762-9145-a993adf6830a | -16.99498 | -56.73505 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.6 |
| 0e88a961-8221-3e3f-a6a5-37a81e932ddb | -16.99402 | -56.7403 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 1691d644-4ffa-3a2c-8c87-42fe06d3f6b6 | -16.99104 | -56.73426 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 52cb3867-ecb9-399a-93f7-72498bfbb46d | -16.99009 | -56.73952 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 1eef17c6-d78a-316e-abaa-12276589ca72 | -16.98913 | -56.74479 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| c95def59-01c1-32bb-a82e-6c7d4f638abe | -17.15783 | -56.96988 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| cc4a658b-4cad-36ca-9a67-86f6c6e96299 | -17.15451 | -56.96552 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 7bef4c0f-c66d-3e9f-8c02-295157c0e173 | -17.15385 | -56.9691 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 060a0ad4-2d57-3116-98f5-58faef40d075 | -17.15053 | -56.96472 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 2da04f91-d4e2-3c27-8ee7-b5e16762e1ae | -17.14516 | -56.75534 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 1d32f2ca-edf6-36ec-ad40-93c62e0811e0 | -17.14422 | -56.76059 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 3f8e0c6f-2aaa-31a8-b457-f18af5bc044a | -17.14123 | -56.75455 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 019abea7-d098-3023-9e52-1dad5256f80f | -17.12063 | -56.75588 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 35405de9-43a5-3854-a4f2-968c90a35d98 | -17.11968 | -56.76113 | 2024-10-05 04:40:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| cf842c44-0072-396d-8bf9-7103125442fc | -18.69858 | -57.29285 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.6 |
| 8092f0f9-d0fa-3a95-b0f2-d1ba4f8017ed | -18.69845 | -57.30606 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| ec7618d1-ce9c-33df-9621-336a60816d95 | -18.69751 | -57.28915 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 322ede75-9291-3ded-b759-bceb9e5d9fe7 | -18.69462 | -57.29204 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.6 |
| 04b870e4-9585-3f8d-a3d7-cd4104a2adaf | -18.69365 | -57.29741 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 959ca6fc-dfb4-3eea-9e6c-f7efda96fb31 | -18.68969 | -57.2966 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 7642b7ea-bcbd-35c5-9eb2-83468c9dae2c | -18.68275 | -57.28959 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 4e685f9f-a248-3606-9661-4ce46e3275b8 | -18.67977 | -57.2834 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 73f529f9-154c-3a31-ac9e-9e0042a17d6a | -18.67967 | -57.29665 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 499e76af-5f9d-316e-a8c4-719332889eab | -18.67879 | -57.28878 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 59626ca8-9794-3751-b851-8b04868c91b3 | -18.66594 | -57.29171 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| ac4bf004-de1b-3841-be68-0d7878375b67 | -18.66492 | -57.27477 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.6 |
| 9544ad2b-2e07-32a7-ad1f-a31f60d28375 | -18.66296 | -57.28552 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.1 |
| 08ffc5c3-35bf-3c00-844f-7e985bc0c69e | -18.65999 | -57.27933 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.7 |
| 659729ea-ebc1-3526-b742-95ab66bcda03 | -18.65504 | -57.28389 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.7 |
| da1bde71-7907-369b-8182-309fee58efe0 | -18.8888 | -57.72201 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 938f8faf-8c0d-3654-bb5a-be142034da8e | -18.70046 | -57.29532 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.1 |
| f56890fe-1052-32e0-b57c-71e7eda85320 | -18.69656 | -57.28128 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| a93dc327-af9d-3fe3-ba36-d443a44b1cfa | -18.69356 | -57.28834 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.2 |
| c1f439d1-d14b-3fc2-a9e9-0fb7287d9b7e | -18.69061 | -57.28217 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.2 |
| eb06e06b-fc93-34db-9ac5-fedf55adf5a3 | -18.6896 | -57.28753 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 33507c6c-535c-32e8-9340-83a02d3ea439 | -18.68843 | -57.33759 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b952d25d-5101-3afb-bb14-f7142aa3c22d | -18.68372 | -57.28421 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 731e77a1-1559-3a87-87bb-3d88de20ef77 | -18.68169 | -57.28591 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 378030b2-d03b-3d54-b699-2bd6f9f47c66 | -18.68074 | -57.27803 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.5 |
| 2cd22e3c-e76e-3a14-b78c-c1d2a09d5d9e | -18.67781 | -57.29416 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| b88869ad-30b9-3bb8-bbe5-496628dba408 | -18.66394 | -57.28014 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.1 |
| cfa5fc1a-0e4f-35c6-9687-413d17a40414 | -18.65802 | -57.29008 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 41e703cd-15f2-31ff-88a1-4848ac0baa77 | -18.65603 | -57.27852 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 23.7 |
| 3fef3e78-296b-3c2c-8245-fe0fc563c85f | -18.65207 | -57.27771 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| c6c5fe2b-0234-3758-97a6-80ecddb05686 | -18.65109 | -57.28308 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 3ee21ff8-88ec-33a0-9943-451f92827503 | -19.10578 | -57.4835 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 49ef9183-69fb-346d-a592-9a057f2c240b | -18.69761 | -57.29823 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.7 |
| 695fa139-6c91-37f4-8db5-9409a1f8a7ff | -18.69651 | -57.29452 | 2024-10-05 04:40:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.1 |


[Clique aqui para ver as próximas entradas](README124.md)
