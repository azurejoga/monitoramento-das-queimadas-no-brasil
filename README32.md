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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d6b4eb7b-2b22-354e-a776-4b812ee33a66 | -10.87022 | -50.82574 | 2026-09-16 04:17:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c99aac6d-05bb-3bb9-9b6c-da562b19977c | -12.51984 | -47.15454 | 2026-09-16 04:17:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ed43376d-9841-373e-8ee7-fe681e8fb26e | -13.75388 | -48.79161 | 2026-09-16 04:17:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2bdcaef1-ad4a-36ab-94df-0fda7c29b327 | -13.61237 | -46.94671 | 2026-09-16 04:17:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 30254a06-cc50-375c-aaa0-98c3eb975214 | -13.7573 | -48.79597 | 2026-09-16 04:17:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 90c39357-dae7-385e-89d0-047306200ac0 | -14.06199 | -46.81936 | 2026-09-16 04:17:00 | NOAA-20 | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 70eb57f0-b26a-3e90-a332-4ae988329662 | -12.19697 | -43.47792 | 2026-09-16 04:17:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d3f2447b-3f0e-31e8-80f6-2cf1987851df | -11.30902 | -47.24424 | 2026-09-16 04:17:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 934de20b-1311-3903-9ab7-b72e4fa8ba4e | -10.87123 | -50.82016 | 2026-09-16 04:17:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 236b0cf4-74b7-3a2f-a2d9-1f4d23bc8bdf | -11.88864 | -43.83046 | 2026-09-16 04:17:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 21a0e6dd-e6c1-3891-b0e8-f2dffc0fbb3a | -15.29025 | -42.80916 | 2026-09-16 04:17:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 15.4 |
| dd79c96b-31a3-3a96-9c1e-64ef4c5d0b2f | -15.2897 | -42.81275 | 2026-09-16 04:17:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 15.4 |
| ec2f9c27-a3de-3661-82e1-4641804c167b | -13.60944 | -46.94177 | 2026-09-16 04:17:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 199745a7-366a-3d2d-a272-a88812828927 | -13.75041 | -48.79102 | 2026-09-16 04:17:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 98554332-a809-3de6-9870-6da36a4bb26b | -12.52103 | -47.10487 | 2026-09-16 04:17:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 22d2e1b0-c385-31dc-8c87-6902caa3de01 | -11.19702 | -46.30423 | 2026-09-16 04:17:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 585484ea-d72b-36e9-a620-1edbbc772654 | -13.22814 | -51.63676 | 2026-09-16 04:17:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e5713d80-533d-3bfd-8455-9eac97bf7f31 | -11.4478 | -49.77075 | 2026-09-16 04:17:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f4028f6-86ff-3978-a46d-f4443ced45b5 | -12.52021 | -47.10949 | 2026-09-16 04:17:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2cc41e21-aa35-3932-b849-5a6cc7d384d6 | -11.47949 | -45.74726 | 2026-09-16 04:17:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0e19a1a9-4da5-36b7-94dd-31bdd67cf390 | -12.38067 | -51.41874 | 2026-09-16 04:17:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7241031d-5f8d-3f6b-8f87-839aba542315 | -18.23015 | -41.24395 | 2026-09-16 04:17:00 | NOAA-20 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 5b406f31-8da0-393a-a663-16b6501c202c | -11.62109 | -46.95901 | 2026-09-16 04:17:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b86c6e8e-5b42-3bd9-b7e2-41ea71c05b04 | -15.45797 | -53.78545 | 2026-09-16 04:17:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fe09988f-a48f-3f0a-a74c-9ccb057347bc | -13.75842 | -48.81281 | 2026-09-16 04:17:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cdf56858-7c78-369d-b243-2f4798d5e7ba | -17.03734 | -41.28746 | 2026-09-16 04:17:00 | NOAA-20 | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e4da67dc-0fdb-33c5-b604-95ee742619cf | -17.0409 | -41.28797 | 2026-09-16 04:17:00 | NOAA-20 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 275011e7-c5fd-3d0b-8bdb-484739573148 | -12.55648 | -47.10139 | 2026-09-16 04:17:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ef939d1-f86f-3eb4-ba59-516f832692d9 | -15.46816 | -53.79134 | 2026-09-16 04:17:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5513ce7e-d348-32a9-b347-be3f6ca61ec5 | -18.22656 | -41.24328 | 2026-09-16 04:17:00 | NOAA-20 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| fbd11340-345c-35cf-8097-ea2cee98167b | -13.54942 | -42.41256 | 2026-09-16 04:17:00 | NOAA-20 | PARAMIRIM | BAHIA | Brasil | 2923605 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2077b76d-faf2-3ddc-b94a-8758c965e4bf | -15.27405 | -42.8032 | 2026-09-16 04:17:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 12e1b942-ee3f-3bc8-86d2-26004442d4ed | -15.36653 | -42.19971 | 2026-09-16 04:17:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 9df22c88-fea3-328f-ab41-e582195bd8da | -15.04009 | -48.55595 | 2026-09-16 04:17:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6f60f4f4-4366-3033-a03a-0058e9748062 | -11.98032 | -52.4665 | 2026-09-16 04:17:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b7d0332b-4dd3-3cb6-8c45-7b10bb96f5fa | -13.60874 | -46.94586 | 2026-09-16 04:17:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6310c13-56e4-31ba-9f8f-f7178f9b2882 | -18.64824 | -47.29291 | 2026-09-16 04:17:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 18a8650f-0a49-3336-ba70-dc504b6a95ff | -13.76443 | -48.8261 | 2026-09-16 04:17:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9cd4d2c6-99ff-3c75-8e71-a319d7126741 | -11.89371 | -43.82032 | 2026-09-16 04:17:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 9201363d-62f8-3bf8-a94b-b1b4ead3cef9 | -11.41306 | -51.42715 | 2026-09-16 04:17:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 67833cf1-1977-3255-a13b-c86f3d50d896 | -15.4689 | -53.78773 | 2026-09-16 04:17:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cf13de0d-ecab-3b03-b145-08f723c62050 | -12.15514 | -47.99141 | 2026-09-16 04:17:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 98004a30-1b14-347b-b7d1-d910f8eebd39 | -12.46768 | -41.40219 | 2026-09-16 04:17:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| dc7d9077-2070-3ad3-84c9-30da2ea85682 | -13.64849 | -45.96441 | 2026-09-16 04:17:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ab7bd3e4-390d-381f-9941-3e3044a344d0 | -11.88647 | -43.82278 | 2026-09-16 04:17:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 89213677-3125-3532-b2ea-a6207f9fa07b | -12.55351 | -47.09625 | 2026-09-16 04:17:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3f9090f3-5ffe-318a-a615-6a3653ffaf85 | -12.38081 | -51.42065 | 2026-09-16 04:17:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 590d900b-d4b1-3813-aa68-af6b303bdf6c | -12.62611 | -50.79028 | 2026-09-16 04:17:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f18f1df6-12e0-35cb-bf14-292499b02aab | -11.98499 | -52.47101 | 2026-09-16 04:17:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0cf67ecb-a683-3cf6-801a-d81326abf373 | -15.89013 | -40.23495 | 2026-09-16 04:17:00 | NOAA-20 | JORDÂNIA | MINAS GERAIS | Brasil | 3136504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| fe768352-416c-3c08-bd49-b010e98a2481 | -11.34523 | -47.31857 | 2026-09-16 04:17:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3a1b4ebe-5e86-3416-b564-0343746a7e1c | -12.52775 | -47.108 | 2026-09-16 04:17:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b86a624f-8cfd-3feb-80d6-7b467e6c6fd5 | -11.88749 | -43.8376 | 2026-09-16 04:17:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 219e187c-dc8b-32c8-86ad-3deae0bfb045 | -11.8898 | -43.82333 | 2026-09-16 04:17:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 284726dd-c113-3383-bb20-cf209ccc5fc3 | -15.46344 | -53.78656 | 2026-09-16 04:17:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c1c35ec6-d8f9-3ccc-a0fa-8e4ce7f0f458 | -13.75798 | -48.79224 | 2026-09-16 04:17:00 | NOAA-20 | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 89327072-a53f-325c-9d58-6156b8cb4a28 | -13.45141 | -41.6092 | 2026-09-16 04:17:00 | NOAA-20 | JUSSIAPE | BAHIA | Brasil | 2918605 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b784cac1-81e9-38a5-bb50-b03e17213764 | -10.88939 | -51.49719 | 2026-09-16 04:17:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 29ce7289-c475-3f1c-8cc9-65e3745b73e4 | -12.37049 | -48.45975 | 2026-09-16 04:17:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 394cd30e-1dbd-3e8a-bed5-cb8d3661a736 | -12.6271 | -50.7851 | 2026-09-16 04:17:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| b095c34b-cfaa-35d6-beb4-124d8c6ebedc | -13.29404 | -51.27228 | 2026-09-16 04:17:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5989a761-6d43-37b7-a8fe-155163d76b38 | -15.88899 | -40.22743 | 2026-09-16 04:17:00 | NOAA-20 | JORDÂNIA | MINAS GERAIS | Brasil | 3136504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| ba6673d6-8419-3fda-825b-c261bea0da95 | -14.76481 | -40.93391 | 2026-09-16 04:17:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 0a2eed16-f55d-3530-8c44-93f2ec3b6eaf | -18.2308 | -41.23946 | 2026-09-16 04:17:00 | NOAA-20 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 6dd96d49-038a-3d1f-a118-e37b0fd2243a | -10.89421 | -54.01665 | 2026-09-16 04:17:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f02f981c-2ecc-35ac-aae1-cbeb5c600585 | -16.78084 | -39.43367 | 2026-09-16 04:17:00 | NOAA-20 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8ffc82b5-c3e1-3592-90ea-0e4303853a8b | -15.50741 | -53.84987 | 2026-09-16 04:17:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3dabcede-cb9d-3e05-aae1-e6d2d8847643 | -12.32953 | -47.95641 | 2026-09-16 04:17:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 76221d65-c0fe-388b-a517-40103e7c4207 | -11.62486 | -46.95969 | 2026-09-16 04:17:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 333dd09e-1ccf-343d-b33f-ffc280455e60 | -13.29121 | -51.26953 | 2026-09-16 04:17:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 07f7ed54-cf46-3f98-9905-d0aba7b2d98a | -15.2774 | -42.80366 | 2026-09-16 04:17:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d95fa5eb-1c0b-3852-9ce0-a31f127e4eba | -11.72387 | -47.59627 | 2026-09-16 04:17:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 001f683b-5ead-3f86-9de1-539b915123bc | -18.11079 | -51.69233 | 2026-09-16 04:19:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 16cc02ec-fe4d-33d1-963b-a25d0852b7f3 | -18.1147 | -51.69637 | 2026-09-16 04:19:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1b293768-5de0-3aa2-a99a-1e0548ee6c68 | -18.11016 | -51.6954 | 2026-09-16 04:19:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2cc98d2e-2350-3ae6-b54a-37cf72cbfa8f | -18.98059 | -49.87431 | 2026-09-16 04:19:00 | NOAA-20 | GURINHATÃ | MINAS GERAIS | Brasil | 3129103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b4e15f70-0f6c-3281-9edb-d5071e549a37 | -18.11533 | -51.69332 | 2026-09-16 04:19:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4b722301-ab25-361d-b340-277e50516b4b | -20.8825 | -46.44087 | 2026-09-16 04:19:00 | NOAA-20 | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0e0e685d-f834-3bb4-9444-75f8d6a39dad | -18.37696 | -49.40055 | 2026-09-16 04:19:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 07922d58-9cef-3203-b166-6b02d8634b5e | -19.9495 | -44.70568 | 2026-09-16 04:19:00 | NOAA-20 | IGARATINGA | MINAS GERAIS | Brasil | 3130200 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a40627c4-9828-3edd-8ce2-c294d4c12273 | -6.3257 | -62.6721 | 2026-09-16 04:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 6ec4742a-1b9f-3ad4-a09d-f609c1e1746b | -6.3624 | -62.671 | 2026-09-16 04:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 40.4 |
| 86e4a557-0b6f-3680-b8ea-424b7476d78f | -6.344 | -62.6715 | 2026-09-16 04:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 891eff36-afc5-3709-a2c7-fa089d2a6008 | -6.3623 | -62.6898 | 2026-09-16 04:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 50928c4b-3c18-36ab-b1c0-e3b372368a91 | -6.344 | -62.6904 | 2026-09-16 04:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 76.0 |
| 6e7c49eb-c7a0-3c33-9cdc-d926b9f2f3be | 2.20285 | -50.89508 | 2026-09-16 04:55:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 633bc7db-59cd-3588-ade6-b18e102d8ee5 | -1.21759 | -47.89473 | 2026-09-16 04:55:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e6f08ec7-7aa5-3694-bbca-c967c553b8aa | 4.7512 | -60.56659 | 2026-09-16 04:55:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| edaf8845-913a-341b-b848-2979adb9b8a7 | 2.18159 | -50.9245 | 2026-09-16 04:55:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 898be681-ba9c-3ac9-bb7a-6d21a81e7cc7 | 1.17518 | -50.9528 | 2026-09-16 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c774928-4276-3cd8-8520-ef41936fcb0e | -1.33739 | -46.22171 | 2026-09-16 04:55:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 377f51e2-c109-38ae-95fe-176d1b981d89 | 1.18704 | -50.93978 | 2026-09-16 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 61ec1cf8-becd-3ff8-b36d-83b67f87b877 | -0.98132 | -47.50623 | 2026-09-16 04:55:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b2b41bc4-4ce1-3bb4-bf2c-11b1086a14de | 1.17575 | -50.95644 | 2026-09-16 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c7d1607d-4d0d-3636-bce5-3492a9c1d01f | 0.19903 | -51.36153 | 2026-09-16 04:55:00 | NOAA-21 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6d8af10a-dfad-3267-a96c-078d0582155e | 1.97175 | -50.95281 | 2026-09-16 04:55:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0377c9d3-024e-337a-8597-1fd1361d8d89 | 4.29434 | -60.96655 | 2026-09-16 04:55:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 636679b0-960a-39f5-bed9-d28cf26170fe | 1.17857 | -50.95227 | 2026-09-16 04:55:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23c05874-5480-3bda-a4cb-1d25b6b45871 | -1.21403 | -47.89043 | 2026-09-16 04:55:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b4f4f4ed-9a90-3ae6-b296-ee18b92679cc | 2.19228 | -50.90442 | 2026-09-16 04:55:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README33.md)
