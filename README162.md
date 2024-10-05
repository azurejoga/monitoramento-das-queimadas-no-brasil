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

## Dados Diários - Página 162

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 902ec65c-7485-3f20-8337-a9fc6d1501f2 | -12.78833 | -50.54408 | 2024-10-05 12:38:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.8 |
| 5f6544b0-45bf-3c32-b140-756358ce5876 | -13.11875 | -46.37963 | 2024-10-05 12:38:00 | TERRA_M-T | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 46f0bf37-2698-3f25-9b51-7335067485e3 | -13.10987 | -46.37833 | 2024-10-05 12:38:00 | TERRA_M-T | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 954f5ba3-f4ed-35d6-9517-345575f7ad51 | -13.10884 | -46.32277 | 2024-10-05 12:38:00 | TERRA_M-T | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 11.6 |
| b9b4ded6-779a-3445-b835-20e34046787e | -13.10753 | -46.33181 | 2024-10-05 12:38:00 | TERRA_M-T | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 33.6 |
| ca0ac000-f208-311b-9eb8-92a69c0d099a | -13.10623 | -46.34085 | 2024-10-05 12:38:00 | TERRA_M-T | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 274a9f9c-890b-3f83-9684-36df45f07b3d | -13.10492 | -46.3499 | 2024-10-05 12:38:00 | TERRA_M-T | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| b0da3b88-eb9d-30d4-a7e3-454ab9429c77 | -13.10361 | -46.35894 | 2024-10-05 12:38:00 | TERRA_M-T | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 0ff0eddb-417f-3fb0-b39d-18552a2bc352 | -15.13501 | -45.66642 | 2024-10-05 12:38:00 | TERRA_M-T | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 23.0 |
| de25ad4e-6627-39c3-a687-9c8e8eccd197 | -14.07658 | -45.53595 | 2024-10-05 12:38:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 13.9 |
| af265244-4a4a-354b-ab6a-d9dd30ea83f5 | -14.07527 | -45.54533 | 2024-10-05 12:38:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 14325478-61fd-388b-abc3-43c8cf9d2bb9 | -14.06625 | -45.54405 | 2024-10-05 12:38:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| eda22a97-6ca7-341b-9439-d553e7761839 | -14.04785 | -45.4778 | 2024-10-05 12:38:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 1e5503c0-199d-326c-86a6-5182696494b9 | -14.04653 | -45.48718 | 2024-10-05 12:38:00 | TERRA_M-T | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 75.3 |
| cf76b473-916e-3182-9ed1-4ddca78c36dc | -14.49136 | -46.5083 | 2024-10-05 12:38:00 | TERRA_M-T | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 0385e7c3-a93b-3458-8914-febfb64c17cc | -17.62789 | -46.98901 | 2024-10-05 12:38:00 | TERRA_M-T | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 11.6 |
| fcdfa9d8-d16f-34cb-866b-c1bf83f88628 | -17.62657 | -46.99828 | 2024-10-05 12:38:00 | TERRA_M-T | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 36b43aea-3d5f-384d-b6d1-2ff02e639cc5 | -17.62162 | -46.96906 | 2024-10-05 12:38:00 | TERRA_M-T | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 9271383e-2706-375b-8c75-ed55dde4a225 | -17.57963 | -46.93721 | 2024-10-05 12:38:00 | TERRA_M-T | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 12.4 |
| c8420638-af37-33d5-9b5d-47986255f7b4 | -16.94642 | -47.11028 | 2024-10-05 12:38:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 750c2e53-7a6c-3d44-bb6c-84f5d1e6466e | -16.9451 | -47.1195 | 2024-10-05 12:38:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 000b5559-2e51-3f36-b0a9-12fed159bd67 | -16.93621 | -47.11815 | 2024-10-05 12:38:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 23.5 |
| b6ed465f-e271-37aa-9244-2a1215cd4155 | -19.15003 | -46.63245 | 2024-10-05 12:38:00 | TERRA_M-T | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 8f9eac22-60d2-30d4-a335-1824771a08b4 | -19.13169 | -46.63323 | 2024-10-05 12:38:00 | TERRA_M-T | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| fdacea2e-5588-386e-b7e8-865d9d94ae96 | -19.06528 | -46.44894 | 2024-10-05 12:38:00 | TERRA_M-T | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| bfd3bd3c-15cd-3240-905a-129d9be44a4a | -12.82034 | -50.54933 | 2024-10-05 12:38:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 8cba7221-deaf-3c31-b9e9-779d80fc729d | -12.85311 | -47.43496 | 2024-10-05 12:38:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 78e85da7-82ce-3981-8a83-3bc2e36f8130 | -12.85171 | -47.44428 | 2024-10-05 12:38:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 2535ec78-d90f-3daf-9561-9b0c015254cc | -12.84891 | -47.46295 | 2024-10-05 12:38:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 0ae40351-ad1b-3637-bf8e-8ce2c77df0ac | -12.84751 | -47.47229 | 2024-10-05 12:38:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| a5b3500c-648b-3d25-b4de-fb47ac55b900 | -12.83789 | -47.47431 | 2024-10-05 12:38:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 7bd771fd-7255-396f-a822-84ba26d84038 | -12.82888 | -47.47295 | 2024-10-05 12:38:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 42c17a5d-97fc-3cf2-933f-dad857bae387 | -12.77898 | -47.43678 | 2024-10-05 12:38:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 22.6 |
| e03477ea-524a-380f-b234-85701cef5087 | -12.47971 | -47.52586 | 2024-10-05 12:38:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| b91d1500-6c18-3c5f-a1f0-63338f8a6901 | -12.77766 | -50.54233 | 2024-10-05 12:38:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 18f6013d-da61-3b16-b6d6-4675e65c6dab | -12.4783 | -47.53525 | 2024-10-05 12:38:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 562a69eb-572a-3b53-b074-3457c01898f4 | -12.77549 | -50.55576 | 2024-10-05 12:38:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 52.0 |
| ccb5e59a-bdd8-3759-9958-0bcce9ca3e0a | -12.76699 | -50.54058 | 2024-10-05 12:38:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 6cac1301-24e5-3c31-8d14-71f1cfa92b0d | -12.76481 | -50.55401 | 2024-10-05 12:38:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 582.3 |
| 275aad28-ee19-38bc-8df2-bdcf5f7a0557 | -12.76264 | -50.56747 | 2024-10-05 12:38:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 4130c759-ae10-30c0-95c9-da35c7331fdd | -12.75631 | -50.53884 | 2024-10-05 12:38:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 26.2 |
| 52bd6537-0405-3cab-95bb-b13c56378e3b | -12.75413 | -50.55227 | 2024-10-05 12:38:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 127.3 |
| f3524790-7fb2-3593-bc8c-3b1a83bcc994 | -12.60561 | -50.96544 | 2024-10-05 12:38:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 11b563e2-a419-39f6-a0d8-f99b4e48dfa0 | -16.34015 | -51.27094 | 2024-10-05 12:38:00 | TERRA_M-T | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 5f0b4d66-4092-3a0e-94d6-b3e993892222 | -16.08603 | -50.43895 | 2024-10-05 12:38:00 | TERRA_M-T | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| bc2f01e8-5a11-353b-95e7-19422b48ec04 | -16.084 | -50.45144 | 2024-10-05 12:38:00 | TERRA_M-T | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| a9a2ff06-2e57-3fbd-bbfd-c8f427931b53 | -16.06883 | -51.50322 | 2024-10-05 12:38:00 | TERRA_M-T | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 41.3 |
| 349978ec-7b9f-32f3-9482-e8b8f3e7478e | -16.06655 | -51.51722 | 2024-10-05 12:38:00 | TERRA_M-T | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 47.2 |
| 33d7586c-24c8-3b7a-847d-2f0a8012cb4a | -18.78946 | -52.6314 | 2024-10-05 12:40:00 | TERRA_M-T | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 561e673b-ff02-3732-a06d-92ad573c424e | -18.50441 | -52.88071 | 2024-10-05 12:40:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 59.6 |
| ad07c19d-59ac-3d6b-bafb-98166293a2ed | -18.50165 | -52.89683 | 2024-10-05 12:40:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 377.1 |
| dadfac26-05b9-3ada-a5b5-a3084435c288 | -18.49889 | -52.91295 | 2024-10-05 12:40:00 | TERRA_M-T | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 223.2 |
| a807a1cd-4e6d-3ec2-991b-437dd0435a5e | -18.49802 | -52.78123 | 2024-10-05 12:40:00 | TERRA_M-T | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 3aa9db1e-0b52-3fee-ac35-a546a48963b2 | -18.49611 | -52.92914 | 2024-10-05 12:40:00 | TERRA_M-T | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 127.9 |
| c412407b-d985-3933-b783-22b7b22919e7 | -18.49334 | -52.94535 | 2024-10-05 12:40:00 | TERRA_M-T | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 154.6 |
| 2157fa13-330d-3479-83f8-39b39e4ff734 | -18.49297 | -52.87871 | 2024-10-05 12:40:00 | TERRA_M-T | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 15.3 |
| a71419fc-6058-3fcf-a14b-ad35bca3e04a | -18.49054 | -52.96162 | 2024-10-05 12:40:00 | TERRA_M-T | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 821.7 |
| 3eec3a15-640c-369f-8717-5df4d685e8dd | -18.48777 | -52.97777 | 2024-10-05 12:40:00 | TERRA_M-T | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 515.5 |
| f2d9b832-28bb-3eaa-94c8-25852e1d73eb | -18.48743 | -52.91084 | 2024-10-05 12:40:00 | TERRA_M-T | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 06d564e6-c166-3c02-b5de-94deac65b023 | -18.48186 | -52.9432 | 2024-10-05 12:40:00 | TERRA_M-T | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 173.2 |
| 4fc3d507-5662-378f-9017-51c066a9380e | -18.47906 | -52.95941 | 2024-10-05 12:40:00 | TERRA_M-T | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 109.4 |
| 7068b9ae-2032-31e1-be23-d7596a0e0103 | -18.47322 | -52.92468 | 2024-10-05 12:40:00 | TERRA_M-T | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 61.4 |
| c17ab3ac-f424-3418-9384-6595834cbd25 | -18.4704 | -52.94094 | 2024-10-05 12:40:00 | TERRA_M-T | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 236e9b6c-ec96-363e-9f89-f8087e8bbbea | -18.69794 | -57.27749 | 2024-10-05 12:40:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 66.6 |
| a210955d-9a1e-30bf-81cf-c60f16c8b7a0 | -18.68219 | -57.2741 | 2024-10-05 12:40:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 131.7 |
| 794fc17c-5575-39a8-a55c-ebf4df7e1e20 | -18.67383 | -57.26498 | 2024-10-05 12:40:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 107.7 |
| 36b6dbdb-d807-39b1-a856-d22bec04e004 | -18.66644 | -57.27069 | 2024-10-05 12:40:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 102.6 |
| f77a686a-2006-3a6e-bcf0-b3ae9ea4693c | -18.65809 | -57.26154 | 2024-10-05 12:40:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 80.1 |
| 5e5c4706-2178-3a76-8805-4de8a1436514 | -18.65158 | -57.29527 | 2024-10-05 12:40:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 63.6 |
| a3ab12e9-05e7-3635-918b-7c39c65cfa17 | -18.65068 | -57.2673 | 2024-10-05 12:40:00 | TERRA_M-T | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 72.4 |
| a7ab5e65-46e0-349b-9744-2670be56b912 | -19.72457 | -49.08951 | 2024-10-05 12:40:00 | TERRA_M-T | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 0ed584e9-ee8b-37e9-823b-4949519e5bf7 | -19.68116 | -44.18375 | 2024-10-05 12:40:00 | TERRA_M-T | PEDRO LEOPOLDO | MINAS GERAIS | Brasil | 3149309 | 31 | 33 | nan | nan | nan | Cerrado | 18.9 |
| a872a86d-1191-38b4-b159-60c7cc197083 | -20.51875 | -44.89434 | 2024-10-05 12:40:00 | TERRA_M-T | CARMO DA MATA | MINAS GERAIS | Brasil | 3114006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 29c4b22a-40b5-3977-9d27-1c5d3e89dbf3 | -21.83342 | -45.29008 | 2024-10-05 12:40:00 | TERRA_M-T | CAMBUQUIRA | MINAS GERAIS | Brasil | 3110707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| d7648bec-6971-3df9-b872-77cee11064ae | -21.6045 | -45.08331 | 2024-10-05 12:40:00 | TERRA_M-T | SÃO BENTO ABADE | MINAS GERAIS | Brasil | 3160801 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.4 |
| ad96e27b-fcad-35ee-ae6c-a373d8a655c4 | -21.36739 | -44.29624 | 2024-10-05 12:40:00 | TERRA_M-T | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| e25b5832-7596-34a7-8ebf-c14c94a474a0 | -19.3944 | -46.39327 | 2024-10-05 12:40:00 | TERRA_M-T | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 8f76708a-0855-319c-9c31-b63e65ffc2f7 | -20.8398 | -45.55731 | 2024-10-05 12:40:00 | TERRA_M-T | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ac8eaf2f-0180-3c8f-ae65-52ab02b9714e | -19.68202 | -46.09723 | 2024-10-05 12:40:00 | TERRA_M-T | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 21ff93ff-10d9-3cd4-b3f9-082e6435f400 | -22.27996 | -46.32364 | 2024-10-05 12:40:00 | TERRA_M-T | OURO FINO | MINAS GERAIS | Brasil | 3146008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 106d94bb-71fe-3369-83f1-53c2949232ab | -21.93731 | -45.83977 | 2024-10-05 12:40:00 | TERRA_M-T | TURVOLÂNDIA | MINAS GERAIS | Brasil | 3169802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 22da454a-848c-39c6-a9ea-dacfd7f69700 | -21.12943 | -45.29538 | 2024-10-05 12:40:00 | TERRA_M-T | NEPOMUCENO | MINAS GERAIS | Brasil | 3144607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.1 |
| f6e9c027-a4f4-3e44-88de-2a786b4f3372 | -22.83094 | -46.32163 | 2024-10-05 12:40:00 | TERRA_M-T | EXTREMA | MINAS GERAIS | Brasil | 3125101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| b8ed0276-8575-3bf6-a887-ca1cf4884b23 | -22.80688 | -46.28499 | 2024-10-05 12:40:00 | TERRA_M-T | EXTREMA | MINAS GERAIS | Brasil | 3125101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 3b6be78e-5d29-3517-9579-b131faeea7f0 | -19.48882 | -46.77686 | 2024-10-05 12:40:00 | TERRA_M-T | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 24e4d455-8de2-3025-b982-3802233048c3 | -19.4875 | -46.78646 | 2024-10-05 12:40:00 | TERRA_M-T | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 9.4 |
| dbe6c778-1dc0-34cf-b52d-25d639b0e98c | -20.6857 | -47.16697 | 2024-10-05 12:40:00 | TERRA_M-T | ITIRAPUÃ | SÃO PAULO | Brasil | 3523701 | 35 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c2e035ed-d0bd-3a26-a35f-7ac4c7eff5fd | -20.68435 | -47.17661 | 2024-10-05 12:40:00 | TERRA_M-T | ITIRAPUÃ | SÃO PAULO | Brasil | 3523701 | 35 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 85b2e756-ba00-3ad2-9db4-ef3164b04ac9 | -20.67538 | -47.1752 | 2024-10-05 12:40:00 | TERRA_M-T | ITIRAPUÃ | SÃO PAULO | Brasil | 3523701 | 35 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 782499d8-bcb8-38e9-bbbf-ee016aa0874d | -20.66942 | -47.08575 | 2024-10-05 12:40:00 | TERRA_M-T | CAPETINGA | MINAS GERAIS | Brasil | 3112406 | 31 | 33 | nan | nan | nan | Cerrado | 8.7 |
| f470b61c-35e4-3265-9723-360257cc7e28 | -20.28114 | -46.76713 | 2024-10-05 12:40:00 | TERRA_M-T | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 28e013ee-1a99-37df-a52e-62071e954c28 | -21.10605 | -46.98825 | 2024-10-05 12:40:00 | TERRA_M-T | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 17.0 |
| fc4d0d8c-1f36-341b-8063-ef25f98c3c54 | -21.09699 | -46.98695 | 2024-10-05 12:40:00 | TERRA_M-T | ITAMOGI | MINAS GERAIS | Brasil | 3132909 | 31 | 33 | nan | nan | nan | Cerrado | 16.5 |
| f0d58234-82bf-3f94-9ec1-328850fd06d9 | -22.70842 | -47.30445 | 2024-10-05 12:40:00 | TERRA_M-T | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 273617d9-f569-36c4-a57a-547a6bf39c75 | -26.5124 | -52.78988 | 2024-10-05 12:42:00 | TERRA_M-T | SÃO LOURENÇO DO OESTE | SANTA CATARINA | Brasil | 4216909 | 42 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 38209a95-4de0-3293-9051-ff2c905af539 | -28.97269 | -51.06308 | 2024-10-05 12:42:00 | TERRA_M-T | SÃO MARCOS | RIO GRANDE DO SUL | Brasil | 4319000 | 43 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 1bbc0295-9025-38ce-b7f0-f6961d84de8f | -29.75266 | -51.45536 | 2024-10-05 12:42:00 | TERRA_M-T | MONTENEGRO | RIO GRANDE DO SUL | Brasil | 4312401 | 43 | 33 | nan | nan | nan | Pampa | 4.6 |
| d94b06cf-2ba0-3b72-8e2d-b897e102765c | -23.16695 | -47.64614 | 2024-10-05 12:42:00 | TERRA_M-T | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| ac630311-51fc-33c1-ba68-96b20485eb8c | -23.16559 | -47.65603 | 2024-10-05 12:42:00 | TERRA_M-T | TIETÊ | SÃO PAULO | Brasil | 3554508 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 91b8cf25-0378-3773-b580-bdac5379526c | -23.11963 | -48.2465 | 2024-10-05 12:42:00 | TERRA_M-T | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |


[Clique aqui para ver as próximas entradas](README163.md)
