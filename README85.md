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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| df55c982-e053-34cd-9b26-dc07cf324eec | -15.0984 | -54.7189 | 2026-09-28 15:20:00 | GOES-19 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 138.7 |
| 2784e0ef-0cc9-3089-a61c-c59a76c9a4bd | -7.4869 | -44.5751 | 2026-09-28 15:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 3fcecc51-0c5f-36b8-abd3-6e462b9669bd | -15.1847 | -46.141 | 2026-09-28 15:20:00 | GOES-19 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 03416ce7-3dd0-3c8a-b4ef-36d887b9a73a | -12.6463 | -47.2598 | 2026-09-28 15:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 102.6 |
| aef31df9-a183-3633-bd05-04f466cd2bcd | -11.5815 | -50.5261 | 2026-09-28 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| d4b64b93-9983-3b8b-953f-882fb7d81b06 | -11.7313 | -50.68 | 2026-09-28 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 56147c60-ab41-3362-a913-0487ba49765e | -10.8001 | -57.2007 | 2026-09-28 15:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 088f0f4e-6780-3042-b18f-9c48a9b626b4 | -11.3436 | -54.1086 | 2026-09-28 15:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 62.0 |
| a4db8b59-134a-3cce-8097-387639f24373 | -12.1685 | -50.7147 | 2026-09-28 15:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 5b85dd90-1ff9-32a3-acfd-d523e0ff7e44 | -13.6866 | -56.6131 | 2026-09-28 15:20:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 52.6 |
| b9b656fb-8f6b-39af-a083-6e82de55e00d | -10.1284 | -50.2116 | 2026-09-28 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 4a21c5c8-e5c0-356c-836c-bc310d440216 | -12.206 | -50.7531 | 2026-09-28 15:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 381dd4e3-e0fb-3255-831b-162fce8a1a83 | -15.4003 | -47.9035 | 2026-09-28 15:20:00 | GOES-19 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 0afa2b41-8018-3285-af02-680e72860d0a | -12.7677 | -54.0296 | 2026-09-28 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 141.1 |
| e3a2154b-c484-3d99-9f0b-08a354715412 | -11.1966 | -44.7805 | 2026-09-28 15:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 612.2 |
| 834aa4a4-f60c-3a02-a38f-3ca472759e8e | -12.2448 | -50.7057 | 2026-09-28 15:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 6cf9ea30-b3ce-3f21-8593-d492db83d0ef | -11.6186 | -50.5861 | 2026-09-28 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 9fcf9f56-7289-380b-8e12-f12b9a3e439e | -8.2859 | -45.4317 | 2026-09-28 15:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 133.6 |
| f33d2737-e133-3dab-89d7-5326293b5e5b | -12.7868 | -54.0275 | 2026-09-28 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 337.4 |
| 2625155c-28e7-3fc5-9252-31ca8c13ef20 | -10.9156 | -50.6845 | 2026-09-28 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 3be9e56e-cb8d-3731-be39-c1236b7a78b7 | -7.7274 | -44.9182 | 2026-09-28 15:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 2db08d4d-37fd-3191-831e-b700dab04066 | -12.2053 | -50.7959 | 2026-09-28 15:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 103.3 |
| ffcf6765-523f-3e44-b4d7-2c766bbbad27 | -13.3439 | -51.3187 | 2026-09-28 15:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 12d42891-3aba-348b-ae14-b366a3b5c929 | -7.3306 | -54.995 | 2026-09-28 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 1a1e3903-351e-3056-8e92-f894f36d60cc | -11.497 | -47.3727 | 2026-09-28 15:20:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 137.8 |
| 98759219-c101-3204-9b4a-650f66bc4f54 | -12.9109 | -52.0719 | 2026-09-28 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 44.6 |
| d31a94a7-f20e-3426-bbe9-31930e56591f | -7.7037 | -54.7722 | 2026-09-28 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 1d038281-8bd9-3625-a8f8-7c09ee4d81eb | -11.7329 | -50.573 | 2026-09-28 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 985bdc4b-a4e1-37da-93db-ff90f62e938a | -12.2699 | -50.3166 | 2026-09-28 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 76a26216-d13d-3d56-976d-21b1801921a6 | -12.6271 | -47.2626 | 2026-09-28 15:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 46eb24ba-f45d-3b7b-9904-0eb2dc1b9d8d | -12.4351 | -44.1497 | 2026-09-28 15:20:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 144.4 |
| e837d7d5-aa69-399f-a031-9415552844b4 | -11.8094 | -50.5428 | 2026-09-28 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| fc1ef486-8e04-38df-94e0-b7536a792222 | -12.9649 | -51.0671 | 2026-09-28 15:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 116.4 |
| 2acbd8ee-d4a8-3c9d-99b8-475de03c424d | 3.7868 | -60.3155 | 2026-09-28 15:20:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 7c154867-d48d-33e4-b02b-44a66ff275be | -10.8185 | -57.2391 | 2026-09-28 15:20:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 79c16e69-9c65-30b7-97ea-a729f69a05a1 | -11.9586 | -50.7393 | 2026-09-28 15:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 89.5 |
| a087bc19-9ddb-3b86-b711-0b603be70ef0 | -13.1803 | -48.5409 | 2026-09-28 15:20:00 | GOES-19 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 146.6 |
| 55083373-c40e-320f-814b-12cb757ae248 | -12.6263 | -47.3075 | 2026-09-28 15:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 108.9 |
| 80648518-8e61-318f-95c7-cf20a386e6c1 | -11.8659 | -50.5791 | 2026-09-28 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 21552f7d-0508-30f0-8ba5-09ebc1ce8ca5 | -12.1952 | -52.7821 | 2026-09-28 15:20:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 68.2 |
| ec9811c6-e32b-32c6-8a06-5919103e7892 | -10.8967 | -50.6866 | 2026-09-28 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 149.4 |
| e9a98939-a012-3cfa-aedf-daf6d6eaa238 | -10.9538 | -50.6592 | 2026-09-28 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 79cad39e-10b8-31da-8670-ea7efcdd2064 | -11.5821 | -50.4833 | 2026-09-28 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |
| c819f3c1-28b1-3e24-8045-70d5a92f0a46 | -17.09723 | -41.61928 | 2026-09-28 15:26:00 | NOAA-21 | PADRE PARAÍSO | MINAS GERAIS | Brasil | 3146305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 28.2 |
| 7cbcec33-9461-39e1-9f2c-1f3ebf562f75 | -21.36028 | -40.98693 | 2026-09-28 15:26:00 | NOAA-21 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 94481e0e-935d-3a97-9d70-13079f0c4c85 | -17.28078 | -41.17341 | 2026-09-28 15:26:00 | NOAA-21 | CRISÓLITA | MINAS GERAIS | Brasil | 3120151 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.1 |
| 3d41677f-63cc-3702-9b23-6538232c72c3 | -21.04156 | -40.89615 | 2026-09-28 15:26:00 | NOAA-21 | ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3202801 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 655b697f-90b5-3638-8cbb-b6da9331f4d4 | -21.3625 | -40.98246 | 2026-09-28 15:26:00 | NOAA-21 | SÃO FRANCISCO DE ITABAPOANA | RIO DE JANEIRO | Brasil | 3304755 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 1ceb749d-9e7c-3a5c-98bc-11a0142ec2bc | -16.61365 | -41.51214 | 2026-09-28 15:26:00 | NOAA-21 | ITAOBIM | MINAS GERAIS | Brasil | 3133303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 9515724e-a589-3d00-a68d-de1526278195 | -16.62012 | -41.5159 | 2026-09-28 15:26:00 | NOAA-21 | ITAOBIM | MINAS GERAIS | Brasil | 3133303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| 48ba38e3-d01b-3068-9971-779674438c03 | -20.40433 | -41.19732 | 2026-09-28 15:26:00 | NOAA-21 | CONCEIÇÃO DO CASTELO | ESPÍRITO SANTO | Brasil | 3201704 | 32 | 33 | nan | nan | nan | Mata Atlântica | 14.8 |
| 9f125e67-9fcf-3a6b-b7be-a234092bb7d5 | -21.04276 | -40.89297 | 2026-09-28 15:26:00 | NOAA-21 | ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3202801 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| a853fa34-e333-33ff-86a0-93586600e18c | -17.09785 | -41.62635 | 2026-09-28 15:26:00 | NOAA-21 | PADRE PARAÍSO | MINAS GERAIS | Brasil | 3146305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 28.8 |
| 4f26f306-0f3c-3b47-83ce-592b0649f8de | -18.8844 | -41.082 | 2026-09-28 15:26:00 | NOAA-21 | MANTENÓPOLIS | ESPÍRITO SANTO | Brasil | 3203304 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 6dee0f39-a0a1-301a-aa14-d06cc8658905 | -14.60704 | -40.95417 | 2026-09-28 15:29:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Caatinga | 52.9 |
| 4f57f8da-5bf0-3dfc-bd44-4b5c79bbe88b | -14.4768 | -40.712 | 2026-09-28 15:29:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 17.2 |
| 88f8d5a7-4473-346e-87eb-f9b8f49eaad0 | -14.6468 | -40.69963 | 2026-09-28 15:29:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 59.2 |
| b68fe041-5e3e-3637-b4f0-0f6a288683b2 | -4.37552 | -40.60894 | 2026-09-28 15:29:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 32.2 |
| 5bbdc7b4-05f4-318f-8f7e-b15fc0f83d85 | -12.6559 | -39.27889 | 2026-09-28 15:29:00 | NOAA-21 | CASTRO ALVES | BAHIA | Brasil | 2907301 | 29 | 33 | nan | nan | nan | Mata Atlântica | 19.1 |
| a2554ffe-d399-38cb-b913-b362d8cb7279 | -14.53391 | -41.27228 | 2026-09-28 15:29:00 | NOAA-21 | CARAÍBAS | BAHIA | Brasil | 2906899 | 29 | 33 | nan | nan | nan | Caatinga | 22.0 |
| 52b1a0c8-49ac-31d6-a6a7-2ab3b898f2ed | -10.47163 | -36.9543 | 2026-09-28 15:29:00 | NOAA-21 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 15.5 |
| 36fc0f22-dda7-3832-906b-ca795d3c20d3 | -15.07984 | -41.20287 | 2026-09-28 15:29:00 | NOAA-21 | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 56.7 |
| c0c10c4d-34ad-3fcb-92a1-02bffc27ebc5 | -3.64306 | -38.81807 | 2026-09-28 15:29:00 | NOAA-21 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 4d3b417b-06ec-3410-89c6-dfcc68d4fef6 | -9.94013 | -40.64573 | 2026-09-28 15:29:00 | NOAA-21 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 8705af4a-193e-3edd-9a64-18a894ce2baa | -14.09795 | -41.38905 | 2026-09-28 15:29:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 0256ca83-079a-3987-b188-56154f75fbf3 | -6.24394 | -41.59491 | 2026-09-28 15:29:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| bc5524af-c258-3742-8305-f46b01255f26 | -9.15942 | -43.08636 | 2026-09-28 15:29:00 | NOAA-21 | ANÍSIO DE ABREU | PIAUÍ | Brasil | 2200707 | 22 | 33 | nan | nan | nan | Caatinga | 18.8 |
| fcd4e46a-164d-3bce-8275-b9d18c59e176 | -14.52528 | -40.86098 | 2026-09-28 15:29:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 10440eb9-189e-3755-b174-abdfce316391 | -15.45449 | -41.44338 | 2026-09-28 15:29:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 37.8 |
| db3dbfb1-3adb-3ad2-b734-200d2cfccf05 | -6.23706 | -41.59075 | 2026-09-28 15:29:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 859762f2-13ef-3efe-a95d-472263719866 | -16.357 | -41.61002 | 2026-09-28 15:29:00 | NOAA-21 | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.4 |
| fde72843-0b3a-3ca9-b4a5-e055848e49f0 | -11.32359 | -42.21452 | 2026-09-28 15:29:00 | NOAA-21 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 5532e6ee-9fae-3000-b8c9-23dd1e99679e | -10.47045 | -36.95117 | 2026-09-28 15:29:00 | NOAA-21 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 32.8 |
| 240bf720-7954-34a5-96ed-598e35c37736 | -14.75024 | -41.96663 | 2026-09-28 15:29:00 | NOAA-21 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 27.2 |
| 1f74b440-37f5-3175-b2bb-87ac9cb104a6 | -14.83312 | -42.03416 | 2026-09-28 15:29:00 | NOAA-21 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 27.9 |
| 63a086fb-4836-3c47-8a90-3533c2287ed2 | -13.87941 | -41.46845 | 2026-09-28 15:29:00 | NOAA-21 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| e5a6723c-aa3f-3f62-92b9-e6a848f1c40a | -3.88434 | -40.8337 | 2026-09-28 15:29:00 | NOAA-21 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 10.5 |
| c658734b-36c5-3553-a012-e8d0fe5ae0b0 | -13.48778 | -40.89267 | 2026-09-28 15:29:00 | NOAA-21 | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 84a07ef9-b9b8-35af-84d5-d1e2fc947ffb | -11.38412 | -40.61183 | 2026-09-28 15:29:00 | NOAA-21 | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 8b3409ba-a766-3c84-bbc6-9c447b07ea8e | -11.32472 | -42.21412 | 2026-09-28 15:29:00 | NOAA-21 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 6fb2d41e-bdef-3f80-af92-79c3def145c0 | -4.6806 | -43.89952 | 2026-09-28 15:29:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| c929c3d0-65af-380e-a5c7-74632f894f05 | -10.46612 | -36.94986 | 2026-09-28 15:29:00 | NOAA-21 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 266.0 |
| dba154e5-d134-371c-9311-ad387cb09626 | -3.59908 | -38.97721 | 2026-09-28 15:29:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9bd7b0ef-09fd-3da9-9b3c-c63e0697725a | -3.6702 | -39.04133 | 2026-09-28 15:29:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 16.0 |
| a2e9960d-1f52-3ea4-8c77-45a8bd14fd0e | -6.61578 | -43.74201 | 2026-09-28 15:29:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 98b0483a-7fe0-32e4-a088-627adc74f196 | -13.75033 | -42.10005 | 2026-09-28 15:29:00 | NOAA-21 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 13.3 |
| fe64bfda-2761-382d-9e55-5196fbd387cd | -14.24743 | -41.28952 | 2026-09-28 15:29:00 | NOAA-21 | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| b87bb447-c27d-3981-8b69-1a8bfc708397 | -14.13858 | -41.45318 | 2026-09-28 15:29:00 | NOAA-21 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 17.9 |
| f14ea648-3495-34e1-92aa-d882f2aaa8ea | -15.45391 | -41.44999 | 2026-09-28 15:29:00 | NOAA-21 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 38.9 |
| 7910440b-1fd8-367a-ae71-a88b01b9307c | -16.24005 | -41.47878 | 2026-09-28 15:29:00 | NOAA-21 | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.2 |
| b258c384-9548-3d8c-ac1e-9b1c195699a1 | -14.72042 | -41.87977 | 2026-09-28 15:29:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 6283abbe-f257-32bb-87aa-0ff64a9795bf | -5.73779 | -43.28065 | 2026-09-28 15:29:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 15.9 |
| a1b6cb75-efd6-3fc0-a89b-2ad79f678c91 | -14.5433 | -40.84924 | 2026-09-28 15:29:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 482ef583-146e-39ad-ac7b-dee36bed744d | -14.72984 | -41.06287 | 2026-09-28 15:29:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 15.3 |
| a298dda4-bc36-345c-ad4e-4dd15b36936f | -5.03561 | -39.89999 | 2026-09-28 15:29:00 | NOAA-21 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 5.9 |
| b3da3c11-67b6-3206-b7b7-86f9589a4e1c | -14.77545 | -41.14111 | 2026-09-28 15:29:00 | NOAA-21 | ANAGÉ | BAHIA | Brasil | 2901205 | 29 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 7537773c-3221-3629-be59-68bea7a2489d | -11.22106 | -39.97789 | 2026-09-28 15:29:00 | NOAA-21 | CAPIM GROSSO | BAHIA | Brasil | 2906873 | 29 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 49d7bc5e-caac-37cb-9c63-7ebb2a32a557 | -14.23747 | -40.95049 | 2026-09-28 15:29:00 | NOAA-21 | CAETANOS | BAHIA | Brasil | 2905156 | 29 | 33 | nan | nan | nan | Caatinga | 28.1 |
| b0634e99-2d38-38ef-a790-41e0078f9762 | -11.32037 | -40.34541 | 2026-09-28 15:29:00 | NOAA-21 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 86e3c2b6-c111-3079-8be5-91d0f8e06fe3 | -9.44741 | -41.80954 | 2026-09-28 15:29:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 11.6 |


[Clique aqui para ver as próximas entradas](README86.md)
