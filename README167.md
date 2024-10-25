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

## Dados Diários - Página 167

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f08a06d7-6119-3ca9-9ce5-2b5afb12e3c2 | -6.35882 | -42.97331 | 2024-10-25 16:52:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 7390f5b0-3352-344d-af26-6a23535490b5 | -6.3525 | -43.02184 | 2024-10-25 16:52:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0ebef091-3541-32d5-a960-44c929a503d0 | -6.06955 | -42.66701 | 2024-10-25 16:52:00 | NOAA-21 | SÃO GONÇALO DO PIAUÍ | PIAUÍ | Brasil | 2209807 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 22a79790-506b-32c9-bc55-1211935dddad | -6.04639 | -42.72435 | 2024-10-25 16:52:00 | NOAA-21 | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 8a304a84-2989-316b-9993-db1e80b5b2ef | -6.04548 | -42.71891 | 2024-10-25 16:52:00 | NOAA-21 | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| a6edcc34-0dc5-3bb8-8723-d4cf06348745 | -6.04153 | -42.72523 | 2024-10-25 16:52:00 | NOAA-21 | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| a218591b-4a69-314f-afad-d7f057643e1c | -6.04062 | -42.71979 | 2024-10-25 16:52:00 | NOAA-21 | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| f5c7a6c9-82f8-3901-b1f1-f692f29837de | -6.03668 | -42.72614 | 2024-10-25 16:52:00 | NOAA-21 | SANTO ANTÔNIO DOS MILAGRES | PIAUÍ | Brasil | 2209450 | 22 | 33 | nan | nan | nan | Caatinga | 59.5 |
| 3e98459e-a9b5-3570-8e60-cdfd2e154f44 | -6.0338 | -43.11529 | 2024-10-25 16:52:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 9.1 |
| 9a77e552-ecff-3453-831e-68e8f6ec0cee | -6.01028 | -43.00745 | 2024-10-25 16:52:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 22.5 |
| 67406b09-06ed-3c7f-93ed-7febffaadaba | -6.01024 | -43.00872 | 2024-10-25 16:52:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 26.3 |
| 5594bc46-ea39-30d7-8122-15d055fbc62a | -5.99297 | -42.96382 | 2024-10-25 16:52:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 46f3dfe2-6d9d-3271-8d50-4304595f7f0c | -5.95142 | -43.27899 | 2024-10-25 16:52:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 6.2 |
| c307bd40-bdd8-36cf-87d6-2be106242f8f | -5.94494 | -42.54303 | 2024-10-25 16:52:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 484deb6e-eaa4-37be-8abc-05c1b8e64e72 | -5.91582 | -42.31531 | 2024-10-25 16:52:00 | NOAA-21 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 5dc06eda-671b-331f-b619-da86d7054e0b | -5.9092 | -42.42533 | 2024-10-25 16:52:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 36838372-7252-3f79-a24d-1f355d4c2e68 | -5.90819 | -42.42317 | 2024-10-25 16:52:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 6b3cb9bb-5d6b-382c-a976-3eda31bc4ffe | -5.9038 | -42.99015 | 2024-10-25 16:52:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 001b97ac-cc5a-3a32-8acd-1226f92f8436 | -5.90352 | -42.98736 | 2024-10-25 16:52:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 0356d4da-8722-35ba-bc1f-d4d7469b7fc9 | -5.89872 | -42.424 | 2024-10-25 16:52:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 15.8 |
| a9fec330-d36b-3f07-8449-19674431042a | -5.89841 | -42.78529 | 2024-10-25 16:52:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| 6c802803-6b9c-3b1d-a59b-e6ddf3b074e2 | -5.87395 | -42.64215 | 2024-10-25 16:52:00 | NOAA-21 | ÁGUA BRANCA | PIAUÍ | Brasil | 2200202 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| b96d1776-9df4-37e7-be21-1741cddf7bea | -5.86904 | -42.64299 | 2024-10-25 16:52:00 | NOAA-21 | ÁGUA BRANCA | PIAUÍ | Brasil | 2200202 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| c231f0eb-7dba-3b60-a441-01874f379288 | -5.8166 | -42.73387 | 2024-10-25 16:52:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 45533fc0-ee19-3d00-82db-9a971b7df865 | -5.81174 | -42.73479 | 2024-10-25 16:52:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 7.4 |
| 18629072-4582-3a61-a056-d934b62fbb9d | -5.79989 | -42.75376 | 2024-10-25 16:52:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 13.6 |
| 99c721f2-b5cb-3329-9479-0f1f8aa516fd | -5.7966 | -42.88105 | 2024-10-25 16:52:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 7aeff5d3-1a48-31ec-9dce-c18c4132fe82 | -5.79592 | -42.75996 | 2024-10-25 16:52:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 19.0 |
| 0eed7364-203b-381d-a4af-f8196a661fec | -5.795 | -42.75452 | 2024-10-25 16:52:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 19.0 |
| 204954b5-e900-3706-8c04-7990697cf19a | -5.78124 | -42.64387 | 2024-10-25 16:52:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 19.4 |
| 151fe6d7-a050-3f2b-b2e8-b2534d555cf5 | -5.78035 | -42.63865 | 2024-10-25 16:52:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 09334330-ba0d-39b6-be55-f5242fb80799 | -5.77937 | -42.63287 | 2024-10-25 16:52:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 0cd1b20f-02a2-36ca-9af1-10611f91e59e | -5.77914 | -42.91928 | 2024-10-25 16:52:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| ac726406-78d4-3b3d-94b2-b883ffb3740e | -5.77787 | -42.91661 | 2024-10-25 16:52:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 6a0ef0d7-4890-3b5e-aa69-d8f8267d25a2 | -5.77352 | -42.6282 | 2024-10-25 16:52:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| c3c597b2-5b97-3db5-a809-e0252ea54711 | -5.77213 | -42.6793 | 2024-10-25 16:52:00 | NOAA-21 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 1532e273-3a1e-31c5-a52d-5463d1010ca5 | -5.70369 | -43.14731 | 2024-10-25 16:52:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 65b437b4-276b-37a4-9df0-c05df3ea2ed8 | -5.69742 | -42.48189 | 2024-10-25 16:52:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| b738b160-dad0-3cdd-b1ab-b61c9405ca8b | -5.69664 | -42.48162 | 2024-10-25 16:52:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 9875e96c-733e-39cc-a1d8-972f8d176d4b | -5.69244 | -42.48272 | 2024-10-25 16:52:00 | NOAA-21 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| c3b4330c-0929-3c6e-b126-8470c6f01e93 | -5.68212 | -43.19397 | 2024-10-25 16:52:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 355fff03-8779-36c7-a89e-7b92b486788e | -5.63387 | -42.78464 | 2024-10-25 16:52:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| ac11de1c-9202-35a4-8b2d-686416f53203 | -5.63242 | -42.78945 | 2024-10-25 16:52:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 95cf63a3-3ba9-3988-b375-6e32c05d21e2 | -5.63151 | -42.78416 | 2024-10-25 16:52:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| bcd748b3-f19b-34a8-8628-18c4eb6a82de | -5.62988 | -42.79084 | 2024-10-25 16:52:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 8d9e6263-a0a1-3509-83c1-300a5ce73643 | -5.62901 | -42.78556 | 2024-10-25 16:52:00 | NOAA-21 | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 7b7561e3-e228-3d85-aa43-37ea0c5a79b6 | -5.53589 | -42.93621 | 2024-10-25 16:52:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| def621f9-0334-3b3b-ba84-afc6531e8868 | -5.48157 | -41.96597 | 2024-10-25 16:52:00 | NOAA-21 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 43219fa9-f3c0-39f5-ac02-006b7070e95e | -5.4769 | -41.9698 | 2024-10-25 16:52:00 | NOAA-21 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| bba511e9-e47f-3579-abf2-4f5c32874277 | -5.47638 | -41.96677 | 2024-10-25 16:52:00 | NOAA-21 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 6443ef73-f8d6-3f9d-afbf-040a2a5baa88 | -5.41934 | -42.82547 | 2024-10-25 16:52:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 20.9 |
| 56955c8a-fdaf-3138-a08b-77eabdb300df | -5.41766 | -42.82888 | 2024-10-25 16:52:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 11.2 |
| ca01f5a1-7f1e-33cd-8e2c-4cf9444ad525 | -5.4167 | -42.82334 | 2024-10-25 16:52:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| f110b50a-e336-32cf-9b52-dc7ef5a851ef | -5.38237 | -42.81472 | 2024-10-25 16:52:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 9a163fc9-8df6-3811-98b1-0271d2c38d3b | -5.31256 | -42.98441 | 2024-10-25 16:52:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 4.2 |
| db2f5958-7653-3188-8ad4-e3fde11167c0 | -5.30164 | -42.72628 | 2024-10-25 16:52:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 06b521ec-d322-3774-a0c6-23fd53d362ce | -5.1019 | -42.40236 | 2024-10-25 16:52:00 | NOAA-21 | ALTOS | PIAUÍ | Brasil | 2200400 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| ee6bd8fc-2f19-3a59-a35f-aef13c780c18 | -5.1818 | -42.71859 | 2024-10-25 16:52:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| d66589b9-1960-3e56-a71f-e0a9f25a99d8 | -5.18077 | -42.7208 | 2024-10-25 16:52:00 | NOAA-21 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 15.3 |
| bc70b78a-c1ea-3303-8eab-7ab5518cf24d | -5.17806 | -42.88621 | 2024-10-25 16:52:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b3d7a461-b271-3b94-9c8d-67f274e185d0 | -5.09637 | -43.01508 | 2024-10-25 16:52:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ebbb3fe9-963e-3fd4-a67b-877a8fc0fdde | -6.3411 | -43.53118 | 2024-10-25 16:52:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| daee3bf7-00bb-3971-9bb8-457c51d6e4e2 | -6.31298 | -43.47728 | 2024-10-25 16:52:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f4cbaf39-37b5-354d-bed2-b85ff902f152 | -6.11007 | -43.36376 | 2024-10-25 16:52:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5bc13240-eba7-345f-9f62-619c9970b84e | -6.05621 | -43.46135 | 2024-10-25 16:52:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 4e5a7e02-4b86-37d8-b4b3-ab9e5e79e04b | -5.96692 | -43.37355 | 2024-10-25 16:52:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 20.8 |
| a1f46ce5-0a60-35fb-a395-a041b48b0769 | -5.96454 | -43.37103 | 2024-10-25 16:52:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 35.0 |
| ca780c25-9336-3b9b-8ed5-17adbe5f3e3e | -5.96142 | -43.36926 | 2024-10-25 16:52:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 27.4 |
| e6931fc0-dfaf-3c56-8106-0eacc878fdd3 | -5.95387 | -43.28099 | 2024-10-25 16:52:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 0aa434a2-d98e-3f5d-8e30-b9ab678875ca | -5.67739 | -43.19484 | 2024-10-25 16:52:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 028f080b-3ccb-393a-b1f3-8915338f8097 | -5.99554 | -43.44036 | 2024-10-25 16:52:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ed70eb6d-0918-3408-adec-d9f85b5566c2 | -5.99473 | -43.4356 | 2024-10-25 16:52:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 0ec3a71f-5258-3316-af0a-e59df64f2c99 | -5.93318 | -43.34348 | 2024-10-25 16:52:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 6cc831c7-f32e-3be2-91d5-0b0580720e73 | -5.93235 | -43.33847 | 2024-10-25 16:52:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 1f4abc9f-d61e-3abc-bfd4-91d3b12633af | -5.81006 | -43.42764 | 2024-10-25 16:52:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ce3e9843-861b-38d9-ba2d-15d5b50bac5e | -5.173 | -43.23953 | 2024-10-25 16:52:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0b49dde5-f1ae-3c2b-a804-41ebcd55af55 | -7.99996 | -42.35448 | 2024-10-25 16:52:00 | NOAA-21 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 988d9889-911a-3e3f-9aa9-117122db7444 | -7.89079 | -43.16445 | 2024-10-25 16:52:00 | NOAA-21 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| ff5f09b1-ce93-36b6-83a3-d67bab4bf9d2 | -7.87131 | -43.13214 | 2024-10-25 16:52:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| ce2e3b0a-0dce-3794-a0e4-dbeaa93bd618 | -7.87128 | -43.13392 | 2024-10-25 16:52:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 24909a8a-bfda-3852-919c-a5d2d02452f6 | -6.55615 | -43.21169 | 2024-10-25 16:52:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 6.6 |
| a82dc196-1e29-3e00-9337-4e12253646ef | -6.53818 | -42.69831 | 2024-10-25 16:52:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 27.1 |
| ff9f2b43-c2c3-3f10-b9f4-e3fa0f692d42 | -6.51886 | -43.16171 | 2024-10-25 16:52:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| cd61029a-846d-3362-9865-cd856939773c | -6.50734 | -43.008 | 2024-10-25 16:52:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 986d3507-9b25-3c4d-b518-bbc44de665cc | -6.49752 | -43.03619 | 2024-10-25 16:52:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2087ccf8-7ea9-35d6-9d2a-9431a142f595 | -6.49278 | -43.03696 | 2024-10-25 16:52:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 28.4 |
| 35e85eab-04b8-37c9-afc7-a440d90b037d | -6.44918 | -43.24892 | 2024-10-25 16:52:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1b83801c-5412-3559-be34-86c664f88525 | -6.44835 | -43.24398 | 2024-10-25 16:52:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0e53b393-bbf1-3b37-acf6-40ece9cd55f9 | -6.44452 | -43.24971 | 2024-10-25 16:52:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b7f7def2-31f8-33e4-a0c8-b95a72f55c05 | -6.4437 | -43.24485 | 2024-10-25 16:52:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 641fea2c-c34c-3124-bb2a-ed7c67248ac2 | -6.58086 | -43.58295 | 2024-10-25 16:52:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| d7097014-29a6-3f65-883f-f599d91f9269 | -7.74433 | -42.91932 | 2024-10-25 16:52:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 18.3 |
| 262a80e4-254f-34d8-9c36-d407fc6d00f7 | -7.74348 | -42.91446 | 2024-10-25 16:52:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 18.2 |
| 3607388d-bbc0-301f-99e9-88a7a9522acb | -7.68719 | -43.26795 | 2024-10-25 16:52:00 | NOAA-21 | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| a1f9e1c9-213a-3b57-9284-c67757e74618 | -7.67017 | -42.86728 | 2024-10-25 16:52:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 13.4 |
| 004c7349-218c-3afb-bd54-8f02c5ad5c4e | -7.60017 | -43.03485 | 2024-10-25 16:52:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| edee7c77-c1af-37b2-8503-75a65d9446bb | -7.52722 | -43.07543 | 2024-10-25 16:52:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 3fe65801-9379-373c-b32a-9f3281aa8beb | -7.52638 | -43.0773 | 2024-10-25 16:52:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| c5df9a04-5aaf-3a66-9aeb-995321bb2950 | -7.49888 | -42.9215 | 2024-10-25 16:52:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 651b791e-20fa-3ea0-8bd4-df8b1ce26ed8 | -7.49625 | -42.9202 | 2024-10-25 16:52:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 10.8 |


[Clique aqui para ver as próximas entradas](README168.md)
