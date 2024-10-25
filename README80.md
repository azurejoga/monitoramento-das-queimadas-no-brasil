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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f718582-faa9-3520-9e7e-82fcad49a970 | 1.57194 | -55.6521 | 2024-10-25 04:59:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7cf723e9-f8c4-3b89-90f2-f1071b5c0cac | -2.74945 | -67.02716 | 2024-10-25 05:01:00 | NOAA-20 | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69672eab-de78-30bd-9ccd-1df45318adff | -2.74853 | -67.03252 | 2024-10-25 05:01:00 | NOAA-20 | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d99f840-d76b-3a2e-b1fd-f27a742c52fe | -2.74794 | -67.03114 | 2024-10-25 05:01:00 | NOAA-20 | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8cb15f08-943a-3121-9a02-e9afee66f5cb | -2.74305 | -67.02589 | 2024-10-25 05:01:00 | NOAA-20 | JUTAÍ | AMAZONAS | Brasil | 1302306 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a0149958-9bae-3038-87e9-dc5d658e4a4d | -4.64991 | -42.79829 | 2024-10-25 05:01:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| aadfb06b-e892-3be4-8105-31e83094a83d | -5.52599 | -42.2342 | 2024-10-25 05:01:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| d39cbe6a-d06c-39b0-90fb-de58e07a18a1 | -5.52516 | -42.2401 | 2024-10-25 05:01:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 298fd4b7-28f5-381a-8957-ab1de86111f7 | -5.52475 | -42.23406 | 2024-10-25 05:01:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 91d6a306-1879-3628-9dd8-6251b6bf9ca3 | -5.52395 | -42.23999 | 2024-10-25 05:01:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 54d315fa-793c-342e-9623-87c81f1712f0 | -5.07945 | -43.82788 | 2024-10-25 05:01:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5e34b909-f23c-3498-b3ff-883cba15c57a | -5.0787 | -43.83303 | 2024-10-25 05:01:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f7c07970-6c7c-3194-a36a-0c3eda6524fd | -5.07611 | -43.82918 | 2024-10-25 05:01:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3314e6c3-ed19-3997-8fde-541f7b7c1987 | -5.0724 | -43.83216 | 2024-10-25 05:01:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8f74eab6-cc5e-34c6-8b37-27163fd0edd7 | -3.80202 | -43.25861 | 2024-10-25 05:01:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f938f339-4bb1-3695-bb62-9ddb1008dac2 | -3.80127 | -43.26384 | 2024-10-25 05:01:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e66c8633-9d6c-3f27-99af-5f968c37b9f7 | -5.72332 | -43.78354 | 2024-10-25 05:01:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 327a70cb-ae0a-37de-b291-56007f8b41e6 | -5.72167 | -43.8408 | 2024-10-25 05:01:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5cb6e386-46e4-3008-996e-b75a005add25 | -5.72096 | -43.84576 | 2024-10-25 05:01:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 89d9e211-5f70-3017-b034-e075e9177abc | -5.71939 | -43.77952 | 2024-10-25 05:01:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 65225ca0-cd5c-32b4-979e-9160ab042265 | -5.71764 | -43.77777 | 2024-10-25 05:01:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d80f69b2-60cf-33b0-a3c9-a2bb619d1490 | -5.71746 | -43.84188 | 2024-10-25 05:01:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8cba3e38-e2c5-34c7-9a6a-ead6d1ac878d | -5.71693 | -43.78278 | 2024-10-25 05:01:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae220f3e-6412-34ac-8902-5f9401e6e104 | -5.71532 | -43.8399 | 2024-10-25 05:01:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9a96b849-95d6-38aa-a4c6-635bfd4a9276 | -6.45408 | -44.68132 | 2024-10-25 05:01:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ac1cccff-3507-3055-86a0-371d6b6b5d89 | -6.45359 | -44.67914 | 2024-10-25 05:01:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 506e79f1-6c13-32f9-a6e3-042f71f0d1d3 | -6.45299 | -44.6834 | 2024-10-25 05:01:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ecd00da0-6671-333a-846b-f51ed046758a | -6.29096 | -44.77091 | 2024-10-25 05:01:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 22373e70-2df9-3a01-bc05-3d68bf3c33f6 | -6.29035 | -44.77538 | 2024-10-25 05:01:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2c9a5598-455c-322d-9874-c880934bba82 | -6.19304 | -44.53082 | 2024-10-25 05:01:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f5e4b13f-2a42-31e1-aecd-17f22794a348 | -6.19179 | -44.54 | 2024-10-25 05:01:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0917d5e-cc8b-34c3-a68c-a261a37f62c4 | -6.19115 | -44.54465 | 2024-10-25 05:01:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9df2b922-fb56-3c21-95a8-d48bfefef86d | -6.19053 | -44.54919 | 2024-10-25 05:01:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cefc7a43-bea9-3764-b076-89043844db4b | -6.18764 | -44.52474 | 2024-10-25 05:01:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 67b0838b-1ec3-39b4-83f5-14cab1635f2a | -5.8886 | -44.64728 | 2024-10-25 05:01:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ee3b68e8-666d-36c9-a481-38b441028389 | -5.88793 | -44.65211 | 2024-10-25 05:01:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4ff17769-caf4-38e2-a07e-26573f379af7 | -5.87089 | -44.68582 | 2024-10-25 05:01:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8437ac7f-4ab7-3627-891e-4f77f2714227 | -5.8649 | -44.6847 | 2024-10-25 05:01:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f2b41934-31f4-3563-8113-f9ebf14761f8 | -5.81024 | -44.49595 | 2024-10-25 05:01:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f357ea43-8ca1-3306-9a4f-e4ce30ba6de6 | -5.62524 | -44.83249 | 2024-10-25 05:01:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0e86a62c-e575-388b-a0ef-2ed36039e161 | -5.61992 | -44.82708 | 2024-10-25 05:01:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 30d035fb-38f6-30a4-bb81-7083d308a46f | -5.61931 | -44.83146 | 2024-10-25 05:01:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 87f6e2e6-1f30-39c1-96b9-7bd01830388f | -5.57515 | -44.88787 | 2024-10-25 05:01:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ad275a5a-efbb-3954-b56c-6dce7e47bda9 | -5.57201 | -44.88496 | 2024-10-25 05:01:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4386328c-c28f-3e12-b185-9b89be6ae8f1 | -5.5714 | -44.88918 | 2024-10-25 05:01:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a37635f5-0735-3e7d-9d7d-48612d158f4b | -5.56981 | -44.88275 | 2024-10-25 05:01:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 51e2275e-06d8-367e-82cb-6db10be2ca77 | -5.56922 | -44.887 | 2024-10-25 05:01:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7da5ed28-9bfd-339e-bba3-8bc74d248583 | -5.50758 | -44.82658 | 2024-10-25 05:01:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4d63107d-8e50-3a04-92a9-d48b75b3c3ee | -5.50698 | -44.83087 | 2024-10-25 05:01:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 81d9e664-dc74-369f-826e-982499025d03 | -5.50163 | -44.82576 | 2024-10-25 05:01:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab40ad36-d332-315e-bbdc-cdbd841e9d66 | -5.28229 | -44.7402 | 2024-10-25 05:01:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0c896416-d8d2-3bcf-bcbe-1f537551caab | -7.19629 | -44.73971 | 2024-10-25 05:01:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b841121f-34b3-3a6c-ab12-8487c902cf59 | -7.19569 | -44.74432 | 2024-10-25 05:01:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c6bcb7e-23ee-3e52-ab94-422d2ea3c453 | -7.19563 | -44.74107 | 2024-10-25 05:01:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8d042859-1e0d-3ebe-93f9-e9a22cd6eec1 | -7.1902 | -44.73866 | 2024-10-25 05:01:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 263ce7ee-719d-3990-aa41-09fc870dc8d9 | -7.18959 | -44.74329 | 2024-10-25 05:01:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 98495f84-2f97-3a8a-a2bc-bc2bc49ccc0c | -7.18954 | -44.74002 | 2024-10-25 05:01:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 400ecb6a-9399-38e5-ab6d-093cb45f0ab2 | -7.06715 | -45.2313 | 2024-10-25 05:01:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| dbecddd9-78ff-3199-8247-b157ddb3712c | -7.0612 | -45.23068 | 2024-10-25 05:01:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| de492875-1beb-3ddb-a2ff-de387c22cbaa | -6.84347 | -44.7572 | 2024-10-25 05:01:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7a1e865-61ec-37d0-9da6-593c01441e1e | -6.83821 | -44.75565 | 2024-10-25 05:01:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 8b438c0d-d6b2-3f7c-a3d0-0ec78dafa124 | -6.83759 | -44.76041 | 2024-10-25 05:01:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c618dd37-a763-300a-8d91-66a40538f654 | -6.83745 | -44.75586 | 2024-10-25 05:01:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 047a7d4e-5bb2-3946-acdb-d021e9485845 | -6.8368 | -44.7606 | 2024-10-25 05:01:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dd2159d5-2a49-3af4-89dd-c848eeaa6047 | -6.46199 | -44.66851 | 2024-10-25 05:01:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0fc199c8-2219-3823-ae4a-73b9d50c3a69 | -6.46136 | -44.67318 | 2024-10-25 05:01:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7a915c43-c3e2-38b2-a4e6-2eefe75b0437 | -6.46097 | -44.67083 | 2024-10-25 05:01:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 074e71f4-f733-3640-8943-78c9770e62e2 | -6.46073 | -44.67793 | 2024-10-25 05:01:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e40a8803-68fe-3507-8a53-14d509a2d198 | -6.4603 | -44.67559 | 2024-10-25 05:01:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c9e3d64f-df55-305f-b2cd-2f2ae24f200a | -6.45964 | -44.68022 | 2024-10-25 05:01:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 298e7087-3465-3c58-a66d-a65b17ab7ca4 | -8.7952 | -44.72449 | 2024-10-25 05:01:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d2efdc41-98a9-3b5b-8c4a-5a16f7b5f39b | -8.79458 | -44.72941 | 2024-10-25 05:01:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7f88d3cf-1fd5-3386-b3cb-686ec9a24abc | -8.79145 | -44.72228 | 2024-10-25 05:01:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3a741b74-527e-3a59-856b-77797159010c | -8.7908 | -44.72717 | 2024-10-25 05:01:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3ae720bf-d124-3bee-8cce-a2e382d8c298 | -8.79016 | -44.73206 | 2024-10-25 05:01:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 35917478-ae83-38b0-94b6-f2e45bb02bf2 | -8.78951 | -44.73697 | 2024-10-25 05:01:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ddb3a2d-e8cc-3b4c-ba79-c55ea9fe8430 | -8.78886 | -44.74188 | 2024-10-25 05:01:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 09c70d89-9c61-3539-b6cb-7d929139ef75 | -8.78772 | -44.73345 | 2024-10-25 05:01:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c7f0c1c5-fbed-3d2f-9f75-87a703a29732 | -8.78711 | -44.73834 | 2024-10-25 05:01:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 30c8d592-1ca4-3c1d-917f-398f1c4958aa | -8.78329 | -44.71797 | 2024-10-25 05:01:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1ae032ca-fe30-39dc-978a-0f64fe05a12c | -8.78268 | -44.72287 | 2024-10-25 05:01:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8693ab27-ef7f-3b9f-ba4c-4534ac55f66b | -8.78207 | -44.72776 | 2024-10-25 05:01:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e34891f0-b455-326b-8eca-0f4795c88d92 | -8.77957 | -44.71587 | 2024-10-25 05:01:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 88864ec1-de5a-38ad-a809-f2542629858a | -8.77892 | -44.72076 | 2024-10-25 05:01:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 69b72f15-82eb-3e9f-99b6-34264458b65b | -8.77828 | -44.72564 | 2024-10-25 05:01:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1915c3e9-84c9-3ea5-8dfa-34b0627ae68e | -8.77764 | -44.73052 | 2024-10-25 05:01:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 82f46706-c4d3-3991-b035-a6719fe3d0c9 | -8.777 | -44.73539 | 2024-10-25 05:01:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa669de1-3ac1-3eb6-bc19-3a475ae472b3 | -8.77581 | -44.72702 | 2024-10-25 05:01:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 36d760d6-8c03-3d6c-af62-a7c787280896 | -8.7752 | -44.73191 | 2024-10-25 05:01:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 08cc3b7a-b4d1-3884-a875-66d55dfb8535 | -3.47173 | -45.65561 | 2024-10-25 05:01:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c16fef5-e6f1-38e9-9ec0-e81125bf7809 | -3.4712 | -45.65919 | 2024-10-25 05:01:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7c049a2e-ea5b-3ff9-abce-ab69f6497392 | -3.47068 | -45.66275 | 2024-10-25 05:01:00 | NOAA-20 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 133d98d7-9e26-3ffa-a193-b6799fecd406 | -3.77515 | -45.73811 | 2024-10-25 05:01:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 746deace-8e3c-3c52-a2b1-268e7c9cc2f3 | -3.77463 | -45.74167 | 2024-10-25 05:01:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 92409954-1d20-3f6e-a029-ba3d1666f538 | -3.77411 | -45.74523 | 2024-10-25 05:01:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 14.1 |
| d58faabc-ea63-327a-ac54-1a4633109d1e | -3.77359 | -45.74878 | 2024-10-25 05:01:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 14.1 |
| b794ef6b-f3e6-39ee-9424-504bbfbde9a0 | -3.76916 | -45.74089 | 2024-10-25 05:01:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3d182532-5a1f-3eb8-b9fb-fe54fccb8447 | -3.76864 | -45.74443 | 2024-10-25 05:01:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 565efbec-0947-3a0b-a5f8-7f652c8d229a | -4.94792 | -45.54163 | 2024-10-25 05:01:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9cb75fbe-c07f-36d5-a6f8-83915b21cf7b | -4.94733 | -45.54566 | 2024-10-25 05:01:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README81.md)
