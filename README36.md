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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a13467c8-2339-39ab-9359-c947e2bf66f3 | -7.73207 | -44.78819 | 2025-09-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 41eac971-69ec-30e8-85b1-9a4414387d96 | -5.19233 | -43.76105 | 2025-09-29 04:06:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 0c34fd43-8cbf-3648-a1a4-379427e11e74 | -5.79559 | -42.85552 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| ab2d9e33-1c11-381e-bff4-e9b22be6d6c0 | -7.2982 | -42.82897 | 2025-09-29 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6fd4bc0f-f8a7-3121-85f2-be68abb04fb8 | -5.72162 | -42.85469 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 5f7ba75b-f6f9-3ee8-88c5-50f21c25836a | -8.14353 | -46.40493 | 2025-09-29 04:06:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 23c89c2e-3827-38fa-9563-49e4dc238382 | -8.27867 | -45.49477 | 2025-09-29 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 53263767-8e2c-3a2e-a39c-e32d760a775d | -8.27494 | -45.49435 | 2025-09-29 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| dc0a051f-6acd-3759-9e9e-f1a8e349695e | -6.46421 | -43.98452 | 2025-09-29 04:06:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 242796b4-68b2-33b4-8cf9-7b6d4d507e0e | -3.30825 | -51.67074 | 2025-09-29 04:06:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f40701d2-0bf1-3ed3-b1ed-f52a26d56c4b | -7.01913 | -44.77597 | 2025-09-29 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 274abd49-d3ce-30a9-a4de-f66853798b02 | -6.14626 | -42.81055 | 2025-09-29 04:06:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 77e1dfa4-409a-3f5d-9640-a5731964b2c6 | -7.59489 | -44.80423 | 2025-09-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2d1d4a2b-d859-3aea-bc36-9263598e4b4f | -7.73725 | -46.99758 | 2025-09-29 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 1b1d9071-4718-3910-9b56-a16787fc028e | -8.26271 | -45.48609 | 2025-09-29 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| b6c77f59-b4e8-3028-9e6a-28524bf433d7 | -5.86605 | -45.76115 | 2025-09-29 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f0b5859-caf4-39e0-8e8a-e61c26196510 | -5.73761 | -42.66829 | 2025-09-29 04:06:00 | NOAA-20 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6dd1c2da-4b39-3f44-9419-5f922d53b648 | -3.95724 | -41.55991 | 2025-09-29 04:06:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6513c8b9-8899-32a6-ad73-9d036e230d8d | -4.11348 | -48.92673 | 2025-09-29 04:06:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5874f750-052c-3070-9c39-aefe97c2b2fd | -7.22312 | -44.78991 | 2025-09-29 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 6f7ab1d5-50c5-30d1-b5fb-c5258724cf57 | -8.27419 | -45.49879 | 2025-09-29 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 966710bd-9571-3cd5-9db5-37c77ee607b3 | -6.07896 | -42.46678 | 2025-09-29 04:06:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e63a1966-cc9a-37fc-a9c2-906cd0749fd2 | -7.24794 | -43.00076 | 2025-09-29 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 3f7395e1-c4bc-3aa4-aa10-a633df101a31 | -6.06624 | -42.61057 | 2025-09-29 04:06:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 822b47fd-6af4-3e65-8492-9231154b2bcb | -7.38136 | -44.29237 | 2025-09-29 04:06:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b897184-3384-3b71-9afc-5a8ccefd0bd7 | -7.85825 | -44.58921 | 2025-09-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c4ede391-c6d0-3159-8a9d-79ab05594841 | -7.73399 | -44.78708 | 2025-09-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b8c2ef37-66e9-3886-9d60-495232ff2dff | -7.80375 | -46.90092 | 2025-09-29 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 135f9229-c835-3508-9f32-9b3440ef99c5 | -7.18241 | -41.70226 | 2025-09-29 04:06:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 730d25dc-510e-3411-acdd-ca10bbe83958 | -6.9107 | -44.00214 | 2025-09-29 04:06:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7e20a928-8948-3ccf-b0ae-4c35b922e270 | -6.48958 | -44.51123 | 2025-09-29 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0ec52ae2-0985-3076-99ad-6d312b2a26ec | -7.58412 | -44.80231 | 2025-09-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e6ade2c6-f545-31cf-b661-ea63c61cdccd | -6.89338 | -44.53156 | 2025-09-29 04:06:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3382c1f1-38f7-3174-a8d8-5760c920d4ee | -2.80342 | -48.62157 | 2025-09-29 04:06:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d1329e94-7bca-35dc-bfb4-9dc52f52b971 | -5.17359 | -41.25934 | 2025-09-29 04:06:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f5c8e52b-6435-3d4e-bca3-2e8592767334 | -7.0408 | -44.7797 | 2025-09-29 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b0c8f0eb-e44f-3550-af51-5f9c3574d5c8 | -6.67534 | -44.60486 | 2025-09-29 04:06:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c5bde6f9-1cc7-3066-adac-e5863c5f5925 | -7.30283 | -43.81585 | 2025-09-29 04:06:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 021fa16c-16f2-3ce7-909b-6cc1b04616a1 | -5.88527 | -43.29966 | 2025-09-29 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 57b4e8f3-dd37-3ea9-b0de-542f17f5ee15 | -7.46602 | -46.29625 | 2025-09-29 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 275586f4-38ee-3273-8925-13f9c512a93f | -4.38855 | -44.08893 | 2025-09-29 04:06:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc6e041b-e131-30b9-8093-405ddfbfe398 | -6.89761 | -44.52809 | 2025-09-29 04:06:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1ecbf848-40f4-3b8e-a1f6-797755778b32 | -7.10708 | -45.53338 | 2025-09-29 04:06:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 54f40d4a-77d8-307e-a929-04051c271e7f | -5.72383 | -42.86256 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 16c19eda-2f9c-3666-990b-eafc028cdfc6 | -3.36329 | -49.75562 | 2025-09-29 04:06:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 86c53c06-0b57-306b-b5f5-b946e9098eb1 | -5.78355 | -42.88712 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 87167345-6fac-3c08-84b4-65ca1974dc4c | -7.18295 | -41.6988 | 2025-09-29 04:06:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c84dfa7d-4ef0-3d79-8837-4f263e816ce8 | -8.27941 | -45.49043 | 2025-09-29 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a53d9d27-69ee-3046-9e8e-6c3198de9530 | -5.7018 | -42.63334 | 2025-09-29 04:06:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 3588272b-ea91-3550-9910-bf067d656bfa | -6.19618 | -42.84457 | 2025-09-29 04:06:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 7c51dae6-6629-344f-b0a4-e1bb449fb97e | -8.00232 | -44.48325 | 2025-09-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 87a72d68-556f-3c4a-b5d3-d26df0abaa3a | -6.57322 | -43.42624 | 2025-09-29 04:06:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 1fc5960e-e788-3852-aa67-6dadec475f19 | -7.29672 | -44.61142 | 2025-09-29 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d5d50077-6318-366f-bad0-2380b1066da6 | -6.67894 | -44.60545 | 2025-09-29 04:06:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9d75ae10-7373-3b7b-8c4d-36a4ca866e6b | -5.71484 | -42.85366 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e5ad1e90-c3e8-359a-96f5-12b7dca3badc | -7.49583 | -44.30217 | 2025-09-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 36660832-eccf-3502-a6da-9d7b4edb59c4 | -5.93071 | -42.90678 | 2025-09-29 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8faeb74a-9bc5-3321-9a1f-e48eb91e62d3 | -6.02742 | -44.19487 | 2025-09-29 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d437d819-9ccc-37d5-8988-8be0c00ef592 | -5.72452 | -42.83654 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 715a6141-43a0-30fe-a2e7-a95a3d491b7b | -8.29858 | -45.44428 | 2025-09-29 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 002779a8-b9b4-3683-b1f5-31358ee8b17e | -6.46313 | -43.65213 | 2025-09-29 04:06:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9facfbf8-21b0-356b-8aa0-63192c99d209 | -5.55819 | -44.86009 | 2025-09-29 04:06:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9318359e-a882-304d-8fb2-aac024617e5e | -5.43373 | -46.67822 | 2025-09-29 04:06:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c39d869-a1cb-3886-821d-0a689a5be51b | -5.28185 | -43.14762 | 2025-09-29 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 087e9962-7d7a-3f0d-a42c-2cb70878114b | -8.26423 | -45.50004 | 2025-09-29 04:06:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2db30ba6-570c-3a65-a8a8-788b82ded8e4 | -6.57262 | -43.42993 | 2025-09-29 04:06:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 68475e41-9283-3e86-b504-c3e264bac42c | -6.70866 | -44.61306 | 2025-09-29 04:06:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 979e821b-993e-3ea9-b222-dc7e30e1f80b | -6.21517 | -44.198 | 2025-09-29 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 949539be-0874-3b45-a726-c41c74d81d22 | -6.15029 | -42.78541 | 2025-09-29 04:06:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c571fdb1-5561-3e60-92f0-d03a59828fdd | -5.9167 | -42.99422 | 2025-09-29 04:06:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 6df8aad3-b557-3cd1-98b4-9a5710fac0b0 | -6.5034 | -44.12012 | 2025-09-29 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c86212e-4911-3d3b-ac6c-c1f8ea0560ea | -2.57813 | -48.40558 | 2025-09-29 04:06:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 36.3 |
| b322e598-89d8-35a2-852c-9ecfe33c7393 | -3.09519 | -47.01702 | 2025-09-29 04:06:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 174476e8-98b0-3639-8d15-ab0fd30ddd3f | -5.1535 | -46.07816 | 2025-09-29 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1ce8bd07-4cdc-37b6-9145-581c4ebf7a83 | -4.97486 | -44.5126 | 2025-09-29 04:06:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 51e6d34d-2372-3c99-b13a-0bf517411ec7 | -7.36795 | -47.02965 | 2025-09-29 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1c86faaa-375c-32aa-9cf4-f6abe36989fb | -6.27571 | -43.6423 | 2025-09-29 04:06:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0b9fb1a0-ecb7-3b56-932c-5f5b5405ee96 | -3.21313 | -43.36336 | 2025-09-29 04:06:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d771bdc-1b56-3355-9266-dce8700123b7 | -7.16866 | -41.7249 | 2025-09-29 04:06:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d98ce780-52ed-3151-b89f-df27964b37ea | -5.89288 | -42.50684 | 2025-09-29 04:06:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 91459e5a-0f49-38d8-a7d7-0b4ee59cea01 | -5.28124 | -43.15136 | 2025-09-29 04:06:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6a59519f-97fd-3183-af3e-4d30a48926e3 | -8.14974 | -46.34503 | 2025-09-29 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b179bf8-9a0f-3fda-bb9d-5330cf6f051b | -5.90757 | -45.84864 | 2025-09-29 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 12821e5e-0a7f-368f-af57-aa0669ed3091 | -6.20439 | -42.84602 | 2025-09-29 04:06:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| f3c84e0c-3ffc-37ce-b1aa-61feea79378a | -5.78871 | -42.65088 | 2025-09-29 04:06:00 | NOAA-20 | AGRICOLÂNDIA | PIAUÍ | Brasil | 2200103 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| ed56ea13-efa0-3fe4-9558-fc7628abe495 | -5.72791 | -42.83707 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 596bfb69-7bc3-34a2-92f9-a1e355a3e516 | -6.61742 | -45.91055 | 2025-09-29 04:06:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6094c56f-9a62-34c6-9248-8d70a7eefa6a | -5.70574 | -42.6303 | 2025-09-29 04:06:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| ff4e2825-84da-39a5-9236-433eaca2b616 | -5.51729 | -42.72948 | 2025-09-29 04:06:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 980381d4-c337-3dc3-9c13-1b70f254b8e8 | -4.3954 | -47.28257 | 2025-09-29 04:06:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fa634e15-fdab-37da-a815-566c88593b9f | -7.7622 | -45.74707 | 2025-09-29 04:06:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f9398f21-7941-352b-aea6-cf11bfa62c65 | -7.39095 | -44.45378 | 2025-09-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 012adde0-2a09-30ee-8f03-af9807f557d0 | -5.14061 | -42.76354 | 2025-09-29 04:06:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9f2e3b6-56c7-3425-9599-9ee0668aa3e3 | -6.06723 | -42.47578 | 2025-09-29 04:06:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7a9363d6-f782-3def-a28c-f7181a73a442 | -6.6541 | -41.39158 | 2025-09-29 04:06:00 | NOAA-20 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 11887764-b99a-3cf9-a115-63047c9723d1 | -5.7194 | -42.84689 | 2025-09-29 04:06:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| 30787008-04f1-3cf8-968e-74e8e4f923c8 | -6.10165 | -44.49553 | 2025-09-29 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac3c8ec1-7eca-3fd5-90f2-d6675e40b3a1 | -7.35839 | -42.09248 | 2025-09-29 04:06:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2e155415-eba4-3e6c-96dd-a494766080f5 | -7.50766 | -44.29615 | 2025-09-29 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| df9a0eed-6fad-39a7-9c84-7e273230c339 | -8.01122 | -47.03324 | 2025-09-29 04:06:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |


[Clique aqui para ver as próximas entradas](README37.md)
