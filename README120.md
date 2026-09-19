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

## Dados Diários - Página 120

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f759fd7-c1b3-35c4-9229-98e1428b1e64 | -9.784 | -45.059 | 2026-09-19 15:10:00 | GOES-19 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 235.6 |
| 702f8379-5059-3bb3-b7b4-da096ca9aa2b | -3.4462 | -57.9812 | 2026-09-19 15:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 75.6 |
| e63a2d16-29f9-368f-af55-907865a8d2c6 | -10.7991 | -50.9093 | 2026-09-19 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 109.5 |
| b0e06f84-495b-3a0f-9bc9-f37985162b44 | -11.8555 | -47.615 | 2026-09-19 15:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 98f4a7c4-fa39-3fd3-b02c-48e59b818edc | -7.7118 | -44.6451 | 2026-09-19 15:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 596.7 |
| 4b35f295-2245-3226-893d-72b6f87bc47e | -2.9157 | -57.7983 | 2026-09-19 15:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 148.5 |
| 51c86d79-b6ff-388d-946d-892e6b094fda | -7.6572 | -46.1237 | 2026-09-19 15:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 451.1 |
| 8973538b-159e-38fd-866a-f60b8b5ea9bf | -10.8911 | -54.0677 | 2026-09-19 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 81.9 |
| f8376766-55bf-35bd-bce5-c8817169a4e4 | -8.4329 | -45.7337 | 2026-09-19 15:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 105.4 |
| 1eb4a071-9754-3fc8-b2ad-620d552d4f10 | -6.9224 | -55.0376 | 2026-09-19 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 99.2 |
| 217d4d7c-7cb5-3726-a3dc-de83b27303dd | -9.2567 | -46.2098 | 2026-09-19 15:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 8d60bfd5-dc7f-37e2-9bb8-23651485c64e | -8.6171 | -54.6126 | 2026-09-19 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 108.5 |
| 5e87cd38-b7e7-35cc-9a5a-1038e70bb3d2 | -11.8746 | -47.6125 | 2026-09-19 15:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 179.9 |
| 62f8c980-23a9-3c9c-a645-5f3fbaad1607 | -9.1523 | -49.9853 | 2026-09-19 15:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 67b559ad-6d38-3b8f-8577-9085c5d28c40 | -7.6574 | -46.1013 | 2026-09-19 15:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 146.2 |
| da7d0d60-a2f9-3a17-97ac-a20d895b946f | -5.6596 | -43.3906 | 2026-09-19 15:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 162.2 |
| 3a449b93-2b6a-3c2a-bbf1-e7e085c057f2 | -11.8549 | -50.0437 | 2026-09-19 15:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 106.5 |
| 717bc393-6f31-3a24-81d4-098864c088fb | -12.5761 | -49.1071 | 2026-09-19 15:10:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 149.8 |
| 2cd59103-65bc-3a23-b557-40c81fc6e356 | -12.2688 | -49.1907 | 2026-09-19 15:10:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 173.1 |
| 7767c035-e3dc-3406-9efb-c5f0af82240a | -7.7844 | -44.8669 | 2026-09-19 15:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 730d33c5-e401-3be5-9ccd-0f10bef03c40 | -11.299 | -51.7238 | 2026-09-19 15:10:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 711830a2-33a3-3491-b705-ed35b9270832 | -9.7501 | -46.0863 | 2026-09-19 15:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 787bd5cb-b9ca-379f-a60a-f87d62739a45 | -11.0608 | -49.7909 | 2026-09-19 15:10:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 114.6 |
| b7d1d8d3-148d-3ac8-9a0c-2c9fcc32c84f | -8.411 | -54.7274 | 2026-09-19 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 130.0 |
| c745ad97-efeb-3cb6-8b71-fd038fd51a7f | -13.3175 | -51.769 | 2026-09-19 15:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 3c6e8941-d2f2-3a8a-9d3c-f63baddfc984 | -9.6277 | -45.375 | 2026-09-19 15:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 89.5 |
| ed73249e-6a27-38b6-a884-35763a71cd59 | -11.4351 | -51.4774 | 2026-09-19 15:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 1f29614c-2e85-321e-966b-8b69287fb54e | -10.0956 | -48.4226 | 2026-09-19 15:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 209.6 |
| b6610c54-12ea-39b1-ab38-58efc296fe92 | -3.331 | -59.8292 | 2026-09-19 15:10:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 58.8 |
| c80c8533-7c75-349c-8ca8-72113c33f277 | -8.1688 | -54.7432 | 2026-09-19 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 149.3 |
| 75368bcc-b7fc-3848-87f7-553d545815c8 | -11.1035 | -49.4623 | 2026-09-19 15:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 247.8 |
| 5f6811e9-2d06-36b0-bdc7-bb4e64a5b04c | -2.8975 | -57.7793 | 2026-09-19 15:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 4a24d951-6dd8-3af3-97e4-195283cbba58 | -8.7734 | -48.6651 | 2026-09-19 15:10:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 59e40824-ba9f-359a-a436-9a33f4c43570 | -10.7994 | -50.8881 | 2026-09-19 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 1aaff097-58b7-397d-988d-1d638a46e444 | -9.238 | -46.1894 | 2026-09-19 15:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 193a264b-cfdb-34a0-9908-5f71bd5401eb | -7.5705 | -57.657 | 2026-09-19 15:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| a3a4e7d4-cb5b-3db7-a626-e46ba803ad0d | -9.0167 | -48.7505 | 2026-09-19 15:10:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 8d6541d9-7251-3cc7-9c71-42068938d0c4 | -10.7736 | -46.1643 | 2026-09-19 15:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 175.3 |
| 181ef9ad-ecce-3829-bf05-bed8965c3b0c | -11.318 | -51.7218 | 2026-09-19 15:10:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 108.3 |
| 4d2dd1ae-f8fb-383a-8644-ff91d7f6ef8d | -9.6668 | -54.3129 | 2026-09-19 15:10:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 189.6 |
| 90c5234a-74ca-3b97-a968-0baaf4056322 | -8.3771 | -45.6716 | 2026-09-19 15:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 148.9 |
| f3cd7945-1d9c-3402-b748-9d73e683fef9 | -2.6966 | -57.5889 | 2026-09-19 15:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 9f51f746-5969-3691-84bc-81f1c8ce7325 | -10.567 | -51.3137 | 2026-09-19 15:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 163.0 |
| 8011977c-818c-361a-8f7a-ba72234da90f | -4.3743 | -55.2677 | 2026-09-19 15:10:00 | GOES-19 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| e76ca584-3258-3997-973c-64798b585b4f | -11.0223 | -54.1379 | 2026-09-19 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 176.8 |
| 125740e4-ee36-3c02-9637-a75fe6384cbf | -10.5667 | -51.3349 | 2026-09-19 15:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 162.8 |
| 28aca07e-7c15-371a-805c-565031930137 | -10.7133 | -50.258 | 2026-09-19 15:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 159.9 |
| 857cd5bd-1436-3ce5-9b77-599b577522a1 | -9.6087 | -45.3772 | 2026-09-19 15:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 14ba4c6f-66dc-3307-b971-3054a7990eb8 | -7.5703 | -57.6962 | 2026-09-19 15:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 6d380ec8-4d55-3fe3-9100-e7fbaa4dbfbc | -8.5986 | -44.5762 | 2026-09-19 15:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 154.6 |
| 495b402c-0f97-3111-8074-70d542f797db | -6.2236 | -45.1853 | 2026-09-19 15:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 474d7618-99dd-37fe-bd63-cd8817cc644d | -11.8934 | -47.6322 | 2026-09-19 15:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 168.3 |
| 44589250-ce00-3a96-af18-3d05d91864f8 | -8.45 | -45.8674 | 2026-09-19 15:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 166.5 |
| 3b628bfb-4257-3822-93a1-0bb44fa3890c | -5.4142 | -45.8734 | 2026-09-19 15:10:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 529af021-c5c1-3835-aef3-2309d9960224 | -10.9133 | -50.8549 | 2026-09-19 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 212.2 |
| 51850788-b5c1-33db-ab33-ea4a1f1effe4 | -9.3611 | -48.3032 | 2026-09-19 15:10:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 0b8086dd-3da1-330f-a5e2-6594b89a94a8 | -8.7731 | -48.6868 | 2026-09-19 15:10:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 136.5 |
| 32b87d4b-d0df-3e32-b9fc-db592eff042a | -8.9412 | -44.3995 | 2026-09-19 15:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 805a61fd-ef55-3189-b227-358e5977a991 | -8.4108 | -54.7476 | 2026-09-19 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 3200178c-afb7-3afe-8ad4-e744dc9d813a | -12.1474 | -50.8454 | 2026-09-19 15:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 68dbb60b-c2c9-3cef-b87a-abede3d51410 | -10.8367 | -50.9266 | 2026-09-19 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 0ec6053c-c9ef-3aa2-b284-6f2991da513f | -9.2606 | -45.9164 | 2026-09-19 15:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 250.6 |
| c030ff15-ec7f-3ad4-8459-895bbfd87abf | -3.4272 | -58.2138 | 2026-09-19 15:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| dbfc6705-cdb2-38d8-b48a-1937c98315d5 | -10.6703 | -50.6465 | 2026-09-19 15:10:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 87df2c00-ba2d-3f44-af70-e3c05ec4cf5c | -10.913 | -50.8762 | 2026-09-19 15:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 212.6 |
| f66669ce-61bf-373c-ac36-85f23cdd89a5 | -7.7631 | -46.7167 | 2026-09-19 15:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 130.8 |
| 595c8450-8d41-3862-8b0a-0b8ab9ec2620 | -11.3237 | -44.0639 | 2026-09-19 15:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 182.9 |
| fe039574-0cb0-3a25-bc20-890a0d2a7457 | -7.8843 | -47.6333 | 2026-09-19 15:10:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 95.8 |
| ed49d9b0-6fcd-3b45-b292-d7cbb599e76b | 3.9142 | -60.541 | 2026-09-19 15:10:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 57.0 |
| ed102767-0dcc-3ff1-883e-4520eb08ea71 | -8.4797 | -57.6282 | 2026-09-19 15:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 0c7c2ccf-5ee4-3103-9581-8319063f1d6c | -9.2603 | -45.939 | 2026-09-19 15:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 1ebd174e-04fc-3091-b989-e992dc33a1a6 | -9.0355 | -48.7487 | 2026-09-19 15:10:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 139.6 |
| ab3cfba5-a414-30fa-843b-5c94bac4fd96 | -11.0412 | -54.1362 | 2026-09-19 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 0e292ed9-428f-313e-9906-868a96a35019 | -3.7311 | -60.6208 | 2026-09-19 15:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 9760e981-a1b5-3328-8f2e-00c5c46bc1ae | -11.3359 | -43.3793 | 2026-09-19 15:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 141.6 |
| 705ff621-4aa1-3e42-b92d-7433baea72e2 | -5.4143 | -45.851 | 2026-09-19 15:10:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 144.5 |
| 1cc11b13-89d5-3182-a154-d752f4a7dc76 | -8.4295 | -54.7464 | 2026-09-19 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 4dedc6a4-0375-3e1e-b7b6-1c78bc926f9f | -11.3604 | -44.1521 | 2026-09-19 15:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 192.3 |
| f983db0e-372d-36a8-b82e-54291845ba45 | -12.1531 | -46.9707 | 2026-09-19 15:10:00 | GOES-19 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 1803f63a-a8df-32db-973a-10d5135a5b63 | -3.3183 | -57.8677 | 2026-09-19 15:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| bf9bf49f-90b8-30e3-bc54-4f6e54396183 | -1.1991 | -55.7304 | 2026-09-19 15:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| c2ffb470-b775-3bef-bb23-799a52bd2d29 | -2.8791 | -57.799 | 2026-09-19 15:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 1e915929-a686-3243-b91b-d86033fa77f8 | -5.3347 | -48.9857 | 2026-09-19 15:10:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 2d57f91a-8b97-330c-bda5-c00fd830a764 | -12.604 | -50.9191 | 2026-09-19 15:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 94f508bc-b81d-3547-9b67-5a7d69d20779 | -8.4503 | -45.8448 | 2026-09-19 15:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 112.4 |
| 2d342f61-f8f4-329b-bf79-8c6d2b4760f5 | -1.2357 | -55.7103 | 2026-09-19 15:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 7e0f5b82-359d-314f-8367-83d3b53c93bc | -12.2883 | -49.1664 | 2026-09-19 15:10:00 | GOES-19 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 188.1 |
| 4153e8a1-b68d-37cb-89fb-253a24926c36 | -12.1471 | -50.8668 | 2026-09-19 15:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 108.4 |
| 746413bf-5825-3600-883c-914d28b46d94 | -8.6173 | -54.5924 | 2026-09-19 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 141.7 |
| b646b8b6-788d-3f4e-873b-596b1e81a20a | -8.7919 | -48.6851 | 2026-09-19 15:10:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 265.3 |
| 65ebba4b-a693-3fc8-a33f-e96f282dd950 | -12.6037 | -50.9405 | 2026-09-19 15:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 74.1 |
| d535912d-8333-34f5-bd24-969fbd2b4c88 | -7.8598 | -44.8595 | 2026-09-19 15:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 177.7 |
| c92875c1-5a9a-3702-a27d-930e1aac22ac | -11.4354 | -51.4563 | 2026-09-19 15:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 176.0 |
| fd4369fa-5d18-313b-a807-495e9b65f614 | -9.2676 | -48.2472 | 2026-09-19 15:10:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 9392288d-30af-3d0e-be5e-f95c9169f2a1 | -3.888 | -49.0767 | 2026-09-19 15:10:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 48bb1421-a0fa-3923-9017-374346e4e265 | -11.0226 | -54.1174 | 2026-09-19 15:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 109.3 |
| 0cefacfd-ac54-34c9-9ee0-639a50151c26 | -1.5859 | -54.4153 | 2026-09-19 15:10:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 630f1723-a906-3b04-951b-2da3ace65763 | -5.3957 | -45.8522 | 2026-09-19 15:10:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 156.6 |
| 0ad72d58-5255-3949-b598-b8c5957ad930 | -11.0845 | -49.4644 | 2026-09-19 15:10:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 205.8 |
| d3d6752f-12c5-3d2a-96b3-35c4ee71dd26 | -10.7715 | -46.3001 | 2026-09-19 15:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 163.9 |


[Clique aqui para ver as próximas entradas](README121.md)
