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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e9f2a955-b77f-3faa-8048-adfc9c56361e | -13.99455 | -56.63319 | 2026-05-02 05:01:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fab1a02a-1843-38c4-a699-429c0046b683 | -11.43295 | -55.09879 | 2026-05-02 05:01:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 732a4ce8-1603-32d4-90a6-18410b2bde35 | -13.81393 | -43.65275 | 2026-05-02 05:01:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e286e973-da26-353d-921f-712f5a0062b2 | -14.20459 | -57.42729 | 2026-05-02 05:01:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 631c099b-bc81-3b15-b15f-cfc98db11546 | -13.99801 | -56.6338 | 2026-05-02 05:01:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 14235c97-eb8d-3621-bacf-f49d0808fcb4 | -12.29186 | -57.40048 | 2026-05-02 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ea64e69-3664-3d66-82fa-df507efae463 | -12.30201 | -57.40673 | 2026-05-02 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 90e24b9b-d2f2-3121-a30c-7a91d4ebc30d | -16.1571 | -58.49107 | 2026-05-02 05:01:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| ea04c28a-3dba-3d43-8d44-0f1c28232292 | -13.99391 | -56.63707 | 2026-05-02 05:01:00 | NPP-375D | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4f4ba3d7-3582-35ec-bfe9-1c349eed5ee6 | -10.97266 | -45.09304 | 2026-05-02 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| dd2663e8-4211-30b5-8344-8505c26337e6 | -11.44246 | -55.10409 | 2026-05-02 05:01:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f7d310b4-1e99-37ab-8fc1-3b8c4c528c2a | -12.29549 | -57.40112 | 2026-05-02 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0a9f9127-12cb-36d7-be15-7d9e00d33d83 | -12.37825 | -50.04137 | 2026-05-02 05:01:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 97ef630c-180c-329d-a484-8c7ef7eb9c05 | -10.97224 | -45.09618 | 2026-05-02 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| bb04c722-8d79-3e1d-8cde-a7823945b512 | -12.3917 | -50.02888 | 2026-05-02 05:01:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| efd98b58-5ca1-3246-9bb6-f35eace7ec9e | -10.98573 | -45.08238 | 2026-05-02 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5097ff46-803d-3743-b34d-1d4df6fea351 | -12.28616 | -57.39256 | 2026-05-02 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 42b6a39e-7b27-33f1-8aac-0c7c80e12036 | -10.99028 | -45.07967 | 2026-05-02 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 415737ca-ecf7-3a90-bc0b-9fbe6dacf142 | -10.97908 | -45.08444 | 2026-05-02 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 35644115-e66b-3f00-bfd0-c98776813ae8 | -13.81441 | -43.6484 | 2026-05-02 05:01:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2dfab204-1440-3d0e-9ebd-02e4780c54ae | -12.37578 | -50.03133 | 2026-05-02 05:01:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 897b28ac-284d-3de2-8c61-e404b06605b7 | -12.29623 | -57.39681 | 2026-05-02 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aee8f498-fed0-34b2-a38e-61d3c1832a40 | -11.44187 | -55.10771 | 2026-05-02 05:01:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94798de7-d719-3297-bb08-191b431a3bda | -12.37758 | -50.0461 | 2026-05-02 05:01:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0cf93a87-0c6e-34d1-ad91-c76741f5097a | -12.37063 | -50.04023 | 2026-05-02 05:01:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 34.7 |
| a8cc75fa-d2ee-3272-a344-510e310cf740 | -10.97992 | -45.07808 | 2026-05-02 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d0a745d7-323c-37a0-a3ee-27436631a648 | -10.98553 | -45.07563 | 2026-05-02 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 35e30bfa-4be6-3e32-8e43-18e85d4dd095 | -10.983 | -45.0947 | 2026-05-02 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d0bb9186-9df8-3195-be69-8e3fedebe86f | -12.2926 | -57.39616 | 2026-05-02 05:01:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 40338f6a-abbb-3b75-9153-f0daf1eee10f | -13.37276 | -54.27039 | 2026-05-02 05:01:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 76386ab7-bd8f-32a7-9d04-0568a98b3a48 | -11.55399 | -48.26791 | 2026-05-02 05:01:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a1bde8a6-efdd-3a01-a38a-9ba1e989965c | -14.20814 | -57.42797 | 2026-05-02 05:01:00 | NPP-375D | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fbd0bc73-6a9a-322d-ae6d-76bf0043e6d8 | -11.44582 | -55.10465 | 2026-05-02 05:01:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1429d56d-294c-318e-97a3-c732060778e8 | -11.44465 | -55.11188 | 2026-05-02 05:01:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99d125d6-d434-3276-aad0-313cbec995c4 | -13.80801 | -43.65202 | 2026-05-02 05:01:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d82af9f-8acc-3fa4-afc5-9488c24ee37f | -10.98943 | -45.08605 | 2026-05-02 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f272a010-1854-3c4c-9b80-73ecf93138cc | -10.99091 | -45.0832 | 2026-05-02 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2f0f0d13-e6ad-3a3b-a01e-59082e038dce | -20.19863 | -46.44598 | 2026-05-02 05:04:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bcb84b8f-888a-357d-9c26-b883ea54fd76 | -18.3127 | -54.65442 | 2026-05-02 05:04:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e4b6bd1d-f105-3dc3-98ca-c0db172853b2 | -20.66794 | -49.69035 | 2026-05-02 05:04:00 | NPP-375D | MONTE APRAZÍVEL | SÃO PAULO | Brasil | 3531407 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7bc72f2c-519d-31e9-95ed-de9dafbdd41a | -20.28231 | -46.44491 | 2026-05-02 05:04:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 50bf345f-93ee-3b30-8956-0758898f905a | -17.93537 | -52.89525 | 2026-05-02 05:04:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 355cae30-6015-36c7-85d3-ff2f0d50609d | -20.28191 | -46.44896 | 2026-05-02 05:04:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44a4b7fc-58a2-3daa-bd4c-a057fe9845db | -17.91311 | -52.89998 | 2026-05-02 05:04:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| afc91a75-5657-307d-b65c-0505b1b760d0 | -20.28268 | -46.4412 | 2026-05-02 05:04:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 65a3167c-1021-3f02-b2fa-82d5dca6a980 | -18.32529 | -54.52743 | 2026-05-02 05:04:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8fcd77c7-c6ae-31ab-b712-b679448b6529 | -20.2803 | -46.44309 | 2026-05-02 05:04:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 811c7f59-fc53-34e1-8ea0-63cdfc14441e | -20.19825 | -46.44968 | 2026-05-02 05:04:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d037c5ca-d983-3ee3-bcf6-02617657d1e3 | -18.49431 | -51.6918 | 2026-05-02 05:04:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 35ce9093-cea9-3223-9cb1-22c0d63c0c93 | -20.71497 | -55.17793 | 2026-05-02 05:04:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 29839086-d3d1-3f5a-97a2-c69c9bb878d0 | -18.17045 | -51.11279 | 2026-05-02 05:04:00 | NPP-375D | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 779e75b5-1cd6-373f-b502-5800713b6ee5 | -21.2345 | -56.92952 | 2026-05-02 05:04:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4085909d-8845-3e80-b967-20abd0f37c78 | -18.49057 | -51.69115 | 2026-05-02 05:04:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 622be942-e776-3bbe-b286-b8abefeac385 | -17.93186 | -52.89465 | 2026-05-02 05:04:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 387751cf-7dd6-3a6c-b9ea-303adb31e8ab | -21.95728 | -57.59752 | 2026-05-02 05:04:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f7e9c6ef-f06e-35ac-85eb-ec8855fe3af3 | -21.66798 | -56.31391 | 2026-05-02 05:04:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3cd8da65-dbad-30cf-a45b-672b0e482a39 | -18.49805 | -51.69243 | 2026-05-02 05:04:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3fe5a549-f660-34cd-8692-7dc8cb0e6f96 | -21.66739 | -56.31763 | 2026-05-02 05:04:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 17b7e546-94c4-3e51-b95e-3368ac2c73f2 | -21.95792 | -57.5937 | 2026-05-02 05:04:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8c0fb278-ae4c-36e2-80e2-e062aa60e2a2 | -17.92014 | -52.90107 | 2026-05-02 05:04:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b9cffb2b-79f4-3422-96b4-93b130f27937 | -20.2799 | -46.44681 | 2026-05-02 05:04:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 84d3f5e5-4d3b-3442-8fc5-cba67c780b37 | -18.48272 | -48.40324 | 2026-05-02 05:04:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6547bb25-f827-388a-8bbd-718b1acd68e4 | -17.93597 | -52.89115 | 2026-05-02 05:04:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a5bcb189-d966-30ee-9c55-ad874766a840 | -20.19787 | -46.45334 | 2026-05-02 05:04:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7061733b-61a3-3f1a-9aaa-aaaa4d428441 | -19.15592 | -57.55517 | 2026-05-02 05:04:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 211b9578-ab34-36d4-935d-60721ad46c77 | -10.9815 | -45.0874 | 2026-05-02 05:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 2df675bc-46fb-3b3e-9e09-9a69d7fbb274 | -12.3887 | -50.0435 | 2026-05-02 05:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 18db4ea8-7c66-30e1-b94f-351ff672a291 | -12.3696 | -50.0459 | 2026-05-02 05:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 4e4be519-0477-383a-9bae-062f5fbfbec3 | -10.9815 | -45.0874 | 2026-05-02 05:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.7 |
| a0a9d15f-3a91-3c73-a318-eb090c9d0a61 | -12.3887 | -50.0435 | 2026-05-02 05:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 48dd0135-fba8-3059-9f6f-a7fe110aa0dc | -12.3696 | -50.0459 | 2026-05-02 05:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 4bd897d3-13ae-38d5-9a0f-befb5db21188 | -11.44081 | -55.10921 | 2026-05-02 05:21:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0ba8e709-2d07-3ee3-9ad6-db47530c4c9e | -12.28753 | -57.39095 | 2026-05-02 05:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2ac512c3-73d2-3659-a285-dfd8b69a6762 | -12.28807 | -57.39194 | 2026-05-02 05:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bc0b217f-02e1-3539-95c6-b56f11afd6c5 | -12.37707 | -50.04617 | 2026-05-02 05:21:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 519a4f65-72cd-34f2-ae2e-eb25c815ec84 | -12.28451 | -57.39139 | 2026-05-02 05:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8010b0e9-1688-3e86-bd31-8f028608d9d4 | -12.28629 | -57.54851 | 2026-05-02 05:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0a680312-0911-3e77-b79f-f575310fd241 | -12.29108 | -57.3915 | 2026-05-02 05:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a9ed08c-6a11-3264-8ba6-1580029a6002 | -12.29345 | -57.4002 | 2026-05-02 05:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7d1a8ad2-78ba-3827-8106-053d9117a253 | -11.44481 | -55.10981 | 2026-05-02 05:21:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e7b45c63-89a7-3afb-b4fa-2ec75a745ea5 | -11.44881 | -55.1104 | 2026-05-02 05:21:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a407cf02-a16f-3436-a479-84d2a8b9b056 | -12.29997 | -57.40535 | 2026-05-02 05:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 56448b82-14cf-3527-967b-238bf024ca5d | -12.37283 | -50.03352 | 2026-05-02 05:21:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 8e988e22-6252-31aa-9802-cc44f03fd84f | -12.37186 | -50.04147 | 2026-05-02 05:21:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 21684eb8-4eba-38ed-96dd-bee385167832 | -12.29701 | -57.40075 | 2026-05-02 05:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6edc9a46-3b8d-3488-92eb-d7e029d45173 | -8.63735 | -63.99303 | 2026-05-02 05:21:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 22efb352-f7c1-30aa-886b-fdb5dded3c60 | -12.37234 | -50.03749 | 2026-05-02 05:21:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 4d70c4de-b811-387c-904a-326f90dcd9db | -11.55147 | -48.26589 | 2026-05-02 05:21:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2aa10d13-bfc9-395f-9a16-0dbfdea47cd3 | -12.29642 | -57.40481 | 2026-05-02 05:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5135b3f5-04f7-379f-be70-877665def178 | -9.53024 | -63.38247 | 2026-05-02 05:21:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 720a093d-5497-3828-ab31-100d0ea6ca90 | -12.37853 | -50.03426 | 2026-05-02 05:21:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 468a89c6-a742-38b4-9ffd-974b0725e175 | -11.43379 | -55.10095 | 2026-05-02 05:21:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 474d797c-8d85-30dc-9aa8-7a2b1632806a | -12.37804 | -50.03825 | 2026-05-02 05:21:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 5e3daec8-bdbf-3492-b57f-b6990f9247b2 | -11.4493 | -55.10688 | 2026-05-02 05:21:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 661e5b72-8db8-3945-b4dc-ecaefee2e435 | -12.37138 | -50.04544 | 2026-05-02 05:21:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 1d856ad6-5a04-3e55-869b-ec0c641a1739 | -11.43779 | -55.10155 | 2026-05-02 05:21:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 992317e2-2976-3202-9f29-a65d7f9b1f97 | -7.86565 | -61.49533 | 2026-05-02 05:21:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a9cb084a-b13e-338d-82b7-6142a26d72aa | -12.28745 | -57.39603 | 2026-05-02 05:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| afbf30b7-af90-3121-9927-9e8e56519bb6 | -12.29049 | -57.3956 | 2026-05-02 05:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 027c783d-a771-343c-9026-54946c8da7f4 | -12.29404 | -57.39614 | 2026-05-02 05:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README7.md)
