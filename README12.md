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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b6676bb6-f36f-38ad-98d9-97ac78ea6703 | -11.48941 | -45.08984 | 2026-08-26 03:49:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b9972bdb-39b6-3bb8-adc7-66c4757fe649 | -6.41736 | -42.78378 | 2026-08-26 03:49:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 587e8464-deae-3705-93dc-503ddf1c352d | -7.39451 | -38.96444 | 2026-08-26 03:49:00 | NPP-375D | ABAIARA | CEARÁ | Brasil | 2300101 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 0bc884d9-cbad-39c7-b77a-7e9ab1d8302b | -5.92178 | -43.6399 | 2026-08-26 03:49:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e829dea0-e61f-39c4-8904-8782b2d17c15 | -12.77352 | -44.26147 | 2026-08-26 03:49:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed8fc17f-1a7c-3c9c-8347-72086da6efa5 | -11.80091 | -47.64347 | 2026-08-26 03:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7cf5c61c-513d-3e74-b96f-942b6e95b8f0 | -13.37544 | -48.21905 | 2026-08-26 03:49:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 47a5b97b-4084-333c-b77f-acf19d9f4241 | -12.76767 | -44.26365 | 2026-08-26 03:49:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ebfc086-0f9a-35fb-8d63-85233a77045f | -4.80131 | -43.17151 | 2026-08-26 03:49:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2491d433-5066-3cd6-9953-dc8834ec6d9f | -10.9849 | -43.71 | 2026-08-26 03:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 055e8c71-44b4-3fdc-8c71-0fd5fe1543b8 | -12.75813 | -46.46586 | 2026-08-26 03:49:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9ff059ef-c1a9-36f2-a052-626072861731 | -12.72201 | -48.37854 | 2026-08-26 03:49:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 77d95ce6-6b90-35e8-8d37-21163b8fdbf9 | -13.33222 | -48.2277 | 2026-08-26 03:49:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| eea2873a-7993-399e-b7d4-a332937f6247 | -12.02512 | -46.02804 | 2026-08-26 03:49:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e519e94f-3fc3-3a55-9977-ea9043fdf995 | -11.01561 | -45.06873 | 2026-08-26 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 505e188c-3077-3abf-9634-9aa08478d58d | -6.85839 | -38.35059 | 2026-08-26 03:49:00 | NPP-375D | MARIZÓPOLIS | PARAÍBA | Brasil | 2509156 | 25 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 1b11ea87-8906-3933-9b02-279fab10b0a5 | -17.69777 | -40.18212 | 2026-08-26 03:49:00 | NPP-375D | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 805ad7cf-6dee-3728-87bb-c41270559433 | -12.62933 | -48.40811 | 2026-08-26 03:49:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 581cff3c-824a-31ff-b683-6790e87dd7d1 | -12.7637 | -44.25601 | 2026-08-26 03:49:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e8e38cf7-e927-3608-9975-84d1ba21b051 | -11.49426 | -45.09502 | 2026-08-26 03:49:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d876b424-b8c7-3ea6-8696-e2be008845de | -11.01484 | -45.07258 | 2026-08-26 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 74bc8628-c3fe-3c84-be1c-9f8ea3df974a | -6.412 | -42.78312 | 2026-08-26 03:49:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| d59724a4-6795-396c-abbe-995c560a1a83 | -11.3363 | -42.12668 | 2026-08-26 03:49:00 | NPP-375D | UIBAÍ | BAHIA | Brasil | 2932408 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0bb6bbb9-a3cc-3b9c-9f81-d89e11f1a9c4 | -16.03165 | -38.99558 | 2026-08-26 03:49:00 | NPP-375D | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 1a779637-cc38-398c-ba58-8eb9604fc64d | -4.84569 | -44.29796 | 2026-08-26 03:49:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cf688f7b-083a-331d-b473-22fd62ba9916 | -14.79821 | -48.79982 | 2026-08-26 03:49:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| e13320cc-c5b8-3a7a-bda2-532ed3c962ff | -11.42199 | -44.53415 | 2026-08-26 03:49:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8442b940-c09a-3389-a4f1-8722435ab050 | -15.062 | -45.32138 | 2026-08-26 03:49:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6cf56bf8-eb27-39d9-8f72-8d636ae558b0 | -12.76118 | -44.26909 | 2026-08-26 03:49:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bafe79a7-3187-3b6f-bef0-d8a6b2a22025 | -12.69798 | -48.41701 | 2026-08-26 03:49:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 040e481d-be98-387b-8c4b-a59706ba85b4 | -12.02868 | -46.01054 | 2026-08-26 03:49:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eca7f9f8-ea2b-35e4-b343-87f4b2a62f64 | -12.69928 | -48.41854 | 2026-08-26 03:49:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e551a2eb-1531-33f8-8af8-db7ef12a25e8 | -6.8742 | -43.74187 | 2026-08-26 03:49:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8fb44d50-9864-3458-ac21-855aee716db7 | -4.84589 | -44.30375 | 2026-08-26 03:49:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5174faff-f563-3e72-9041-da386975018b | -12.80831 | -42.72752 | 2026-08-26 03:49:00 | NPP-375D | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 4.1 |
| b4eea05d-7bc3-3b16-8dd4-dbcf272f7544 | -11.28794 | -47.07067 | 2026-08-26 03:49:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2327194f-e847-30ff-bf42-4793a2d2ec87 | -11.28041 | -47.07487 | 2026-08-26 03:49:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 64c33c39-ef3b-3451-9aa6-234042b06465 | -12.66813 | -48.42481 | 2026-08-26 03:49:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 4f97f487-fc57-35a7-a8bd-46099bb97abd | -12.02957 | -46.00617 | 2026-08-26 03:49:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fd80e9b3-c565-3074-94ef-fb5ff8d2ec39 | -12.02786 | -46.03393 | 2026-08-26 03:49:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 09dc3955-381e-3a5f-a490-81d041f3b342 | -4.87592 | -44.30927 | 2026-08-26 03:49:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6de9b4b6-9712-3af8-9dd2-06a8fade58bc | -5.92042 | -43.64775 | 2026-08-26 03:49:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3fe0fd67-867e-3b0b-8dbf-f62bf79f7a10 | -12.6362 | -48.40898 | 2026-08-26 03:49:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ff80045c-1a6e-315c-9d82-5898d1ee03c4 | -10.91148 | -44.74036 | 2026-08-26 03:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 52a4517d-0e2e-3c92-92b7-81dd9db74d76 | -12.72596 | -48.3842 | 2026-08-26 03:49:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 80b6bccf-4ce4-3163-bf2f-90f353d2baa5 | -4.80691 | -43.17244 | 2026-08-26 03:49:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 56fa2551-9a13-37df-b836-7567ced14851 | -6.87354 | -43.74563 | 2026-08-26 03:49:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7066ba6c-c2cc-33c3-8244-a64dee7d4202 | -17.78127 | -47.09372 | 2026-08-26 03:49:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aa574a60-622a-30a7-9574-0e414927025f | -11.79989 | -47.63915 | 2026-08-26 03:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dcad9c65-b545-389b-a0b4-8d2e2745ab8e | -6.88693 | -43.7502 | 2026-08-26 03:49:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0db1972c-a98c-3865-9c5e-398737a3ebb1 | -11.01476 | -45.06502 | 2026-08-26 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 606facb1-cfe2-3603-9ff0-ba7b2dae71b0 | -12.02958 | -46.02516 | 2026-08-26 03:49:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 58bfe509-1fb8-349f-ab23-1c057f6bec6c | -6.95138 | -42.68586 | 2026-08-26 03:49:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| a3209817-e561-3b69-a921-4be34d491ad9 | -12.03697 | -46.03051 | 2026-08-26 03:49:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 653d54f8-3e3a-3357-b540-0c66f2729423 | -12.76618 | -46.45701 | 2026-08-26 03:49:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a529f5a7-11e3-3ab0-99e9-0a812ac80a5f | -6.94619 | -42.68407 | 2026-08-26 03:49:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 249c69f9-f577-39cb-9ae3-6bab7ce435bb | -6.41794 | -42.78057 | 2026-08-26 03:49:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 42addf1c-905b-3fd0-b5e9-220329b1fe42 | -11.81803 | -47.66027 | 2026-08-26 03:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 011cfe19-0865-323d-9149-386158d6f027 | -13.3587 | -48.20049 | 2026-08-26 03:49:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6fb1bb3e-8228-3454-b0c7-a476eb6830a8 | -12.02188 | -46.01363 | 2026-08-26 03:49:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 9a54d2ee-69e3-34f2-a5e8-dcdf679f870e | -6.87641 | -43.74434 | 2026-08-26 03:49:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4e5074a8-8c22-326d-940b-9350cf381be0 | -11.63816 | -47.15788 | 2026-08-26 03:49:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4ef838b6-9a1e-3af9-8d7b-b28ce23232c8 | -5.9171 | -43.64615 | 2026-08-26 03:49:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e43eafec-fda2-32e5-94c3-ee3c9b4a5038 | -12.71514 | -48.37777 | 2026-08-26 03:49:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 36130fc4-29d9-36d4-a85d-178cc8830dce | -12.66319 | -48.41481 | 2026-08-26 03:49:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a6c46dd7-8193-3b61-8046-fdd119f59a97 | -18.94588 | -41.01784 | 2026-08-26 03:49:00 | NPP-375D | ALTO RIO NOVO | ESPÍRITO SANTO | Brasil | 3200359 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 9dccc1b8-218f-30ca-94c3-10c236d09542 | -6.88133 | -43.74914 | 2026-08-26 03:49:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 914cacae-da4e-3995-a505-e459a77ee7bf | -11.42539 | -44.54599 | 2026-08-26 03:49:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a84be6b8-3f9a-387b-939e-63ccf3274d35 | -11.42402 | -44.55316 | 2026-08-26 03:49:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c1a854ca-a0a4-330b-a36f-ccf9ddda0684 | -7.09035 | -42.17634 | 2026-08-26 03:49:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3dae7d29-d936-38cc-9a9e-ee2ddc27f4fa | -13.33559 | -48.21189 | 2026-08-26 03:49:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2158c4f6-33af-30c9-84a3-734749c68cd2 | -5.34845 | -45.16399 | 2026-08-26 03:49:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b0b4aa66-f398-30e6-8a63-4e0939e8cec1 | -15.76527 | -43.37513 | 2026-08-26 03:49:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f5e99d82-04f2-328b-a51a-af9d99de251b | -13.3578 | -48.23727 | 2026-08-26 03:49:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| d4104311-7851-3efb-bcc4-f26403bb353e | -12.67928 | -48.40537 | 2026-08-26 03:49:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 12206b81-cd8e-30b5-8c72-1323b3aedf98 | -6.24073 | -44.80017 | 2026-08-26 03:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 58d3d1eb-32db-3951-8bd7-06afd8d287ef | -6.24054 | -44.80175 | 2026-08-26 03:49:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f9671b38-2368-3571-917e-78182c6141ce | -12.73608 | -46.4818 | 2026-08-26 03:49:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7b5e01b3-c7c0-30e6-99d5-8338f61765b7 | -12.68507 | -48.41133 | 2026-08-26 03:49:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1b461959-34e7-34d6-ab8a-5eea82695abd | -13.33801 | -48.20057 | 2026-08-26 03:49:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1deb4656-91a4-39a3-8753-ac4fd5138dbc | -12.76813 | -46.44734 | 2026-08-26 03:49:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f320a624-a200-329a-8ca8-6d79f443f4df | -7.1405 | -42.77157 | 2026-08-26 03:49:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ce1c2a60-c7ca-3131-a040-2c55c5402469 | -11.37965 | -45.15915 | 2026-08-26 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 954d3755-81d5-3c32-9bd2-4bf872eacc5b | -12.66977 | -48.41705 | 2026-08-26 03:49:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3c772ae6-1000-37c1-a687-b65130a76a91 | -12.02277 | -46.00927 | 2026-08-26 03:49:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 2397d78b-a4c7-3a96-8383-53410d71195f | -6.87917 | -43.74657 | 2026-08-26 03:49:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 409200ad-743e-3b1b-be17-d18715112ef4 | -12.68308 | -48.42083 | 2026-08-26 03:49:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a38c6f8b-616c-3250-b6ec-3f1f6fea840c | -11.37887 | -45.16315 | 2026-08-26 03:49:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2c9b49d5-e36f-3cd4-bd2c-605f9a0a8097 | -17.69405 | -40.18142 | 2026-08-26 03:49:00 | NPP-375D | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 15.2 |
| c89e9b2b-17de-3fd5-8d9e-6c32ba7cc8f0 | -12.7651 | -46.46239 | 2026-08-26 03:49:00 | NPP-375D | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 17aa1bea-faad-3f70-84f2-bd6990dbf74f | -12.76181 | -44.26582 | 2026-08-26 03:49:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f07a91a1-48a4-3ecf-8cc5-b1de5e591b3a | -14.03518 | -43.85173 | 2026-08-26 03:49:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e0e17671-301a-3360-b411-d420a84c2775 | -6.94615 | -42.68491 | 2026-08-26 03:49:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| aa7dbff9-0eed-3e76-9e72-f3feea45a9f2 | -12.75318 | -46.45935 | 2026-08-26 03:49:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 17e4063e-f258-3a1f-b1c4-bac59fffff3b | -12.03465 | -46.03078 | 2026-08-26 03:49:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c204819d-59d3-365e-97ae-f0c2b698277d | -12.03015 | -46.03369 | 2026-08-26 03:49:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 81689ac9-ad13-341f-9e69-10eff7f99d1a | -12.76113 | -46.45105 | 2026-08-26 03:49:00 | NPP-375D | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ad9c554c-9fd8-3da0-bf43-2b7d96e9f99d | -15.0597 | -45.32284 | 2026-08-26 03:49:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 96244fc0-87ff-3c1c-ab19-7de1248a01a4 | -11.82351 | -47.65709 | 2026-08-26 03:49:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ab577129-c016-3d49-b109-920599c01ca3 | -7.09087 | -42.17345 | 2026-08-26 03:49:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README13.md)
