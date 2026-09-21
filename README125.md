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

## Dados Diários - Página 125

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 613e51cb-c4d6-340c-b213-779e46e254b4 | -10.3924 | -50.2275 | 2026-09-21 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| de09fe60-154b-3ec3-8693-3f9b25a9a887 | -6.728 | -59.423 | 2026-09-21 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| c9ced574-a9a4-3304-9101-31be72a3471f | -2.8791 | -57.799 | 2026-09-21 14:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 1893531f-3b66-3f8b-b917-e4222c4ec6e8 | -6.1175 | -59.9452 | 2026-09-21 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| c6e43857-7ebc-33f5-9db8-e73cdbae6ee5 | -10.3546 | -50.2313 | 2026-09-21 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 99.9 |
| d85a69db-6b2b-3e7e-806f-542bd7ac4fb4 | -8.7267 | -44.8836 | 2026-09-21 14:10:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 74.3 |
| ed150770-fcf1-3802-b6c6-a9d0b982816e | -11.0991 | -54.0285 | 2026-09-21 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 60707c84-b870-31a2-bb29-09ab58469695 | -11.3419 | -51.3606 | 2026-09-21 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 107.1 |
| bf590b57-e8cf-34d6-9e00-a20c28600f21 | -12.3102 | -50.1826 | 2026-09-21 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 160.4 |
| c729cd09-d467-39e4-93ed-5a3929b1b50f | -8.1876 | -54.7219 | 2026-09-21 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 87e7e34b-2b72-3b46-adcd-74150353bd05 | -11.0412 | -54.1362 | 2026-09-21 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 98.5 |
| c94b54f7-ba2d-3244-8575-f667ff2893b9 | -10.9358 | -50.5972 | 2026-09-21 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 57815820-7c20-3240-9d61-a2a3cd268671 | -11.8715 | -48.9792 | 2026-09-21 14:10:00 | GOES-19 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 103.6 |
| d465a576-dc90-3291-81a7-db9bbfacd5c8 | -6.6761 | -50.9381 | 2026-09-21 14:10:00 | GOES-19 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 158.3 |
| cd9ce98a-8e84-3e7e-bd9d-e204a8ecff79 | -10.9361 | -50.5759 | 2026-09-21 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 53a20a09-dc5f-3ccf-867f-2facba5a70b5 | -7.3259 | -55.6153 | 2026-09-21 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 9f435270-ecf8-34a6-ad6b-5781933cd16a | -10.4278 | -51.8739 | 2026-09-21 14:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 4a8ca465-825f-3d3d-a243-779bbb0c7da9 | -4.4644 | -55.6815 | 2026-09-21 14:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| d01a4032-a23d-39da-9935-77ea5633948a | -14.1815 | -51.808 | 2026-09-21 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 149.0 |
| b94f4ffd-4046-3f64-96fb-6ea39d709f5e | -5.8225 | -53.5214 | 2026-09-21 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 84b4ed17-4c83-3707-a166-58857ce28edc | -3.3 | -57.8681 | 2026-09-21 14:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 75.9 |
| be8034fc-6b3e-3060-b9ee-7810c4b3fbf7 | -4.9533 | -45.16 | 2026-09-21 14:10:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 166.6 |
| 72af24bc-61c7-3ff5-8b10-5e9c214ce8ef | -10.8011 | -50.7604 | 2026-09-21 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 115.4 |
| 392d021c-5054-3216-9122-0a37a7f43e2e | -8.7726 | -44.28 | 2026-09-21 14:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 211.7 |
| 397f591e-a6ed-3b38-83ef-187906f71ea8 | -10.2979 | -50.2372 | 2026-09-21 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 102.4 |
| fbb8e96e-7627-31bc-8c20-2f66b40618b1 | -10.4728 | -51.302 | 2026-09-21 14:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 99.3 |
| 37ac824a-6565-399a-8a11-fd99d04237d3 | -8.7912 | -44.301 | 2026-09-21 14:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 78.9 |
| fe40b132-5ee2-3865-9a16-37e1e73e779e | -3.3453 | -42.7832 | 2026-09-21 14:10:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 147.9 |
| 1fb8ce2f-94e9-3648-b53d-d50817e3b0fa | -10.3917 | -48.8915 | 2026-09-21 14:10:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 141.1 |
| c01dcb47-98bb-373f-ba88-4dae430c5fc9 | -10.3363 | -50.1905 | 2026-09-21 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 9d5f0569-45a4-36e1-bb78-98a66bb566ad | -11.8362 | -50.0244 | 2026-09-21 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| a7fc990c-c071-3891-91fb-18182c7e69b8 | -12.3028 | -50.6559 | 2026-09-21 14:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 119.5 |
| dd935ef7-8412-3930-b519-ecdc83dbd503 | -8.7729 | -44.2568 | 2026-09-21 14:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 171.5 |
| 4a1513d1-25b8-3a95-9eca-3eb274173f2c | -5.6221 | -43.3934 | 2026-09-21 14:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 145.5 |
| b10bac11-3c6a-338d-8f8e-69e05a8e683e | -13.2596 | -51.7973 | 2026-09-21 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 179.0 |
| 7c4290f5-948a-3ac0-a057-04092ab4cf4f | -6.8263 | -55.5421 | 2026-09-21 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 131.4 |
| 413fe186-56c5-341d-bf26-def60ed30319 | -7.5888 | -57.6953 | 2026-09-21 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 404ad5c7-6f6b-37e6-a160-156917d5b93d | -6.5453 | -44.8415 | 2026-09-21 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 3b62f43d-79b6-320a-bdea-ee0ec56a8fda | -12.026 | -50.0663 | 2026-09-21 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 25c26d30-e248-38a7-81a5-93667236b7dc | -6.9225 | -42.9088 | 2026-09-21 14:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 99.4 |
| fca9e7b2-7bfe-3b9f-8604-be23603793da | -10.3728 | -48.8936 | 2026-09-21 14:10:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| bf09f46c-021b-3c4a-ae63-f53a98109ffe | -10.4919 | -51.279 | 2026-09-21 14:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 80.9 |
| d0986ec8-d162-35c5-9505-3e1a0a2e8e14 | -8.7537 | -44.2821 | 2026-09-21 14:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 130.9 |
| 880faf6a-3d6b-3c0d-9540-9d3fe40aeb27 | -12.4012 | -47.0255 | 2026-09-21 14:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 465.9 |
| 25da97f9-74ad-3dff-aa41-4679a190d88c | -12.3105 | -50.161 | 2026-09-21 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 322.8 |
| 7ef2183d-cdea-3320-a9eb-80bbfde95484 | -7.5704 | -57.6766 | 2026-09-21 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 125.4 |
| e7b5681c-387b-3c8f-8fd4-9b3923dc479a | -12.0451 | -50.064 | 2026-09-21 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 335fb00d-0d43-37b1-8fd8-93badcfb325f | -10.8853 | -51.5347 | 2026-09-21 14:10:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 58d6e563-c574-3054-abcb-6b8741ed7378 | -3.4461 | -58.0199 | 2026-09-21 14:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 2bed3790-930a-36b9-afef-95000d9ef5a4 | -10.0898 | -50.2795 | 2026-09-21 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 122.5 |
| 30418559-10a5-3449-92c1-47ebaa777cd0 | -12.8056 | -54.0462 | 2026-09-21 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 133.4 |
| bd62dee0-9ca6-3bf4-96ed-41207f75dfcc | -10.955 | -50.5738 | 2026-09-21 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 98.6 |
| d1d3e30a-cc0a-35e1-a18f-66b0306a1978 | -9.043 | -48.1384 | 2026-09-21 14:10:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 96f00adf-36c8-353b-9821-2cdc06f3b4cb | -11.4545 | -45.3432 | 2026-09-21 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 115.7 |
| 612e083a-4330-3e58-9b64-430a164cc065 | -10.7652 | -50.6153 | 2026-09-21 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 123.9 |
| e7f18ce8-6c55-3832-8f76-ce47c925dd03 | -5.1984 | -56.1103 | 2026-09-21 14:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 38e33138-5213-3360-95a9-13bd23fd34ad | -11.3603 | -51.4009 | 2026-09-21 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 92.2 |
| d41143ed-bfde-3f83-b3c5-eb7272d7fb21 | -10.09 | -50.2581 | 2026-09-21 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 72.3 |
| a99b527f-0d97-3537-b5f0-81335dbe1bec | -6.392 | -45.1948 | 2026-09-21 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 148.4 |
| 8a4ee972-5e64-326b-9a07-a9e5557134c9 | -11.0804 | -49.7456 | 2026-09-21 14:10:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 107.8 |
| 5156beb1-4633-3b89-9b6a-7228c1b203d2 | -10.8735 | -53.9668 | 2026-09-21 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| c0e8fc8b-f32b-3cfd-9255-1ab260a15f8f | -14.0993 | -52.1163 | 2026-09-21 14:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 120.6 |
| 07bf6ba4-e847-3502-a83e-9ef1f148310a | -9.9768 | -50.2694 | 2026-09-21 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 86.8 |
| 5b441e2e-eb00-382e-babe-dd0991cdc267 | -9.5594 | -66.0359 | 2026-09-21 14:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 0c1e7bfd-20d9-3bea-8a35-18c32add6be3 | -6.4671 | -59.9711 | 2026-09-21 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 6e69d63e-0244-36a5-aeaf-3b101e30c68d | -6.7369 | -55.0874 | 2026-09-21 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 3382fa95-4eb9-3eec-a949-29cf54144f99 | -10.4297 | -50.2663 | 2026-09-21 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 1afd0d7b-8a4f-3aae-944e-db350f38883a | -3.6947 | -60.5645 | 2026-09-21 14:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 01bf773f-f2e6-3259-86aa-314f7c45c29d | -5.804 | -53.5223 | 2026-09-21 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| b7f3c8e7-8aef-3c8b-85c8-7b11df46db19 | -6.4107 | -45.1934 | 2026-09-21 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 50a4fa22-1624-3d74-aee6-e57b01871f92 | -3.6449 | -58.8647 | 2026-09-21 14:10:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 67.3 |
| babc3364-b7c7-3b9a-87c1-1effd2b83ab3 | -10.7655 | -50.5939 | 2026-09-21 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 4c6d7db4-018e-3280-ac4c-bbc45385eb37 | -5.7504 | -43.7091 | 2026-09-21 14:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 153.4 |
| ebbd0c19-f350-3286-a0cf-b4dc8ca0092a | -3.6945 | -60.6215 | 2026-09-21 14:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| c6c9ebbc-e1e6-3dc0-9545-2c8b2d998fbe | -6.3918 | -45.2175 | 2026-09-21 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 7fb18f57-e44f-31ac-939b-711965a59d47 | -5.7692 | -43.7077 | 2026-09-21 14:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 15769010-8257-34ab-8626-d55a39b667e6 | -2.9025 | -50.4214 | 2026-09-21 14:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| fe621253-0eef-3731-98d6-27ecbee66112 | -6.1653 | -47.5052 | 2026-09-21 14:10:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 42ceb7f4-c4c1-30cb-9809-5cf244580c00 | -6.8264 | -55.5222 | 2026-09-21 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| c36c92cb-ab04-32ca-a52d-5ff44e529ce5 | -5.9334 | -59.9707 | 2026-09-21 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 126.7 |
| e427f088-4772-3772-a437-fa1ee0f2ccf0 | -7.5703 | -57.6962 | 2026-09-21 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 5075bdc6-c1de-32e1-b84a-0be4256f268f | -10.3725 | -48.9153 | 2026-09-21 14:10:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 69484698-5a59-32f3-ab51-b2f01efc2cd4 | -13.2033 | -51.7193 | 2026-09-21 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 69.8 |
| c1b67b22-2be7-31bd-9e56-2cb4d2de1816 | -13.3251 | -51.2997 | 2026-09-21 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 99cf16e6-8083-3778-bd2b-b85450e13db6 | -5.9335 | -59.9515 | 2026-09-21 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 118.5 |
| 0800aa1b-d92e-30d6-a1ad-7950ca64bae7 | -10.7463 | -50.6172 | 2026-09-21 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 23d58866-76fd-3e98-886b-b9c961424dc7 | -2.8791 | -57.8184 | 2026-09-21 14:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 110.2 |
| 2bc67926-101e-3d6c-9b63-36b2f3c6cd21 | -6.6763 | -50.9172 | 2026-09-21 14:10:00 | GOES-19 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 103.9 |
| 177a4a07-a91d-39d3-8292-30e73edf90b6 | -3.753 | -59.419 | 2026-09-21 14:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 2aceca9c-1d1d-3797-a645-e69ca4bbd07e | -11.8533 | -50.1515 | 2026-09-21 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 91f29126-d32e-37bb-8e8a-b39c582f04a0 | -6.8033 | -59.15 | 2026-09-21 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 5b927ff7-444a-3717-92a8-dd625551038d | -11.118 | -54.0268 | 2026-09-21 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 9ae10268-d585-3388-8c11-8821469d62c3 | -10.3914 | -48.9133 | 2026-09-21 14:10:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 126.5 |
| a8f64884-2999-3b84-ac46-fa9682f40e45 | -13.3443 | -51.2973 | 2026-09-21 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 175.5 |
| afe60f11-bb6f-3435-8e63-183240221751 | -9.7504 | -46.0637 | 2026-09-21 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 3c75f8b8-b85d-3e41-b11b-6d5fd116586b | -9.247 | -57.1488 | 2026-09-21 14:10:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 981f701a-9fb5-3410-a643-5d03a732d20e | -8.1872 | -54.7622 | 2026-09-21 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| a455aa41-d02f-3015-a1d0-8d9d71a0385d | -9.3986 | -48.3213 | 2026-09-21 14:10:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 8a5b793d-bfda-357a-a0cc-5a180c365c71 | -12.3025 | -50.6774 | 2026-09-21 14:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 97ae5b42-870a-3f4e-8ebd-5cfaafa0c77d | -5.8411 | -53.5002 | 2026-09-21 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |


[Clique aqui para ver as próximas entradas](README126.md)
