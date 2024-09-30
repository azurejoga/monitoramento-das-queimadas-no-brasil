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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e1f1e82a-dc64-36b2-95c2-ddb947a23782 | -10.96248 | -46.47663 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bfb75e6e-e6f9-34f1-b8d8-2964fbd85d7b | -10.9611 | -46.47321 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ceb0f293-5ced-3901-aed5-56303c708c79 | -10.95994 | -46.41028 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d469276d-eeee-369c-ab6a-397311e0a941 | -10.95704 | -46.40595 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cf5ebfee-9d67-38de-a33f-f049206d1c01 | -10.95531 | -46.3938 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5863bea-d3c9-3596-923f-cc94828530ff | -10.95416 | -46.47214 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 42d7f315-b6eb-3a78-95ac-8e3fc2207f2d | -10.95414 | -46.40156 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5b0f502a-b4f3-354f-a418-a8092764e875 | -10.95127 | -46.46777 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 340878b2-ee7e-3ac9-a729-6b8f571ae142 | -10.9507 | -46.47161 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e3423474-dc05-3d6d-9dd1-31f09b349b10 | -10.9358 | -47.30463 | 2024-09-30 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 30992b7a-4808-34d0-864d-655fa960a188 | -11.34559 | -46.27625 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4c554c70-0ad0-38fe-965d-a5abef56eaa5 | -11.31215 | -46.1824 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a5af9750-479d-32a7-8475-105bc9d3f3f6 | -11.30924 | -46.17778 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 22ae3f3a-f8d1-3976-b4b7-2fbd387eb05c | -11.30632 | -46.17322 | 2024-09-30 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6fbca7d0-271b-3c7e-9759-476dc42d95e6 | -10.9803 | -46.45206 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3c288b6f-bb29-3311-af14-cae98d29ce16 | -10.97975 | -46.45577 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 768a6a11-69fe-3c41-b078-dc16fd5db227 | -10.97919 | -46.45953 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 60e885ca-eb1d-32e7-a5cd-28258f200ff8 | -10.9785 | -46.44019 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ee4569d-bda5-3d78-84d6-fcfbc6d3ebd6 | -10.97794 | -46.444 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9daa3619-d45b-3fdf-90f2-9acb897a28cd | -10.97739 | -46.44773 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1291e3b3-649e-3b18-a6d8-a01bfbb40a1a | -10.97684 | -46.45142 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8babb54a-7975-3f97-85cc-4943f1c9df69 | -10.97573 | -46.45895 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 923bce93-b267-321d-9537-38b1fd6b6bbb | -10.97516 | -46.46277 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4f3838df-b247-348c-b56c-0b0c789bfee1 | -10.97328 | -46.42737 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 855919e0-e1ee-346f-928f-6a1a36231945 | -10.97152 | -46.42777 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 143a4ffd-d3ec-3ead-9f22-e697f86b5598 | -10.96702 | -46.44571 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1e56e721-70df-34ab-ac5d-56ff7caf0b1d | -10.96305 | -46.47276 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a3e5c23-65a1-3ac0-8fdc-5f3239f3c986 | -10.96286 | -46.46161 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6788209c-1a5e-3b19-96bd-dd499b48560f | -10.96285 | -46.41457 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 78a9d83a-0852-3487-9260-bcefd02a9565 | -10.96051 | -46.47707 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 76f13491-1725-3c09-bc96-e45fea694850 | -10.96051 | -46.40648 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8e1775d5-2bf7-39d4-9895-5e657d718d25 | -10.95763 | -46.47268 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3ab7f2b6-f51f-3fdf-9403-ad69913e8fde | -10.95473 | -46.39768 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3da887d2-fda6-3ea3-814e-c1029f414f12 | -10.95243 | -46.38931 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 51ba9caa-3704-3026-8c5d-3a16136c05e9 | -10.95185 | -46.39318 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1110c636-dbbc-3ae0-9ebd-0d6d6443461b | -10.9478 | -46.46726 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c392fda4-ee39-3e70-a98b-2875b9c817d4 | -10.93451 | -46.46129 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 99a3f2f0-93c6-3806-a205-03d9855cec0e | -10.92064 | -46.45913 | 2024-09-30 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| de0416b7-6e82-3217-8d30-ee58130f97d7 | -11.82332 | -47.6193 | 2024-09-30 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8f9fcf00-2fc2-3934-8eda-2f1436bc73ea | -11.82276 | -47.62293 | 2024-09-30 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1bf20674-79ed-35d9-a956-fbe228adb04b | -11.82221 | -47.62656 | 2024-09-30 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2aea14be-f6cf-3a03-9dae-525ff4c0e278 | -11.81829 | -47.62968 | 2024-09-30 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 06ba8bdf-d63d-3a69-ad29-d3409c8474a7 | -11.81322 | -47.61773 | 2024-09-30 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 71fab940-95df-3c87-b8bb-df42a2738cb3 | -11.80759 | -47.60941 | 2024-09-30 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2db71ff8-f6bc-33c2-8037-fc95a5904d72 | -11.80704 | -47.61305 | 2024-09-30 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 90c7ef35-8c14-3585-a5b8-edb7e403ab26 | -11.80312 | -47.61615 | 2024-09-30 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a22e507a-0ef1-3a66-94ca-78c88294471e | -11.80196 | -47.60111 | 2024-09-30 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 88faf481-3e5a-3a1b-9269-d0b4058f1214 | -11.79859 | -47.6006 | 2024-09-30 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0d177c41-fed7-3ccb-b339-ed658234193f | -11.79522 | -47.60008 | 2024-09-30 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 502818be-5805-30b7-a4c9-5bf677144ce4 | -11.79467 | -47.60371 | 2024-09-30 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 02847cef-8bba-3357-a2dc-ffa3eb37d4ad | -11.79131 | -47.6032 | 2024-09-30 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 50192fb2-f609-3051-942a-5556b456209a | -11.78794 | -47.60268 | 2024-09-30 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 67fc69b0-1519-3d0c-ae42-ffb7423fe998 | -11.78739 | -47.60631 | 2024-09-30 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 530799a7-f161-3a93-bb5b-dcd943736834 | -11.78457 | -47.60216 | 2024-09-30 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5f463898-b592-32e1-bf4a-b6e1d57399f8 | -11.78403 | -47.60578 | 2024-09-30 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 965bdd4b-f2b8-33ad-8799-84e87e482663 | -11.78348 | -47.6094 | 2024-09-30 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| da1e0ee8-e65e-3672-9225-c3b86bebe271 | -11.78066 | -47.60525 | 2024-09-30 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3652aa6c-ef66-311d-8ae6-130be70f2d47 | -11.78018 | -47.63121 | 2024-09-30 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e07f3f27-f7c1-3d29-98d2-3461c29341ec | -11.78011 | -47.60888 | 2024-09-30 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8bf73553-dc25-3a85-b8ce-27afc41cde26 | -11.77675 | -47.60835 | 2024-09-30 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c93b9cfb-fedb-3969-bef3-af330e7b84d5 | -11.7762 | -47.61198 | 2024-09-30 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ae1489a8-0de9-31c5-9408-33b33d2c50be | -11.77565 | -47.6156 | 2024-09-30 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e594b60d-9dfc-33b3-91cd-39871c32946f | -11.76296 | -47.67675 | 2024-09-30 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a748cb01-204c-3744-922f-dd446ea02e2e | -11.62058 | -46.80556 | 2024-09-30 04:32:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f46686ad-1345-3599-b7c9-455edf5133d1 | -11.62 | -46.80942 | 2024-09-30 04:32:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1e08bed-5d9d-3769-862b-7ff316011e0c | -11.56831 | -47.44984 | 2024-09-30 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 42b1bbd9-eb06-392a-b0da-2c759b0b355f | -11.56775 | -47.4535 | 2024-09-30 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0d37f1e2-a817-33ec-9cbe-f0ed47977f8b | -11.56493 | -47.44933 | 2024-09-30 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 483f7fe5-794a-30d3-9e33-6c83c098ce4b | -11.56044 | -47.45612 | 2024-09-30 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ffa3e005-49b2-3b73-a8b3-1f6ec08d3b51 | -11.55988 | -47.45977 | 2024-09-30 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 37acae60-631c-3373-823f-0faf0d63cb8d | -11.49321 | -47.32929 | 2024-09-30 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c82b1ef6-99c0-330c-8339-bd1f5d3e7aeb | -11.48872 | -47.33614 | 2024-09-30 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fad58e2e-5c92-342d-b5d2-ac07eff3aa8b | -11.48816 | -47.33982 | 2024-09-30 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 26cb3aec-655c-3a03-b3f5-b05dc4b746eb | -11.48423 | -47.34297 | 2024-09-30 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc04707c-ad8c-3661-8ec5-505e4207d718 | -11.48309 | -47.34328 | 2024-09-30 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f47ccb13-fbee-3056-b0a9-c948eca90597 | -11.4814 | -47.33174 | 2024-09-30 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 303a998c-7f4f-3c9e-9bf2-6626535894bb | -11.47801 | -47.33122 | 2024-09-30 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f785f31b-20af-37c1-831d-7b4804e7fc94 | -11.47745 | -47.3349 | 2024-09-30 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7df5fb21-a927-346b-bfec-c7b33e1e7ea1 | -11.45083 | -46.95816 | 2024-09-30 04:32:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| b6b88bc3-2eb3-36cc-850a-15400553f548 | -11.45026 | -46.96203 | 2024-09-30 04:32:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 20398b12-b998-3b8e-891a-39e31d680ca0 | -11.44971 | -47.24385 | 2024-09-30 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 155436cf-d474-3e6d-a374-a2f3522614d0 | -11.44915 | -47.24753 | 2024-09-30 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e0c3f143-427d-3a82-b3d4-9051a9b6880d | -11.44741 | -46.95766 | 2024-09-30 04:32:00 | NOAA-20 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| f772da4b-a758-3f88-86a0-3569f7a19d7c | -11.41691 | -47.23119 | 2024-09-30 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 63384b3f-3b98-37e6-8329-595de543837a | -11.41407 | -47.22697 | 2024-09-30 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1ef768c1-90ab-3999-814f-906a19f17f6c | -11.41352 | -47.23067 | 2024-09-30 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0cf1352e-d8a1-3bb5-9a03-2ab496c16feb | -11.41068 | -47.22644 | 2024-09-30 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a5aab89c-e757-32e2-9849-338db8702e77 | -11.40729 | -47.22592 | 2024-09-30 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 84d1e965-a345-3f4a-a2ee-b4b75a4c8d8c | -11.40674 | -47.22961 | 2024-09-30 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ee023581-a752-30e3-a2dc-cb8f1c915a20 | -11.40334 | -47.22909 | 2024-09-30 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8478d04d-3af5-3494-aa2a-47b37fc62868 | -11.40279 | -47.23279 | 2024-09-30 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d40e6db6-3224-3d30-b4de-bea8a3a8bd4a | -11.40223 | -47.2365 | 2024-09-30 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0929c9c6-fc6f-3287-be64-10c658af1e4c | -11.39995 | -47.22857 | 2024-09-30 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d935ce0d-913c-3afc-8f55-d2f9d64a8f5c | -11.3994 | -47.23227 | 2024-09-30 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ece3fe48-51b5-3c5d-a054-df94fc72b0ce | -11.39884 | -47.23598 | 2024-09-30 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 10a259e9-a405-30aa-8c59-946de45f4c30 | -11.39545 | -47.23546 | 2024-09-30 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 94488308-a97d-3e26-b540-ddf3f641b9bc | -11.39323 | -47.25027 | 2024-09-30 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a52bd1b7-1c55-3cfc-9d3a-de3fc4dfb2ef | -11.38984 | -47.24974 | 2024-09-30 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4fe36e8b-e681-3ac0-a7c2-6745e999a3ed | -11.38929 | -47.25343 | 2024-09-30 04:32:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 636d4b77-40c6-3972-b5e7-7c43a5e4e26f | -11.32938 | -46.85939 | 2024-09-30 04:32:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README39.md)
