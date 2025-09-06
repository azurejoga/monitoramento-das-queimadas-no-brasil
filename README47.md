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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f8ddf7be-c984-3481-be26-7ba16305518e | -11.63197 | -47.80102 | 2025-09-06 04:19:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 37ef0ba0-e193-3aa7-8bd8-d0a04e978f96 | -18.98632 | -44.22791 | 2025-09-06 04:19:00 | NPP-375D | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d6aa5886-f1dd-3fc4-a44f-bb806f984513 | -15.72959 | -53.60241 | 2025-09-06 04:19:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 060404cb-2701-332a-ab3e-b02de152d911 | -11.01206 | -45.92956 | 2025-09-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f21b815a-4a9a-3d18-8fa1-b4e654536205 | -9.98543 | -51.61655 | 2025-09-06 04:19:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 024790d6-fc10-3df2-843f-88abc8684324 | -12.00327 | -47.77427 | 2025-09-06 04:19:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 38989b18-c74d-358f-bcb4-a13f79b30df8 | -11.84783 | -47.56836 | 2025-09-06 04:19:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5d8fc1f5-8819-3626-a2ad-2c099635d51c | -12.00986 | -47.77995 | 2025-09-06 04:19:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 00aaf35f-9585-338d-9d18-092c32cec1f5 | -10.94958 | -44.83287 | 2025-09-06 04:19:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1507d56d-f627-3053-b6ee-dbd4b3a82e60 | -19.0681 | -41.13873 | 2025-09-06 04:19:00 | NPP-375D | CUPARAQUE | MINAS GERAIS | Brasil | 3120839 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1c339ec8-b0cd-354d-800b-a8ba937fb5ce | -22.2589 | -48.74514 | 2025-09-06 04:19:00 | NPP-375D | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 8230d295-5ea1-3f1c-bc19-4fc61c45f64a | -17.13455 | -47.27175 | 2025-09-06 04:19:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 520f14e4-7582-3743-aad2-3a6e6acad364 | -12.53648 | -48.06387 | 2025-09-06 04:19:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e8d5ef32-bfc5-30d5-a5c8-19b4c2ef32ab | -19.76423 | -57.96078 | 2025-09-06 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| b1eb671d-1768-35f6-aefa-c82a5ed49991 | -18.01208 | -49.25992 | 2025-09-06 04:19:00 | NPP-375D | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a633674e-cc31-3f1f-b7f0-67639e9bc636 | -21.82933 | -47.99279 | 2025-09-06 04:19:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b36d4645-93c6-3bea-8244-6ed639893592 | -9.24214 | -57.07579 | 2025-09-06 04:19:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 32993979-036c-3319-9016-a38d667d193a | -18.08572 | -45.80337 | 2025-09-06 04:19:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ce08e70a-8920-3ced-9efd-48a7ac51c23a | -10.54912 | -47.00597 | 2025-09-06 04:19:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| d2152438-c76e-306f-964d-470e4519f9e7 | -17.71412 | -44.51037 | 2025-09-06 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 167fe3cc-f6da-3756-a4b4-00006d00ab68 | -10.77589 | -47.78082 | 2025-09-06 04:19:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 228b5c6a-85c6-35ea-a432-1fdb80d68ab3 | -17.76277 | -42.51411 | 2025-09-06 04:19:00 | NPP-375D | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 94bc16d9-b0fd-3a25-ad3e-4809ba403adc | -11.91231 | -46.6433 | 2025-09-06 04:19:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 89b99653-a600-3bb7-a1f0-3ea93625e743 | -19.90402 | -57.93476 | 2025-09-06 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| f478b2fb-744f-376c-88b2-9719b8025701 | -21.99917 | -49.918 | 2025-09-06 04:19:00 | NPP-375D | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 23d8f52a-7a04-3df3-a814-56dd926d831c | -10.98059 | -46.81765 | 2025-09-06 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 654d0d96-4f60-33ad-ae18-8c9187224820 | -10.2141 | -49.7191 | 2025-09-06 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 41b8a389-ce4f-33a3-9fad-9e6e22d3c68f | -12.72906 | -45.09545 | 2025-09-06 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| aa19e8b0-af30-3a25-919f-2cad54ae9606 | -11.75392 | -47.74347 | 2025-09-06 04:19:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a163f581-671b-32cb-8a95-2e63489bf0ec | -19.89424 | -57.92232 | 2025-09-06 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| cc4f1170-7540-3a66-bf06-5808ca1ada26 | -11.6498 | -47.15155 | 2025-09-06 04:19:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cfb5fa2c-5d9f-3822-8f54-016b8fef0acf | -17.70621 | -44.49426 | 2025-09-06 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 07d2b061-2c74-31c1-a172-a1dac50c45c3 | -22.25275 | -48.76047 | 2025-09-06 04:19:00 | NPP-375D | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 682897d0-b76c-3db0-9b96-efb7e829987a | -11.94018 | -41.62953 | 2025-09-06 04:19:00 | NPP-375D | MULUNGU DO MORRO | BAHIA | Brasil | 2922052 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| d478f982-cb80-3d9f-a3a2-8c2f5a90791c | -19.6293 | -49.38855 | 2025-09-06 04:19:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 855f7bce-37b8-3aaa-97f3-72e3ffe76f22 | -9.98778 | -51.61959 | 2025-09-06 04:19:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 789a1606-cbcf-3077-811a-66b52b2675f8 | -12.08914 | -45.68896 | 2025-09-06 04:19:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0f310b57-67c1-3322-a658-a5fec420dbf4 | -17.96547 | -44.41414 | 2025-09-06 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c816dba7-fedc-358c-bb63-4c8354687661 | -16.33489 | -52.95123 | 2025-09-06 04:19:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3f9355cf-b819-3780-8853-018d6ada40fd | -12.43883 | -43.77942 | 2025-09-06 04:19:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 520e5d49-c0c3-3c55-b192-8acb6b6b8486 | -16.31726 | -52.93594 | 2025-09-06 04:19:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ebe1c43b-bfbb-34d7-a4cd-bac7da6229a4 | -22.25138 | -48.74771 | 2025-09-06 04:19:00 | NPP-375D | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| bbd74bf0-8b9f-3081-a643-849ffa5992f4 | -10.96923 | -46.82019 | 2025-09-06 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba684b23-d926-32fd-85b5-666e5c48ad83 | -17.31268 | -44.9278 | 2025-09-06 04:19:00 | NPP-375D | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6facfd04-859e-3edc-91b5-5d04425d787f | -10.1375 | -55.16253 | 2025-09-06 04:19:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1d812262-5ac9-3381-a222-7f66df2d1efa | -19.63368 | -49.38487 | 2025-09-06 04:19:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b493d415-04bc-3b7c-ac26-b54554099f61 | -22.27354 | -49.56505 | 2025-09-06 04:19:00 | NPP-375D | GÁLIA | SÃO PAULO | Brasil | 3516606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| de3765a8-6e64-362d-94c2-92a05006f87e | -23.32877 | -50.88074 | 2025-09-06 04:19:00 | NPP-375D | JATAIZINHO | PARANÁ | Brasil | 4112702 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 54d1e172-3817-314e-acd6-6fc3a349999b | -18.26243 | -43.02845 | 2025-09-06 04:19:00 | NPP-375D | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 5ec5b9bf-2f42-3c94-8429-8bc3aa1ee698 | -11.38489 | -43.6013 | 2025-09-06 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 57e83f44-9c2d-3d00-add4-26674e3c7289 | -22.84763 | -49.17136 | 2025-09-06 04:19:00 | NPP-375D | IARAS | SÃO PAULO | Brasil | 3519253 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9c67615c-0ed4-3141-bc72-d418f83665ed | -20.91623 | -44.01141 | 2025-09-06 04:19:00 | NPP-375D | LAGOA DOURADA | MINAS GERAIS | Brasil | 3137403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| a3c76003-5020-38ec-a9df-74661492ddd8 | -19.40521 | -44.31366 | 2025-09-06 04:19:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 715a682a-7245-3a2e-b591-477b3336e99e | -11.38818 | -43.55819 | 2025-09-06 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a4763068-9ba4-3d93-b355-d1b0d2826fdb | -16.33424 | -52.94931 | 2025-09-06 04:19:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b7456373-bde7-31b1-9f37-66c2d16e3551 | -13.33146 | -43.25262 | 2025-09-06 04:19:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ddf8fdd5-1c4b-3617-915e-d42e6a260fcb | -10.97991 | -46.82173 | 2025-09-06 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9304cfa2-113e-3b9f-acf7-0c0bae069591 | -19.78259 | -45.20976 | 2025-09-06 04:19:00 | NPP-375D | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e15c6d61-6789-39b6-8b7a-8f0ae23416f2 | -11.39936 | -43.61815 | 2025-09-06 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 02333c1d-a712-3e1f-a1f6-8f93b7416558 | -19.20813 | -42.87485 | 2025-09-06 04:19:00 | NPP-375D | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 4959bdb0-80bc-3abe-b31f-e13ebc52b547 | -10.75531 | -46.3459 | 2025-09-06 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f0e658db-c32e-37e3-a72e-d5a01b01c245 | -12.55752 | -41.30523 | 2025-09-06 04:19:00 | NPP-375D | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1e2230c8-6745-3b4a-ab0d-0d605c17d433 | -9.97329 | -51.64376 | 2025-09-06 04:19:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 35b8703c-5688-3fe0-8ad8-4c8bd8994135 | -21.83271 | -47.99341 | 2025-09-06 04:19:00 | NPP-375D | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 50fa695c-232f-312b-87b6-1b6bc385e56e | -11.54295 | -47.31847 | 2025-09-06 04:19:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4b0d7fad-d90f-3416-8fe2-f1b5ec989d7e | -9.20952 | -57.09596 | 2025-09-06 04:19:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d755a854-e132-3359-b2a9-9e9bac6c9585 | -17.91339 | -45.90448 | 2025-09-06 04:19:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3cb99ecb-62aa-3b6b-83fd-bbf684268500 | -11.22566 | -46.18559 | 2025-09-06 04:19:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 103f566f-33ea-3b45-993e-69b87f40d819 | -11.2056 | -55.02369 | 2025-09-06 04:19:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 444ee407-5f0c-3556-b921-c82e5f72348a | -17.70229 | -44.49736 | 2025-09-06 04:19:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3622b21f-8ede-3bd5-9a90-bbbe42c64bbe | -11.60551 | -52.18383 | 2025-09-06 04:19:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 40f4cf00-861f-36d3-9b10-98b7e8934f5e | -22.25822 | -48.74915 | 2025-09-06 04:19:00 | NPP-375D | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.0 |
| a31afc79-7459-31f7-b971-5a588679a77e | -21.493 | -46.19416 | 2025-09-06 04:19:00 | NPP-375D | DIVISA NOVA | MINAS GERAIS | Brasil | 3122405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7b10a528-8125-3a53-99dc-d03fdca95663 | -18.59401 | -43.64732 | 2025-09-06 04:19:00 | NPP-375D | DATAS | MINAS GERAIS | Brasil | 3121001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f939477d-9f6b-35d5-b175-c18772d0b131 | -11.93344 | -46.66756 | 2025-09-06 04:19:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 69c59c89-45cb-3f8d-8359-b42cec7c25a2 | -22.2411 | -48.76641 | 2025-09-06 04:19:00 | NPP-375D | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 11fbff7f-a538-3575-81d8-749fe5a3f688 | -18.09969 | -46.93229 | 2025-09-06 04:19:00 | NPP-375D | LAGAMAR | MINAS GERAIS | Brasil | 3137106 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 05bc90ab-43f4-3291-8091-b653f389edb3 | -15.71696 | -53.58792 | 2025-09-06 04:19:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2d14e465-60d0-31ab-be38-7513991d59db | -12.00694 | -47.77494 | 2025-09-06 04:19:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ae396fbf-92e4-3dcf-95cd-21ca2b46723c | -15.7226 | -53.55939 | 2025-09-06 04:19:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3b0ed3b1-85dd-3321-9c4e-1493f3220ab4 | -15.76111 | -53.65156 | 2025-09-06 04:19:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2d24389b-fa34-3ca7-b87f-932dbfdbb440 | -22.66114 | -46.8272 | 2025-09-06 04:19:00 | NPP-375D | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 8b85417c-b82c-35a7-be9c-06b2e1386a11 | -20.23812 | -51.31354 | 2025-09-06 04:19:00 | NPP-375D | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 72058e86-86f0-3fc6-95f6-add83b0de087 | -9.24176 | -57.07594 | 2025-09-06 04:19:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 69ab5243-9664-3213-a51f-4089ac231f4e | -22.65722 | -46.83035 | 2025-09-06 04:19:00 | NPP-375D | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 55571660-cc2e-32b9-a9a4-e76352034a5e | -23.32593 | -50.87529 | 2025-09-06 04:19:00 | NPP-375D | JATAIZINHO | PARANÁ | Brasil | 4112702 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| c25b1ecf-1b89-37d4-b3d5-064ee111ac5f | -10.97704 | -46.81712 | 2025-09-06 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0312c7c-7502-356e-8663-cf95483f4a96 | -21.23769 | -46.95052 | 2025-09-06 04:19:00 | NPP-375D | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7b67f129-43ad-3167-8758-8556f067edfd | -19.50207 | -45.93569 | 2025-09-06 04:19:00 | NPP-375D | SANTA ROSA DA SERRA | MINAS GERAIS | Brasil | 3159704 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 075ea528-d164-3da2-bb75-a91f3f55d6b7 | -10.47171 | -53.62218 | 2025-09-06 04:19:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a1d0639f-6c71-3fda-8b9f-0a2d6a193d37 | -12.72963 | -45.09189 | 2025-09-06 04:19:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 773d0ffa-5a0f-39fc-8735-40c2a63593b5 | -10.77667 | -47.77629 | 2025-09-06 04:19:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 04ef14a0-8dc6-3ba1-b3d9-f15128427200 | -19.46546 | -46.27575 | 2025-09-06 04:19:00 | NPP-375D | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7cd3b685-0727-3ee1-a600-3ea4e6d19d43 | -18.00397 | -49.26291 | 2025-09-06 04:19:00 | NPP-375D | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1ec8784f-ebe3-31e3-8fa4-b92b3225e5e5 | -19.8054 | -57.94653 | 2025-09-06 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 429e31fa-fd09-3a75-88fd-5bef77ab1d8a | -19.90507 | -57.93009 | 2025-09-06 04:19:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| b6e49f8d-793b-32d9-a1d9-724d624c6c65 | -21.44016 | -45.26138 | 2025-09-06 04:19:00 | NPP-375D | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 42cb2f4a-9b05-342f-802c-e60cc2413fc5 | -20.10633 | -44.32207 | 2025-09-06 04:19:00 | NPP-375D | IGARAPÉ | MINAS GERAIS | Brasil | 3130101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4733661f-4701-3298-9497-0300c71bc5ed | -10.23564 | -50.54732 | 2025-09-06 04:19:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d031fdc5-aed3-3e82-b953-aa12b51ed969 | -19.12242 | -46.44611 | 2025-09-06 04:19:00 | NPP-375D | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README48.md)
