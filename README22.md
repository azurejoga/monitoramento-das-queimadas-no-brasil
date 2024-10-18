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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1050a38e-819d-364e-97d9-b482f970271f | -6.53705 | -35.15508 | 2024-10-18 03:28:00 | NPP-375D | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 3a773a70-e4d4-3e21-b6da-e9d2125cff2a | -6.40641 | -35.33736 | 2024-10-18 03:28:00 | NPP-375D | NOVA CRUZ | RIO GRANDE DO NORTE | Brasil | 2408300 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 41b9069e-9046-35c0-9e87-307a35c67afd | -6.08764 | -35.11806 | 2024-10-18 03:28:00 | NPP-375D | NÍSIA FLORESTA | RIO GRANDE DO NORTE | Brasil | 2408201 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| fb8ea2c3-b403-35c8-88e7-698f1d13417e | -7.11237 | -35.19989 | 2024-10-18 03:28:00 | NPP-375D | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 0cee803f-f577-341c-8c6f-900bbb80c1dc | -6.75029 | -39.18673 | 2024-10-18 03:28:00 | NPP-375D | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4d4bca54-f9e8-3ede-b211-f3e379226a7e | -6.57234 | -35.12206 | 2024-10-18 03:28:00 | NPP-375D | MATARACA | PARAÍBA | Brasil | 2509305 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| ab40c72f-36cc-39d9-8906-c1fcaa487036 | -5.94733 | -39.67534 | 2024-10-18 03:28:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| eafdf20c-34f1-3fae-aa43-60c8810a35bd | -5.59676 | -43.74292 | 2024-10-18 03:28:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d1155739-1560-380b-b5f3-84a63b1b571e | -5.29757 | -43.07621 | 2024-10-18 03:28:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e0d8259f-6f0b-39a9-873c-c197bbbbbeb3 | -5.29672 | -43.08095 | 2024-10-18 03:28:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 435ccfde-c97a-33d7-8312-24b16ebbb021 | -5.22148 | -43.19097 | 2024-10-18 03:28:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f13667a9-5c99-32e1-917d-724577332ccb | -5.21524 | -43.18981 | 2024-10-18 03:28:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3afc4ecb-f653-34de-94a0-eab2d58c9af3 | -5.16612 | -43.99545 | 2024-10-18 03:28:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 408f28d2-08f7-372c-a478-47291c4f6066 | -4.79061 | -37.75635 | 2024-10-18 03:28:00 | NPP-375D | JAGUARUANA | CEARÁ | Brasil | 2307007 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 10e29bd7-f4ac-3c39-8051-c5784e79bb92 | -3.92697 | -42.40927 | 2024-10-18 03:28:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 109f1662-2f3f-3d2e-bbb7-4de579e721cf | -3.92619 | -42.41383 | 2024-10-18 03:28:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 8ef2595d-d09c-3604-a68e-02c230ad58d6 | -3.9254 | -42.41839 | 2024-10-18 03:28:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| a168234a-1a01-3b2a-81c1-6bdf1743f859 | -3.9217 | -42.40365 | 2024-10-18 03:28:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 96992427-1f99-39b3-a918-cd07058b132a | -3.9209 | -42.40821 | 2024-10-18 03:28:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| b5ea2662-d0dc-3387-9670-e4e2e918300b | -3.92011 | -42.41277 | 2024-10-18 03:28:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| dae70603-68a4-38a0-aa02-aa6a968778d1 | -3.91932 | -42.41732 | 2024-10-18 03:28:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 7d8bdabd-cabe-3318-bd22-053ddc272084 | -3.91562 | -42.40262 | 2024-10-18 03:28:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 34bfb743-3f0c-3200-bad2-50bd479785cf | -3.91483 | -42.40718 | 2024-10-18 03:28:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| ec2f1a9b-f44a-3236-8fd0-f83090922aa5 | -3.91404 | -42.41173 | 2024-10-18 03:28:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 11.6 |
| 39568927-c9dd-3a4a-b67b-379f4748e13d | -3.91325 | -42.41626 | 2024-10-18 03:28:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1f760b4b-4a7e-37be-b71c-358b481ef38b | -3.91246 | -42.42077 | 2024-10-18 03:28:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 40c998e1-8b44-3313-af13-2082f41b7786 | -3.90955 | -42.40158 | 2024-10-18 03:28:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 72d5e77d-0e0c-3b40-8230-2028d6ff8865 | -3.90933 | -42.39904 | 2024-10-18 03:28:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c926ea84-a95b-3c79-9f5c-34db3fba2b29 | -3.90857 | -42.40362 | 2024-10-18 03:28:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2b0aeeb0-5e66-3afb-a94d-88f9f99b57e7 | -3.79011 | -43.2355 | 2024-10-18 03:28:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2e1c57c8-e647-3b58-81ce-9661d6d30a0e | -3.66806 | -39.06816 | 2024-10-18 03:28:00 | NPP-375D | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b9ebc554-1a71-39ad-9c62-cce2d20a3ff4 | -3.53811 | -43.61848 | 2024-10-18 03:28:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| b7e05ffa-82fd-3f54-bb03-492ec831ad76 | -3.53153 | -43.61732 | 2024-10-18 03:28:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c86e3819-3841-38b1-8e84-a5f5ed2f8a29 | -3.51802 | -43.23382 | 2024-10-18 03:28:00 | NPP-375D | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 20ed7796-ef24-35fb-8f3c-9f42e4903ec4 | -10.3424 | -36.68375 | 2024-10-18 03:30:00 | NPP-375D | NEÓPOLIS | SERGIPE | Brasil | 2804409 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c265c4d0-15bd-374c-9607-1c8899e0ff1e | -10.28641 | -36.37058 | 2024-10-18 03:30:00 | NPP-375D | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1a6855f8-9d32-3a34-8d2e-5185889fe427 | -21.33797 | -45.88093 | 2024-10-18 03:32:00 | NPP-375D | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 064bb653-80fe-38b7-b9c0-239f46b397bc | -21.33253 | -45.87928 | 2024-10-18 03:32:00 | NPP-375D | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 5b17c848-1832-317c-a2d0-fcafa5053cfd | -21.15983 | -44.98085 | 2024-10-18 03:32:00 | NPP-375D | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 61f803e9-00e2-38dc-98b7-ca39f8fdf612 | -21.15453 | -44.97993 | 2024-10-18 03:32:00 | NPP-375D | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 432b6bbf-a47f-35f7-a37b-683a1b471a84 | -20.34704 | -42.77584 | 2024-10-18 03:32:00 | NPP-375D | URUCÂNIA | MINAS GERAIS | Brasil | 3170503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 304d3e63-1e7f-3f6c-9377-e655cd37e4a8 | -20.34602 | -42.78083 | 2024-10-18 03:32:00 | NPP-375D | URUCÂNIA | MINAS GERAIS | Brasil | 3170503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2be31658-6898-3c26-b11b-46ac0e05235a | -19.91408 | -42.25162 | 2024-10-18 03:32:00 | NPP-375D | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 6c94533c-e237-3d1c-a7b6-99603b771d8d | -19.70702 | -42.22362 | 2024-10-18 03:32:00 | NPP-375D | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 1799cf37-8553-3b1b-9ae8-48871e0803ef | -19.70604 | -42.2285 | 2024-10-18 03:32:00 | NPP-375D | ENTRE FOLHAS | MINAS GERAIS | Brasil | 3123858 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| d69e36ad-989d-3a17-9c6b-75214f6f9ee9 | -19.66783 | -46.2338 | 2024-10-18 03:32:00 | NPP-375D | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9efe1d16-5f81-310e-93db-2a8cd475b36e | -19.66684 | -46.23117 | 2024-10-18 03:32:00 | NPP-375D | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d25bc0c4-1397-396b-b68e-0510433655d8 | -19.64509 | -40.77935 | 2024-10-18 03:32:00 | NPP-375D | ITAGUAÇU | ESPÍRITO SANTO | Brasil | 3202702 | 32 | 33 | nan | nan | nan | Mata Atlântica | 16.5 |
| b9c64550-2f35-348a-9fb3-00de0a9f3f4f | -19.64433 | -40.78331 | 2024-10-18 03:32:00 | NPP-375D | ITAGUAÇU | ESPÍRITO SANTO | Brasil | 3202702 | 32 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| 7d433bc5-eac7-35ad-b243-eb862f94436f | -19.13997 | -42.29417 | 2024-10-18 03:32:00 | NPP-375D | PERIQUITO | MINAS GERAIS | Brasil | 3149952 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 98731a21-a6b8-32bf-862f-50f294e698fb | -18.97135 | -47.12175 | 2024-10-18 03:32:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c32377f7-caf8-3e9c-bfde-5e48ce757ca7 | -18.97006 | -47.12737 | 2024-10-18 03:32:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c42efcaf-ea92-3f31-9889-26905ae4f50f | -18.86523 | -47.52172 | 2024-10-18 03:32:00 | NPP-375D | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1c104e6-ac87-3f64-b21d-25d513c9ada3 | -18.85885 | -47.52028 | 2024-10-18 03:32:00 | NPP-375D | ROMARIA | MINAS GERAIS | Brasil | 3156403 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f8d7cadb-d47c-3149-8863-e75546267109 | -18.61063 | -40.2478 | 2024-10-18 03:32:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 672b541f-008a-3f76-a967-eeca062fc899 | -18.60291 | -40.99815 | 2024-10-18 03:32:00 | NPP-375D | ÁGUA DOCE DO NORTE | ESPÍRITO SANTO | Brasil | 3200169 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| c3c764cc-81f6-36d3-a7d8-9db907211dfc | -18.60205 | -41.00257 | 2024-10-18 03:32:00 | NPP-375D | ÁGUA DOCE DO NORTE | ESPÍRITO SANTO | Brasil | 3200169 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 0e57d7ae-f1c3-3821-8250-fb491d552dad | -18.60159 | -40.99518 | 2024-10-18 03:32:00 | NPP-375D | ÁGUA DOCE DO NORTE | ESPÍRITO SANTO | Brasil | 3200169 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 34637598-c080-380f-b88f-55abd8c9936c | -18.60078 | -40.99948 | 2024-10-18 03:32:00 | NPP-375D | ÁGUA DOCE DO NORTE | ESPÍRITO SANTO | Brasil | 3200169 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| edb60e31-16ed-3ba4-94b3-76c3e106fabd | -18.59999 | -41.00372 | 2024-10-18 03:32:00 | NPP-375D | ÁGUA DOCE DO NORTE | ESPÍRITO SANTO | Brasil | 3200169 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 3d078e06-a0a7-3d4c-85ac-283c8a67e07a | -18.5988 | -40.56821 | 2024-10-18 03:32:00 | NPP-375D | VILA PAVÃO | ESPÍRITO SANTO | Brasil | 3205150 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| c8d9bc40-8797-3df6-b2ff-edcb1621038b | -18.55746 | -40.94625 | 2024-10-18 03:32:00 | NPP-375D | ÁGUA DOCE DO NORTE | ESPÍRITO SANTO | Brasil | 3200169 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 027271ea-1b2d-32e9-b7b5-22a876b279fd | -18.5566 | -40.95077 | 2024-10-18 03:32:00 | NPP-375D | ÁGUA DOCE DO NORTE | ESPÍRITO SANTO | Brasil | 3200169 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| a8babf13-a816-387e-a887-268c64a2f3b4 | -18.55239 | -40.94952 | 2024-10-18 03:32:00 | NPP-375D | ÁGUA DOCE DO NORTE | ESPÍRITO SANTO | Brasil | 3200169 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| be8812b1-134e-37fd-97fa-ab9cb64a27e2 | -18.3015 | -41.88268 | 2024-10-18 03:32:00 | NPP-375D | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 27d95aa7-fecd-30e9-a0ad-1beb26645e8d | -18.3006 | -41.88733 | 2024-10-18 03:32:00 | NPP-375D | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7dca5b5f-7ec5-3798-97ee-ba9cc72a4e32 | -18.10292 | -42.71798 | 2024-10-18 03:32:00 | NPP-375D | FREI LAGONEGRO | MINAS GERAIS | Brasil | 3126950 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 20711944-8193-31e0-b0e4-a06294780d29 | -18.1019 | -42.72308 | 2024-10-18 03:32:00 | NPP-375D | FREI LAGONEGRO | MINAS GERAIS | Brasil | 3126950 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 83d5e8ed-2f27-31cc-a0fa-44fb5121f951 | -18.09717 | -42.72152 | 2024-10-18 03:32:00 | NPP-375D | FREI LAGONEGRO | MINAS GERAIS | Brasil | 3126950 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.7 |
| 6ffc75bc-047b-35e4-86d5-0aeef841c706 | -18.0956 | -42.65435 | 2024-10-18 03:32:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| d9991a09-245b-3f00-a63a-cfaa2c558266 | -18.09454 | -42.65964 | 2024-10-18 03:32:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 40182e81-765c-32da-accd-59b1ca458a54 | -18.03975 | -39.92535 | 2024-10-18 03:32:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f7693ecb-9853-3a20-9cf2-15e3e8f7a914 | -17.96671 | -42.51294 | 2024-10-18 03:32:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| a79700ce-dc0b-394a-8861-1e1a02469cd1 | -17.96577 | -42.51773 | 2024-10-18 03:32:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 730e4d4a-2781-3f66-b70a-d8db0fbf3fa6 | -17.96517 | -42.51457 | 2024-10-18 03:32:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 3746a911-6adb-31a2-9519-72b1e10e4571 | -17.96419 | -42.51936 | 2024-10-18 03:32:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 21e72a55-ec09-3ee9-954a-c54bdc43058d | -17.96201 | -42.51155 | 2024-10-18 03:32:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 4fcbaa26-3345-35ba-87dc-b59728ca8544 | -17.96138 | -42.50871 | 2024-10-18 03:32:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| 3ada7b60-051c-32e6-8016-3b389d06c48c | -17.96106 | -42.51636 | 2024-10-18 03:32:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| eb3e6dec-f02a-3abe-b073-3bb7a2eed803 | -17.96041 | -42.51344 | 2024-10-18 03:32:00 | NPP-375D | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 98464c35-2c4f-3698-9328-7d5dbae07d56 | -17.82687 | -42.31974 | 2024-10-18 03:32:00 | NPP-375D | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ce8bc3d7-42d4-393e-8adf-b12146ef56e2 | -17.82237 | -42.31759 | 2024-10-18 03:32:00 | NPP-375D | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 63d6394d-02a6-3529-82bf-54c1ed0897a2 | -17.67398 | -42.74422 | 2024-10-18 03:32:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d6961f9e-4c1e-37e5-97a0-8b1749d5d5d6 | -17.63487 | -42.3433 | 2024-10-18 03:32:00 | NPP-375D | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9203250d-ac99-3cee-a6d0-7e9b55f33f87 | -17.62279 | -43.93132 | 2024-10-18 03:32:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 30cb27a9-7ea2-3e50-a9ec-887b9a2e0c70 | -17.62212 | -43.93456 | 2024-10-18 03:32:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 03936aac-0eaa-3763-8a60-55af65e6ee23 | -17.61756 | -43.93003 | 2024-10-18 03:32:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 96a0acdc-2d72-3587-af8d-1fa24f464e3e | -17.61688 | -43.93328 | 2024-10-18 03:32:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6e765c53-628f-34a9-bcde-c9e9f49f9719 | -17.58375 | -41.97914 | 2024-10-18 03:32:00 | NPP-375D | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a09956e8-31f5-3c34-bdab-9cbc211c90ec | -17.37974 | -40.44842 | 2024-10-18 03:32:00 | NPP-375D | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| f907e81f-3106-35ea-a48a-62602f781710 | -17.3755 | -40.44766 | 2024-10-18 03:32:00 | NPP-375D | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 03714a0b-0707-3ac5-8c17-7c7ec6f02a21 | -17.19462 | -45.46894 | 2024-10-18 03:32:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6491ee69-c55a-3914-9211-ff1db0b61013 | -17.19367 | -45.47332 | 2024-10-18 03:32:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 78664fcd-d1bd-3254-993f-614faf649597 | -17.18979 | -45.46301 | 2024-10-18 03:32:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1ffc3c23-3040-39b3-897c-ba267b16c01c | -17.18884 | -45.46738 | 2024-10-18 03:32:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b97d6b1e-a802-37ec-b1db-9fdacc75c3f8 | -17.18789 | -45.47178 | 2024-10-18 03:32:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8a8348e6-2c11-39ae-b26d-02325e28576a | -16.77553 | -41.79926 | 2024-10-18 03:32:00 | NPP-375D | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 11521f66-920a-3455-a621-fa50efff17d8 | -16.34928 | -43.69714 | 2024-10-18 03:32:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1c0f462-7478-3ee0-b2ee-80fa1b762f52 | -15.58695 | -42.94474 | 2024-10-18 03:32:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| caf43744-1f46-3d5b-be7f-87f970d98996 | -15.58182 | -42.94364 | 2024-10-18 03:32:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README23.md)
