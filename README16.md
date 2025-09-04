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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d0dfd1f5-4272-3126-8598-7c31a3bc3b5e | -3.20421 | -40.73386 | 2025-09-04 03:34:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d71b0c58-96a2-3492-9011-1866781be4c9 | -5.97996 | -44.14923 | 2025-09-04 03:34:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 513457fa-20da-3335-9ac8-0bae844e50cd | -6.12388 | -44.14648 | 2025-09-04 03:34:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 50c3c973-9ba6-3044-ae96-cbb3a3084e45 | -3.48472 | -40.67435 | 2025-09-04 03:34:00 | NOAA-20 | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1cc7984c-23f8-3d1a-83d5-1dce5cecf6f9 | -5.89144 | -44.35348 | 2025-09-04 03:34:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2988dba3-031f-3d06-9491-024868a9b654 | -5.60341 | -45.02567 | 2025-09-04 03:34:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 9a1d7184-73c2-32dc-8017-b5deae932ccc | -6.22892 | -43.38 | 2025-09-04 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0005223a-3911-3901-922a-269a8b158b68 | -5.97291 | -44.12094 | 2025-09-04 03:34:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4e7d6151-6ff7-3e12-a467-d2a1c4314cb0 | -4.90237 | -41.76138 | 2025-09-04 03:34:00 | NOAA-20 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| af5aff02-1838-37ce-8e9a-3f3e8e5e01e9 | -6.25191 | -43.31396 | 2025-09-04 03:34:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8ab86b98-051e-3e43-8e12-9dabe389a178 | -6.25495 | -42.64687 | 2025-09-04 03:34:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9c8fdc9e-e96d-3d02-a598-145fcacacb03 | -6.2721 | -43.32885 | 2025-09-04 03:34:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 50b9f951-86c7-3f3f-bc2e-4eeb6ed0cf56 | -5.93408 | -43.02742 | 2025-09-04 03:34:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 52274345-129b-3d98-8e5e-3b608b7e841f | -6.21784 | -43.37799 | 2025-09-04 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| be23df69-bcc4-3c03-bd54-052be45d25a4 | -6.16049 | -43.31529 | 2025-09-04 03:34:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 4ac5499b-a585-3b26-8594-175265f1bb2a | -5.68418 | -45.94632 | 2025-09-04 03:34:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 62f61e62-1920-37e7-8a0d-b766b5686d67 | -5.69358 | -45.9415 | 2025-09-04 03:34:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7178c834-8d97-3c11-8e2a-ceda2338ee58 | -6.23349 | -43.53938 | 2025-09-04 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ca5dd330-0cc1-3229-9666-a38c182a12c0 | -5.89219 | -44.34916 | 2025-09-04 03:34:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3fcfe347-683e-39f0-9b17-fa4acdea86f5 | -6.24764 | -43.5571 | 2025-09-04 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d1ca9d38-2936-324e-a567-f57169045128 | -6.22962 | -43.54045 | 2025-09-04 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d082c54d-c880-3b3b-8b4a-f12d571c50a2 | -5.97841 | -43.82376 | 2025-09-04 03:34:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e681759d-12be-3f3d-98db-61e3d2b61230 | -5.84241 | -42.99935 | 2025-09-04 03:34:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| ed275e7d-d885-3f67-a360-e8daf11eb71d | -5.48602 | -45.2288 | 2025-09-04 03:34:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 51ed0019-652e-3d4f-a4f3-891129546ad3 | -6.2934 | -43.59274 | 2025-09-04 03:34:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ce510fe-9e78-31df-97dc-d5a891605b5a | -5.79116 | -43.22614 | 2025-09-04 03:34:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8197010-c3f4-3cd7-948c-7f81fb07a504 | -6.22621 | -42.44106 | 2025-09-04 03:34:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 06fa1c94-3d51-38b8-9655-86b568f2796c | -6.16665 | -43.31718 | 2025-09-04 03:34:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ddc8dc71-3a58-36d8-ac44-8441aa9aa344 | -6.22649 | -43.54607 | 2025-09-04 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f641166e-15a7-3f57-a67a-59d7c5d90653 | -5.89556 | -44.34899 | 2025-09-04 03:34:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a7855c2b-3c5c-318f-8a92-6cc6d6f98163 | -5.68523 | -45.94067 | 2025-09-04 03:34:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 83eafe6e-2adb-328d-b745-dc25e03bd374 | -5.68699 | -45.60529 | 2025-09-04 03:34:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c767455e-d5e2-37a2-bea9-34c639dae486 | -6.17151 | -43.31744 | 2025-09-04 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e70dff49-86a8-3d5d-91d1-4b623c6d4a00 | -6.2905 | -43.31898 | 2025-09-04 03:34:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eff3564c-d1f0-3313-a781-37e732542dce | -6.24338 | -43.54866 | 2025-09-04 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 69710df8-0498-38ca-97f2-c39319ac36ef | -5.76931 | -44.8707 | 2025-09-04 03:34:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7256724f-c961-3f53-aa6f-a6818fed84be | -6.12476 | -42.9474 | 2025-09-04 03:34:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| a38e1856-132e-39ca-8b39-b19f3a1dfa66 | -6.12351 | -42.95437 | 2025-09-04 03:34:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 049ab9b3-da6a-368e-8086-329d5587a65a | -5.69987 | -45.15681 | 2025-09-04 03:34:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0d4be1ae-ad05-3a9f-a4d4-247c5f4eebd0 | -5.83156 | -42.99716 | 2025-09-04 03:34:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7780bc37-a18f-3914-ac5f-1cffe6835953 | -6.17704 | -43.32306 | 2025-09-04 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 86769d09-2bda-37ef-9390-fecfa5a65282 | -6.26793 | -43.50852 | 2025-09-04 03:34:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 78ec0d94-9d20-3259-b2fe-9cb75a7d7abb | -5.98581 | -44.15031 | 2025-09-04 03:34:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7fa053a9-76ab-3d1b-bcd0-451d21007573 | -4.83399 | -42.73492 | 2025-09-04 03:34:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 76109aeb-e496-35b7-a609-c9727b2dbaee | -6.2633 | -43.59899 | 2025-09-04 03:34:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 50fd299e-c962-36dc-a61c-2d7da3c3843a | -6.25743 | -43.31497 | 2025-09-04 03:34:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0e282a7c-1cba-3f2d-9f08-5b8ff1eb348e | -5.38278 | -42.87553 | 2025-09-04 03:34:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| bc4e57d1-60a1-39c0-b139-322d37b565c0 | -3.48459 | -43.33575 | 2025-09-04 03:34:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3d7afcdc-f695-36a5-9ce4-f2b4d589f601 | -6.21404 | -42.44901 | 2025-09-04 03:34:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b1baf9b3-4d01-3ff7-a718-e9d5905e2ac2 | -6.22716 | -43.54238 | 2025-09-04 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f40d652e-5269-3823-966a-1078abb4cd95 | -6.16052 | -43.31965 | 2025-09-04 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cdabb5b7-79e3-3d31-845a-c580ac2165be | -5.48203 | -45.23148 | 2025-09-04 03:34:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bef47d1e-d8f9-3cd4-be54-3eaf8b80471a | -6.29275 | -43.59644 | 2025-09-04 03:34:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 427622a0-78dd-3946-8a45-d3f1e665a35e | -4.83279 | -42.74194 | 2025-09-04 03:34:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a990964d-c687-3b28-bbff-981ca85e2303 | -5.69527 | -45.40333 | 2025-09-04 03:34:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5fc8c94b-545a-3e29-b532-2fe04265289c | -6.22424 | -43.55848 | 2025-09-04 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5548568a-35be-3c15-a3bf-678bd03646e2 | -5.74613 | -45.5407 | 2025-09-04 03:34:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| abf70c7f-eb61-3f98-996d-3379c843485f | -6.15919 | -43.32243 | 2025-09-04 03:34:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 51e8e1ed-1a46-3593-987b-cba9a8748948 | -6.21051 | -41.8039 | 2025-09-04 03:34:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 512711f7-8d4f-3aeb-8867-12178738a766 | -5.68601 | -45.94597 | 2025-09-04 03:34:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 58733918-e1f6-3589-9402-87fd9c434abd | -5.70526 | -45.16283 | 2025-09-04 03:34:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f30dbaeb-c8ca-3613-8118-11806065dbe5 | -5.97724 | -43.82373 | 2025-09-04 03:34:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e200e49c-8856-39b9-ba4d-15aab81b88dd | -6.2102 | -41.80478 | 2025-09-04 03:34:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8d4b783f-8e72-37dd-b1cd-34bb6c7b9afd | -8.05418 | -44.14171 | 2025-09-04 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce42cb18-6079-3129-aecd-98143235ccdf | -8.89513 | -45.859 | 2025-09-04 03:36:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 8d912940-47df-31a1-b8e9-019aec85c216 | -8.43435 | -45.05681 | 2025-09-04 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 39a503c9-f804-3d8c-b421-54308d61bde6 | -11.96139 | -45.78059 | 2025-09-04 03:36:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 882d7f6c-ff5b-355f-8c6a-8c8cfa94fd88 | -6.33495 | -45.64629 | 2025-09-04 03:36:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c6b321e9-01eb-3f09-add9-910b439f5ffd | -9.81645 | -47.81406 | 2025-09-04 03:36:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a09a1f9-ee18-32b0-94e6-0acd4558aeca | -9.47757 | -47.61674 | 2025-09-04 03:36:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c3252ed7-3ad4-314f-8cef-b3982aefb26c | -9.03655 | -47.01504 | 2025-09-04 03:36:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7df7677f-0821-362f-a932-268cff41c0f9 | -11.9009 | -46.66263 | 2025-09-04 03:36:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 125c0f58-0873-3232-ba73-41091591581a | -6.28284 | -43.85238 | 2025-09-04 03:36:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a420f38-f116-38de-baa8-a0b182bbc8b6 | -8.0149 | -44.78427 | 2025-09-04 03:36:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4ee0c450-4d12-37d2-ac53-171eb35b483b | -11.05022 | -45.40996 | 2025-09-04 03:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dfa6a085-fd47-35d5-9648-0ee61755fecd | -7.54881 | -45.72042 | 2025-09-04 03:36:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f6d69e96-c813-3e23-8dca-5e59072a4a8d | -6.88581 | -45.56307 | 2025-09-04 03:36:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 244244b0-a8ba-3810-8152-29dd456591a9 | -8.06687 | -45.35636 | 2025-09-04 03:36:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 44868adc-9f24-347e-85c2-725a0b970f6b | -8.03091 | -44.14119 | 2025-09-04 03:36:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e995c999-6aa1-3b6c-b0bb-8d1c41da1678 | -6.49182 | -43.07772 | 2025-09-04 03:36:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5d2aedb3-4e5d-31b9-8ecb-d61d55b27eba | -6.86847 | -45.58636 | 2025-09-04 03:36:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 1d051f64-cf79-394b-b5dd-04b367fef716 | -11.03722 | -45.13685 | 2025-09-04 03:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 771b8f0b-5c79-3a95-84d6-01e3e6f5d3e0 | -9.63877 | -46.12742 | 2025-09-04 03:36:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e92d2c20-5b4e-3834-bac9-8fbcea616f6b | -10.0561 | -46.22628 | 2025-09-04 03:36:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9213f790-bc40-3cca-9ded-b4b9e77d8ba4 | -6.78421 | -44.09494 | 2025-09-04 03:36:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| c106b76b-60ac-3c2b-8cc0-e0877cd1e663 | -6.88526 | -44.88065 | 2025-09-04 03:36:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 43fd67e2-2e2a-3f0c-b6f8-d68acb2c195d | -6.73397 | -42.25239 | 2025-09-04 03:36:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 88d46229-fa95-32a7-9ce3-1e59b74ec58f | -9.64148 | -46.12478 | 2025-09-04 03:36:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 51173c7e-fdc0-38ae-9f9b-bbbe4bec7b2d | -6.78522 | -44.45291 | 2025-09-04 03:36:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8054ea35-cf95-3da1-a031-ddd1a7bc28ed | -6.02481 | -46.67444 | 2025-09-04 03:36:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2f118a8c-6025-3fb8-87df-afa3ee53b27f | -6.87177 | -45.19556 | 2025-09-04 03:36:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d36c0d40-2c1d-3962-939d-d6dadce9d7aa | -8.07578 | -45.34399 | 2025-09-04 03:36:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c067a3e4-e113-3586-9c2c-da12be43d9b0 | -9.49844 | -43.16466 | 2025-09-04 03:36:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 632bda32-6ea9-3c92-b345-f25dce1a3c07 | -6.87372 | -45.55803 | 2025-09-04 03:36:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 3791d59e-6460-3e18-8cc7-2e5e216b31f7 | -6.30167 | -44.15186 | 2025-09-04 03:36:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 1afe9d6d-cdfc-3882-a251-8259566d439d | -8.07393 | -45.35379 | 2025-09-04 03:36:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 82bbd528-fc21-32dc-aed8-2f4653d11edf | -6.02712 | -46.66197 | 2025-09-04 03:36:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b7f33b60-c6ad-3bae-b047-f28fa9c0e5de | -11.04526 | -45.40435 | 2025-09-04 03:36:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 971b3888-52c6-3628-bea6-a7f9aed3d142 | -11.12786 | -44.64099 | 2025-09-04 03:36:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ac6905c9-0360-3fc5-a981-49e6d3ede583 | -8.01408 | -44.78876 | 2025-09-04 03:36:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README17.md)
