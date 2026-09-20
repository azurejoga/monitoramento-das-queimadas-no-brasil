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
| 99b3e2c1-6c13-3123-9db5-84ef27892bb7 | -10.8364 | -50.9479 | 2026-09-20 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 317.6 |
| 770bc63b-b598-35e3-a4ea-e5fe032e667b | -8.0892 | -55.3511 | 2026-09-20 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |
| b38688d7-5c10-3783-8112-79c29846f5d7 | -6.7184 | -55.0884 | 2026-09-20 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 9676b451-18c8-38b1-88b8-1a1734985171 | -9.2188 | -46.2139 | 2026-09-20 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| d08eabc6-fe1d-363b-8589-8b90902aa5e2 | -6.1359 | -59.9446 | 2026-09-20 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 6c4a6854-471c-32ea-92b5-d1fd228a6424 | -12.642 | -50.9359 | 2026-09-20 14:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 16813698-39fd-30e6-a522-24cebbdd5222 | -17.5795 | -44.9765 | 2026-09-20 14:00:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 120.6 |
| bba8d534-36ef-3d24-9807-424192c4ded0 | -3.3183 | -57.8677 | 2026-09-20 14:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 72b852b6-0a8f-33ef-bf80-adacc7e0815b | -11.0509 | -54.9106 | 2026-09-20 14:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 652.8 |
| 257c6255-1aca-33e8-b6d0-a21ecb8e1b9e | -10.7899 | -46.3429 | 2026-09-20 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 119.4 |
| 5bfde172-944d-3662-9e78-8ffe572357d2 | -7.9637 | -44.0667 | 2026-09-20 14:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 99.2 |
| d8a4fde4-048b-3744-b3b5-92190dc9e0cc | -12.5224 | -50.0484 | 2026-09-20 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 7a2beb28-bd54-3f10-9eb7-0778107434bf | -11.041 | -54.1567 | 2026-09-20 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.2 |
| fcbe3a88-e9c7-3854-a344-9edf2b130992 | -8.7733 | -44.2336 | 2026-09-20 14:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 3f7e5722-acea-387d-bb97-0ff4a57d4ecf | -3.3492 | -59.8861 | 2026-09-20 14:00:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| e708e215-46c7-3cf9-8b4d-8217c9932df6 | -11.0994 | -54.008 | 2026-09-20 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 90.4 |
| d743d2e8-59e9-36ec-8d74-bc956c95331c | -8.0894 | -55.331 | 2026-09-20 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| ea46c391-fe80-31c1-81cb-d3185ab827c3 | -12.1516 | -47.0608 | 2026-09-20 14:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 111.6 |
| fb8a49ba-3b18-3b36-be8b-2cbce10d644c | -5.8088 | -55.7095 | 2026-09-20 14:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 9b3dc199-608b-32ca-b15a-ec72f55af226 | -9.8313 | -48.4073 | 2026-09-20 14:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 149.4 |
| 5f295ef1-3e0b-3e68-9029-331c23d93ab6 | -13.9641 | -47.8464 | 2026-09-20 14:00:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 13db33e2-a964-3e01-973b-f60c6dd3770c | -11.3793 | -51.3989 | 2026-09-20 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 97.5 |
| ac2f5874-0c6c-3013-9df8-ff756affd567 | -8.7729 | -44.2568 | 2026-09-20 14:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 295.3 |
| 0fca2612-2fa6-39a8-b31e-fb2cc419dd9a | -11.8744 | -50.0199 | 2026-09-20 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 9ac46175-4907-3a3e-b191-3a8e4f76e0d3 | -3.478 | -59.5779 | 2026-09-20 14:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 16ce5986-953d-3897-ab29-0448a1392917 | -7.5941 | -46.7317 | 2026-09-20 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |
| bbf62bf4-83a0-3c71-898d-0171a1f53ee9 | -6.4486 | -59.9717 | 2026-09-20 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 203.3 |
| 904a0574-7c8f-3124-998e-493b550b6d80 | -8.1686 | -54.7634 | 2026-09-20 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 162.5 |
| 47d91b57-de17-38fc-a473-acdff780df54 | -10.3914 | -48.9133 | 2026-09-20 14:00:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 21968276-870e-38ce-a258-21b249735cab | -12.9084 | -51.01 | 2026-09-20 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 91.4 |
| b513405c-54b5-3d7c-ac50-664a1df69887 | -3.7129 | -60.5832 | 2026-09-20 14:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 146.3 |
| 9a9b3a34-698f-398b-a33e-8caa8b8ab048 | -14.061 | -52.1 | 2026-09-20 14:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 138.7 |
| 9ad5357b-4412-3fe7-82ee-375cebd6c339 | -9.2603 | -45.939 | 2026-09-20 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 542.1 |
| 7a3753c8-0568-365b-a118-fe5e5a8f6caf | -6.4671 | -59.9711 | 2026-09-20 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 133.1 |
| 926c4e29-5973-353a-9bf7-7d2f45f69f21 | -2.9143 | -58.3401 | 2026-09-20 14:00:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 3bec1935-3f69-3d26-9e43-816a56bd40c3 | -6.3137 | -41.7768 | 2026-09-20 14:00:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 71.5 |
| 16a52ae7-d822-3cc9-aad3-f90fc9875f24 | -10.9301 | -53.9618 | 2026-09-20 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.8 |
| ad18f102-1a13-356b-80a2-f5e96ef60465 | -3.364 | -42.7824 | 2026-09-20 14:00:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 3339b0ae-0e0e-3713-be52-c1ef2119e8b1 | -11.8747 | -49.9983 | 2026-09-20 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 134.4 |
| bf34841a-291c-3400-bf69-f6610f9b7f8b | -3.3492 | -59.867 | 2026-09-20 14:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 89.0 |
| bdb0bf52-c912-30ea-8c91-b56e2371e5f7 | -10.8921 | -53.9857 | 2026-09-20 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 131.3 |
| 3863ab2e-5932-392b-bab8-1e11c7228864 | -14.6661 | -46.6919 | 2026-09-20 14:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 54.2 |
| 9ebf05e4-d156-3f94-8f58-2aa758aef6fb | -9.8397 | -46.4361 | 2026-09-20 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 450.5 |
| d5c922e9-3972-3fad-9cd1-9b0b6a814d0d | -10.6889 | -50.6658 | 2026-09-20 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 329e53a5-1163-39fb-bbd6-71c94a88e2e6 | -8.3777 | -45.6263 | 2026-09-20 14:00:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 78215251-5711-36f2-879b-d2f5e16f3fa9 | -11.1369 | -54.0251 | 2026-09-20 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 3c973a08-2592-35d2-9638-56b0403a8efd | -9.0541 | -48.7686 | 2026-09-20 14:00:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 150.9 |
| ecb6bcce-7987-3231-91ec-f1d34079eabf | -10.8367 | -50.9266 | 2026-09-20 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 289.1 |
| fead24d3-9d85-3fbf-bc33-34ea4e2893c4 | -6.9225 | -42.9088 | 2026-09-20 14:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 87.0 |
| fb605322-5c17-3de3-970a-59eb3508f516 | -14.6856 | -46.6886 | 2026-09-20 14:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 156.9 |
| 1c36670f-9ac5-3be0-81dd-4c6c378f7e3c | -9.2567 | -46.2098 | 2026-09-20 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 1993b594-78e7-37ee-8b7b-38a6d6079b01 | -3.6947 | -60.5645 | 2026-09-20 14:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 82711ebb-add5-32dc-9038-24f9857ce4c6 | -10.8553 | -50.9459 | 2026-09-20 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 162.6 |
| 60847533-0b8a-39e0-8153-654811ab2135 | -12.5227 | -50.0267 | 2026-09-20 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 108.6 |
| e04ba56e-9535-3663-a56d-41f092dad8ea | -7.6927 | -44.6699 | 2026-09-20 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 71.2 |
| ad6ea829-5675-3587-8876-5b31da2d16e5 | -3.3675 | -59.8857 | 2026-09-20 14:00:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 92af9850-edd3-35a8-8d1f-9b7da0203ca3 | -11.1183 | -54.0062 | 2026-09-20 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 122.5 |
| 88108e25-57d1-3d06-953a-76483ccb3dec | -3.3454 | -42.7597 | 2026-09-20 14:00:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 163.1 |
| a3c43d9c-d5a9-349c-b6f4-f32e079fc2d2 | -3.3493 | -59.8479 | 2026-09-20 14:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 07dfcd18-585e-3f9a-92e1-d9505369cee1 | -10.837 | -50.9054 | 2026-09-20 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 90.6 |
| f395e41b-f2af-3551-a709-b655ec15e71a | -6.7406 | -44.0909 | 2026-09-20 14:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| d5174156-8c0f-3ed7-8cae-4f6433c2850b | -9.8505 | -48.3834 | 2026-09-20 14:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 4e6e0ff6-8c3e-3a79-a87d-55cef09cbf2b | -6.4048 | -43.8885 | 2026-09-20 14:00:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 61.9 |
| d3531674-0f1b-3845-878f-1e382de4291a | -6.467 | -59.9902 | 2026-09-20 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 124.1 |
| 29ebff3d-3dff-382e-96c5-ac0d9017be50 | -3.4455 | -58.2134 | 2026-09-20 14:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 1c56eeaa-e815-3834-a2ec-78742bb64123 | -8.754 | -44.2589 | 2026-09-20 14:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 162.5 |
| ed218258-cd77-3776-ab81-8d75dc57e0b8 | -17.5595 | -44.981 | 2026-09-20 14:00:00 | GOES-19 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 2a680aa6-4804-3272-9e46-74f15e9bfbc9 | -12.5415 | -50.046 | 2026-09-20 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| 1f35b8fa-c8de-35b7-b5af-ea6eae3b6c8f | -3.6945 | -60.6215 | 2026-09-20 14:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 58b64074-a3a8-3f31-a76b-bf3202769c8c | -9.0544 | -48.7469 | 2026-09-20 14:00:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 110.4 |
| b9900cc2-e281-3fa2-8ddd-efcc22360711 | -9.3609 | -48.3251 | 2026-09-20 14:00:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 148.7 |
| 8c18ece5-384f-36b8-83e2-68fe7e8ff112 | -6.5688 | -42.5638 | 2026-09-20 14:00:00 | GOES-19 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 69.4 |
| 32e63414-505b-3cbd-a2b4-e1c95ce2b20e | -11.155 | -42.7885 | 2026-09-20 14:00:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 210.4 |
| ff2c8720-9b2c-32de-a0b4-a44cc7a0c335 | -8.1376 | -46.8155 | 2026-09-20 14:00:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 123.5 |
| b314846d-3406-37e4-ae01-22f45800fb62 | -3.3675 | -59.8666 | 2026-09-20 14:00:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| ce0b29d9-aea0-3e0a-89c2-d006ff6aec27 | -6.4485 | -59.9909 | 2026-09-20 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 175.8 |
| 1fe633aa-b173-3c80-8504-6bb9ed2e0e76 | -12.2341 | -50.1703 | 2026-09-20 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 267.3 |
| 26ba6a12-211f-3748-a32c-bfc24725bb7d | -14.9314 | -49.9103 | 2026-09-20 14:00:00 | GOES-19 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 12c57d9b-4f65-3aa6-8b1e-012843d9ab6d | -7.5944 | -46.7095 | 2026-09-20 14:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 543dc922-a75c-3910-90da-1341243339ce | -6.3198 | -59.9572 | 2026-09-20 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 94.4 |
| aa4a7968-8537-3784-97be-e9e1fcf40b7d | -9.3577 | -50.0943 | 2026-09-20 14:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| ff38388c-eb20-32cc-8dbd-5e3eb2fe5bff | -10.6 | -50.2486 | 2026-09-20 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 3ebeafb2-780d-3acc-8af5-ac1f751cb52b | -10.9665 | -49.7583 | 2026-09-20 14:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 118.4 |
| 9a3946ac-15ba-3816-9e52-50be02a93f88 | -12.8704 | -50.9933 | 2026-09-20 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 85.1 |
| d2ea3f9f-4b72-35e5-9774-2d456cb715a9 | -12.1715 | -47.0131 | 2026-09-20 14:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| e3d52ee0-02aa-35f7-90be-78a8b08490df | -12.1708 | -47.0581 | 2026-09-20 14:00:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 06343a83-d48b-3a2a-874d-64cefb5c9f5d | -9.2563 | -46.2323 | 2026-09-20 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 0bcfc378-d53a-3ec5-8a03-13b430f945eb | -11.1372 | -54.0045 | 2026-09-20 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 78.7 |
| cfcca4af-7dbc-3cf4-9c99-c46503dce903 | -12.3209 | -50.718 | 2026-09-20 14:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 4d668e82-8cca-3d6c-9c1f-96bc8ef130cc | -7.7439 | -46.7629 | 2026-09-20 14:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 59.3 |
| a6a7c054-8e6e-3dc2-a359-8910e6fdc3ae | -8.9752 | -44.6722 | 2026-09-20 14:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 105.3 |
| a68f6922-97d0-3a11-98e2-dfc06ed855e0 | -9.5525 | -63.7842 | 2026-09-20 14:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 6f16e7c8-170a-32ab-af39-655c2ef18fba | -12.1715 | -47.0131 | 2026-09-20 14:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 8bbc7b20-f75b-3d5e-82e9-88134b152e0b | -11.6624 | -50.1954 | 2026-09-20 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 122.3 |
| 31039dff-f236-366b-a5e3-7c233058dc27 | -11.9678 | -50.1379 | 2026-09-20 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 100.3 |
| 8e79d48a-7afe-3a20-8de4-64233a7d14ad | -3.3454 | -42.7597 | 2026-09-20 14:10:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 131.6 |
| bfccfea5-e063-39df-98e7-3c15cb19b07e | -10.6 | -50.2486 | 2026-09-20 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 4debe760-d412-3239-b135-0c0716122728 | -7.0098 | -45.257 | 2026-09-20 14:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 95ed4922-c318-38bf-a132-48a83773ee5d | -10.7115 | -60.7312 | 2026-09-20 14:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 51.9 |
| a9330668-a3db-363b-894b-a953dc46a399 | -13.5911 | -51.458 | 2026-09-20 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 179.5 |


[Clique aqui para ver as próximas entradas](README124.md)
