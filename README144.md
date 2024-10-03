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

## Dados Diários - Página 144

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 595d6b13-387b-30d9-8f16-3fe628d50717 | -17.11899 | -47.13567 | 2024-10-03 04:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 14.0 |
| b74e649e-a252-37ef-b774-11e335696fda | -17.11751 | -47.13097 | 2024-10-03 04:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 90001aaa-4695-35bc-a992-31a9560ad87f | -17.11693 | -47.13614 | 2024-10-03 04:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 15492faf-ef05-35b7-9a32-8525040a48aa | -17.11473 | -47.13028 | 2024-10-03 04:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5dd592cf-2958-3cb1-b141-bb2e7be14eeb | -17.11412 | -47.13531 | 2024-10-03 04:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 49aca081-fe16-32bf-995e-fef47d9b33bd | -17.11263 | -47.13076 | 2024-10-03 04:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| fd89bb5a-5405-375c-9992-5ec2f84c42c2 | -17.11205 | -47.13576 | 2024-10-03 04:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 6cfa1fe6-5beb-320f-a497-2677b0a8d5e7 | -17.10985 | -47.12997 | 2024-10-03 04:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 77b73c77-f08b-3cf7-ae23-989bd158f6a0 | -17.10924 | -47.13499 | 2024-10-03 04:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 0351224b-7cc6-32f6-9f34-e4a1f82d7016 | -17.10776 | -47.13036 | 2024-10-03 04:53:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 41c5e889-ab05-3ba6-8a5a-f5565cb1f1c8 | -18.81682 | -46.63539 | 2024-10-03 04:53:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8c11f440-940c-3d4f-9956-bab99a4127ca | -18.8117 | -46.63482 | 2024-10-03 04:53:00 | NPP-375D | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a5547b20-182d-3eb9-8c4b-033bdc44f56e | -20.63797 | -46.73931 | 2024-10-03 04:53:00 | NPP-375D | PASSOS | MINAS GERAIS | Brasil | 3147907 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f9f1d6d7-c299-3664-ad7f-5d21d0fe9e35 | -19.62199 | -47.17092 | 2024-10-03 04:53:00 | NPP-375D | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 25ee2805-96d3-334e-a87e-115e96efdc14 | -19.61699 | -47.17043 | 2024-10-03 04:53:00 | NPP-375D | ARAXÁ | MINAS GERAIS | Brasil | 3104007 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f1ab1b1b-66bd-3659-80f8-750fc9d5d44f | -21.89204 | -48.47753 | 2024-10-03 04:53:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 23438542-254d-3103-bdf6-68ffa32272ff | -21.88675 | -48.48221 | 2024-10-03 04:53:00 | NPP-375D | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c7a7e410-c439-3503-81b2-6e1c9ddd773e | -15.73231 | -48.38532 | 2024-10-03 04:53:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d06ef928-5f2b-3674-8362-85f9d44e8a0f | -15.85866 | -48.54721 | 2024-10-03 04:53:00 | NPP-375D | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e465393d-23a7-3058-8ddf-b2a8ae9cf1c5 | -15.8581 | -48.5515 | 2024-10-03 04:53:00 | NPP-375D | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9c483dd5-2b66-30bb-8c45-603a71cb0059 | -15.73665 | -48.38615 | 2024-10-03 04:53:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| db57d62a-53fe-3d52-940d-2ac602cf178b | -17.73796 | -48.44428 | 2024-10-03 04:53:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 09f0ca21-5101-3d18-84cf-7d451b030e24 | -17.74686 | -48.44578 | 2024-10-03 04:53:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 30abc202-87d9-30a7-99f5-773591c49897 | -17.74632 | -48.45032 | 2024-10-03 04:53:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0481724c-636c-36b3-9578-77bafb1d4ae6 | -19.09233 | -48.04876 | 2024-10-03 04:53:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5e2ee64a-5561-37f9-ba23-91e5628e92e7 | -19.08766 | -48.04811 | 2024-10-03 04:53:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e9ec1173-2667-34f9-8119-b8c7bd4929ba | -19.08705 | -48.0533 | 2024-10-03 04:53:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f50bba62-a66d-3265-a0e4-0024c2ebdc54 | -18.78836 | -47.99413 | 2024-10-03 04:53:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 75986bd7-6f04-36e5-b88b-2da6ffb1c7c2 | -18.78776 | -47.99925 | 2024-10-03 04:53:00 | NPP-375D | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 73370e70-5187-30f9-84e2-2d49b906f4af | -19.09352 | -48.27787 | 2024-10-03 04:53:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 767dcdb5-6725-362c-8bd4-ee298a2cd575 | -19.08893 | -48.27723 | 2024-10-03 04:53:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 50abc0bb-71c7-37da-8cb6-ab4475fe1970 | -18.62148 | -49.1898 | 2024-10-03 04:53:00 | NPP-375D | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0195a85f-51e6-34e1-9d0f-4863661ea8bb | -18.61718 | -49.18915 | 2024-10-03 04:53:00 | NPP-375D | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 1be3b175-f38a-3b55-80d3-92bb76f9f3e1 | -20.5727 | -49.62167 | 2024-10-03 04:53:00 | NPP-375D | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b8b1a9f7-0d73-3871-a654-a2d5f20ae998 | -21.23738 | -49.41237 | 2024-10-03 04:53:00 | NPP-375D | IRAPUÃ | SÃO PAULO | Brasil | 3521507 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 46e8c0e8-c245-3a0e-8fd3-0a63036ac109 | -16.10818 | -50.27275 | 2024-10-03 04:53:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| adea6232-d799-385a-ba8b-b3c0006c7ca3 | -16.1075 | -50.27781 | 2024-10-03 04:53:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 45b8bcce-3682-3d43-83ea-d0b4e539b466 | -16.10737 | -50.30824 | 2024-10-03 04:53:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ac2382c7-0de1-3a26-a6fe-be33ff926eea | -16.10493 | -50.26741 | 2024-10-03 04:53:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fb831337-3d32-3a3b-ac2b-e238c2913805 | -16.10425 | -50.27247 | 2024-10-03 04:53:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a49057a0-4166-3be1-b622-78f5fe1b40c6 | -16.10357 | -50.27751 | 2024-10-03 04:53:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| de7ac12f-2458-3e0a-9bc2-e2db96dda283 | -16.10166 | -50.26218 | 2024-10-03 04:53:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 72a824cd-2de0-336e-8404-bc502ed95adf | -16.10098 | -50.26732 | 2024-10-03 04:53:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 21ebf7dc-0d8c-342a-8b12-03fdac3f21b5 | -16.09963 | -50.27739 | 2024-10-03 04:53:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 3b8b2a8b-6cfb-3e58-893f-7fdc7d78ab71 | -16.0977 | -50.26213 | 2024-10-03 04:53:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a83ea0f3-8316-3586-8541-03d4f44f8800 | -16.09314 | -50.26663 | 2024-10-03 04:53:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ce23be60-1049-3b80-a906-0bdaffcde39c | -16.09182 | -50.27649 | 2024-10-03 04:53:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ee93e0cb-69db-33b2-a4fe-b99bdf27c608 | -16.08797 | -50.27567 | 2024-10-03 04:53:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4c4b9417-6fbe-33d7-837a-6c7676842546 | -16.08739 | -50.27906 | 2024-10-03 04:53:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e2b24e88-6c7f-3714-9482-83ff0f62da6c | -16.08729 | -50.28074 | 2024-10-03 04:53:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 522587bc-1c63-3713-befa-76c2dae74b52 | -16.08665 | -50.28433 | 2024-10-03 04:53:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3c43e036-f347-33e1-82a3-e3aa37079d2f | -15.92335 | -49.98861 | 2024-10-03 04:53:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3acbe84f-236d-38bf-ad6f-a9a2d38f2ce2 | -15.90821 | -50.16197 | 2024-10-03 04:53:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 880bbf62-cc1e-3009-9816-d3e14efe1b9a | -15.90757 | -50.16671 | 2024-10-03 04:53:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dada8315-d051-3581-be23-52584e22f322 | -15.90431 | -50.16138 | 2024-10-03 04:53:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a417057a-7fcb-3861-ab39-a5d860164eae | -15.90366 | -50.16617 | 2024-10-03 04:53:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| adbbed09-3549-38cb-8743-6a7e1e8c130b | -15.89974 | -50.16578 | 2024-10-03 04:53:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2e639f84-fd6c-3a3a-ab82-5bb8b70d5d10 | -15.89581 | -50.16537 | 2024-10-03 04:53:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d6a8df63-6fec-387a-99dd-b52c40e344a1 | -15.89453 | -50.1451 | 2024-10-03 04:53:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1441221f-a1ef-3a23-8b56-db04431eb89c | -15.89387 | -50.15011 | 2024-10-03 04:53:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e4e6055-d80e-3cdf-bd09-bee00beecb05 | -15.89321 | -50.15504 | 2024-10-03 04:53:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4a784d64-21c7-300f-af11-92f1200acbe0 | -15.89256 | -50.15991 | 2024-10-03 04:53:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 792a3921-ff5f-396a-9907-b0b17534ad90 | -15.89191 | -50.16479 | 2024-10-03 04:53:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8516097a-5eb9-36ef-b1cf-01c9b288cec2 | -16.42165 | -49.92704 | 2024-10-03 04:53:00 | NPP-375D | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7ec2fbbb-0505-3ef3-9daa-962d616effdb | -17.16354 | -49.21543 | 2024-10-03 04:53:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 885e3e85-f42e-3875-9baa-e7cd830d0bb7 | -17.15882 | -49.2187 | 2024-10-03 04:53:00 | NPP-375D | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7f8c7ffc-8f19-3733-bc37-91f1a6eb4f9a | -16.80442 | -50.12206 | 2024-10-03 04:53:00 | NPP-375D | PALMINÓPOLIS | GOIÁS | Brasil | 5215900 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5de9b2ce-7c20-312d-bceb-210a768216c7 | -16.80369 | -50.1275 | 2024-10-03 04:53:00 | NPP-375D | PALMINÓPOLIS | GOIÁS | Brasil | 5215900 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8bfd9979-9b7d-35ca-9db6-e0737707cfbc | -16.79973 | -50.12689 | 2024-10-03 04:53:00 | NPP-375D | PALMINÓPOLIS | GOIÁS | Brasil | 5215900 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 50a2947a-00f5-3f08-b111-86c285e16250 | -16.10133 | -50.4403 | 2024-10-03 04:53:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 72a8563b-3070-36f0-bf49-b8619905904c | -16.11828 | -50.43123 | 2024-10-03 04:53:00 | NPP-375D | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 95c3a65e-1e89-317a-9ed8-454909685783 | -16.11754 | -50.43665 | 2024-10-03 04:53:00 | NPP-375D | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9613b0e0-3a02-33e5-913c-c71bfd9357dd | -16.09918 | -50.39817 | 2024-10-03 04:53:00 | NPP-375D | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7f7dd480-6143-34ec-b449-08955e1a44ed | -16.11363 | -50.43647 | 2024-10-03 04:53:00 | NPP-375D | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 63049dc2-dc88-3d99-8c0b-c6843303a738 | -16.67208 | -50.59843 | 2024-10-03 04:53:00 | NPP-375D | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 31418748-37c5-392b-9074-fceb8ada88ca | -16.66824 | -50.59786 | 2024-10-03 04:53:00 | NPP-375D | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a869de39-5f79-30f2-aa17-b858226b55b5 | -16.66757 | -50.60268 | 2024-10-03 04:53:00 | NPP-375D | AURILÂNDIA | GOIÁS | Brasil | 5202601 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e6840187-154a-3a09-8698-b73b71c24b39 | -16.44987 | -51.06135 | 2024-10-03 04:53:00 | NPP-375D | IPORÁ | GOIÁS | Brasil | 5210208 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 642859fb-dbdb-3da0-a380-6067b83c9947 | -16.18084 | -51.09458 | 2024-10-03 04:53:00 | NPP-375D | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 49c137ab-215c-36f9-83a1-cbb1d8b357f6 | -16.18006 | -51.09245 | 2024-10-03 04:53:00 | NPP-375D | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0cbea060-2c84-373a-a76d-84682235f536 | -16.11296 | -50.44142 | 2024-10-03 04:53:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fd520101-0d53-38ff-a2ac-1a88251b0047 | -16.10906 | -50.44118 | 2024-10-03 04:53:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 10aa6452-c8d4-3f5a-b78c-ac69c322d956 | -16.10585 | -50.43595 | 2024-10-03 04:53:00 | NPP-375D | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 9992db4d-7c1e-3e09-868c-0cc6f5b1e60f | -16.10517 | -50.44091 | 2024-10-03 04:53:00 | NPP-375D | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 01e9b904-4361-3988-939a-d3afaed196b2 | -16.10306 | -50.39856 | 2024-10-03 04:53:00 | NPP-375D | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 251be55d-9a33-3e6d-a775-b59d75a4c7a8 | -16.10252 | -50.37346 | 2024-10-03 04:53:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c8f01ce9-8142-32a1-898b-57d2357591ca | -16.10199 | -50.43542 | 2024-10-03 04:53:00 | NPP-375D | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 72a951ef-4c97-34ae-a9d2-8ac8429d3472 | -16.09865 | -50.37291 | 2024-10-03 04:53:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 81b22955-5164-3f03-a3e4-21304e8712bd | -16.09814 | -50.43486 | 2024-10-03 04:53:00 | NPP-375D | BURITI DE GOIÁS | GOIÁS | Brasil | 5203939 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fb63043c-aedd-35b5-9265-510a035f0154 | -16.09478 | -50.37237 | 2024-10-03 04:53:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6f34422d-edba-374f-ae77-d0165aaa3b84 | -16.09091 | -50.37182 | 2024-10-03 04:53:00 | NPP-375D | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 385bd5c1-9ac7-329e-b7f8-1bada0e30380 | -16.08738 | -50.42722 | 2024-10-03 04:53:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2fcb02db-b63c-3d9a-b197-5ff2cf71bec6 | -16.0836 | -50.42612 | 2024-10-03 04:53:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6eb0c2ee-bf9b-3350-b4f7-4534a5e4512b | -16.08135 | -50.32533 | 2024-10-03 04:53:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8b429f93-cce6-31e6-aeb9-6934d5bd0962 | -16.08115 | -50.32365 | 2024-10-03 04:53:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c3adb4d2-f5f3-3a90-9059-500ff3205bae | -16.08071 | -50.33012 | 2024-10-03 04:53:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 916c9e5a-dbff-3971-a7e6-35489943d4b2 | -16.08048 | -50.32843 | 2024-10-03 04:53:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 50772668-5f2c-3956-ac7b-22329ad45fc9 | -16.07817 | -50.31955 | 2024-10-03 04:53:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f3f990cd-aa01-3ce5-b8dd-375ff9e98811 | -16.07801 | -50.31787 | 2024-10-03 04:53:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 85b575f6-817e-3b7a-b6cd-7c4b5c6c221f | -16.07752 | -50.3244 | 2024-10-03 04:53:00 | NPP-375D | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |


[Clique aqui para ver as próximas entradas](README145.md)
