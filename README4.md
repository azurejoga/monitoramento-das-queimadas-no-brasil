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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 614db4f4-f285-3f12-bba4-f812ed9f986a | -4.7767 | -45.3237 | 2025-09-03 00:24:00 | METOP-C | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| af1079e3-80c0-351f-bd2d-f237a3041045 | -7.9014 | -46.472099 | 2025-09-03 00:24:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 12d7706a-f864-39f9-b602-ceb88067fe14 | -6.4531 | -44.673302 | 2025-09-03 00:24:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 376f562a-4826-3703-8ae4-be873426312f | -7.7068 | -48.749599 | 2025-09-03 00:24:00 | METOP-C | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| fd7a1c13-70ef-3257-9248-8216401c0e46 | -12.8771 | -48.033901 | 2025-09-03 00:24:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cb019746-515b-3408-b209-36bad15c907f | -5.4725 | -51.220402 | 2025-09-03 00:24:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7efefe05-5999-3b8f-8739-c7980b694626 | -8.0645 | -45.366402 | 2025-09-03 00:24:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| da407a96-5d8d-3d61-91c5-40e5b51df9b4 | -13.9024 | -48.102901 | 2025-09-03 00:24:00 | METOP-C | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 57f9d187-d2aa-3330-8dbc-2c5ce86c3397 | -9.5086 | -48.885502 | 2025-09-03 00:24:00 | METOP-C | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ec82cbae-b2a6-39da-b628-3a03deb1dddc | -3.2284 | -47.1213 | 2025-09-03 00:24:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb57fc82-9677-3d16-bb2a-633f8b613014 | -6.2388 | -42.632801 | 2025-09-03 00:24:00 | METOP-C | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4928855d-80bd-302d-bc32-4cda0ad2ce04 | -5.4409 | -42.840199 | 2025-09-03 00:24:00 | METOP-C | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| af4f2951-f165-38c6-81fd-398695e917ff | -6.0249 | -46.005001 | 2025-09-03 00:24:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 36957b2c-f539-388a-84ec-7b27502f68d9 | -6.4626 | -49.528099 | 2025-09-03 00:24:00 | METOP-C | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82fd51b6-7d23-31e7-9244-423aeb5bc549 | -6.3377 | -45.658298 | 2025-09-03 00:24:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 820af4d6-7979-37f6-aa9b-9951d9ad0d3b | -6.2685 | -44.498299 | 2025-09-03 00:24:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| afac6c20-7a98-31a5-9339-7c212f415125 | -5.6132 | -45.013699 | 2025-09-03 00:24:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 18189835-0cea-3023-b5e6-a831957d5e9e | -6.8273 | -44.776199 | 2025-09-03 00:24:00 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 20e27954-de5f-3151-96c5-08a44800c3d2 | -5.681 | -45.9431 | 2025-09-03 00:24:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 355bd3a5-a0cf-3090-92dd-c03c850a7b36 | -6.6957 | -48.3992 | 2025-09-03 00:24:00 | METOP-C | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| bd6ef2e1-7293-3106-aebe-ec1bbd757d4f | -7.9275 | -46.450901 | 2025-09-03 00:24:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d9b13b13-1d79-367b-9d12-2fb2349b120f | -6.9792 | -44.3591 | 2025-09-03 00:24:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0eea6d43-c512-373f-93fb-04104fd10676 | -5.7885 | -43.224998 | 2025-09-03 00:24:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e9aecbb9-6511-3168-9411-bc0ef70363bb | -13.5221 | -47.013 | 2025-09-03 00:24:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 053afcbb-4935-3794-b522-54c23b489746 | -4.8894 | -44.9608 | 2025-09-03 00:24:00 | METOP-C | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c63ab045-4e11-362e-ac08-c22f1e5e16bd | -9.1312 | -49.654701 | 2025-09-03 00:24:00 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0d6baea1-8f6e-32a5-9f7f-aff15744ff37 | -15.5475 | -48.323299 | 2025-09-03 00:24:00 | METOP-C | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2dc5bd7c-1c28-366c-a2ad-dd16e0e6835c | -9.4478 | -40.395199 | 2025-09-03 00:24:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 02b05c61-00a2-3b8f-879b-cb99fd582ad7 | -11.5977 | -52.089199 | 2025-09-03 00:24:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e09dcfa8-aa75-3a56-a0c8-f82f79dc55f2 | -6.5404 | -44.5597 | 2025-09-03 00:24:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 922dbc7f-ab0d-338b-9598-af062be01198 | -11.5782 | -52.093102 | 2025-09-03 00:24:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 02ce26ea-e3fc-3e77-a48c-9049fe08da40 | -7.5036 | -45.346401 | 2025-09-03 00:24:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0dea6724-68d8-396e-94cd-8e6d10019d49 | -6.2486 | -42.630501 | 2025-09-03 00:24:00 | METOP-C | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| de71dc88-dceb-3a6d-8fe9-6f1a5f88d4ba | -7.7947 | -45.4487 | 2025-09-03 00:24:00 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0f12ebc7-64b3-32fb-8819-f171143b0f86 | -9.4575 | -40.392799 | 2025-09-03 00:24:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| ec4898c2-8be4-393e-ae3c-5667983ab3a2 | -6.8531 | -52.791401 | 2025-09-03 00:24:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eb9d7c5d-7227-36c0-90a3-f74a93c11c42 | -6.1221 | -44.131401 | 2025-09-03 00:24:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7f1028e6-42a5-36af-ae30-564538ea181c | -11.5907 | -52.054298 | 2025-09-03 00:24:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 22672ae1-8dcd-3881-aec7-1d6c9634fda2 | -7.0032 | -43.4342 | 2025-09-03 00:24:00 | METOP-C | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 27ba594e-8db3-38a0-9bd4-1a48a6d1cb97 | -7.4254 | -46.002701 | 2025-09-03 00:24:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b8021636-7b9a-3fbb-9772-e58ba4e65026 | -4.6661 | -41.9538 | 2025-09-03 00:24:00 | METOP-C | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 234eeb78-3e72-3d3b-b2f1-dc0ae78ef9bb | -10.9072 | -50.831699 | 2025-09-03 00:24:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1694bbbd-33e8-338b-adac-e72aedda88ac | -12.8415 | -48.010399 | 2025-09-03 00:24:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dff09e43-12b1-36e2-a064-b53e6d1c3b10 | -10.119 | -47.440899 | 2025-09-03 00:24:00 | METOP-C | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 06c302c7-cba6-39d4-8903-e299acc852a9 | -11.6004 | -52.052399 | 2025-09-03 00:24:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 60475642-602f-3a68-a687-d0df8f59ee4d | -7.8948 | -46.442699 | 2025-09-03 00:24:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 98840629-3549-37b3-a031-7db0c4e5ef0b | -6.8407 | -52.828499 | 2025-09-03 00:24:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b8984ba-d6c8-3927-b40b-601ec2c8d0fc | -9.6326 | -47.046398 | 2025-09-03 00:24:00 | METOP-C | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 08baf3f4-c83a-3831-aa58-699691e5b2d2 | -6.9471 | -43.281101 | 2025-09-03 00:24:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 117e87b4-310b-3ea5-a3ea-729a303632e7 | -9.7436 | -49.411098 | 2025-09-03 00:24:00 | METOP-C | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1dbb0862-f7d5-38ef-be90-1d9004a0f554 | -7.4677 | -44.826302 | 2025-09-03 00:24:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3bb53ae5-db47-3e83-8593-b65c61e692cf | -7.8564 | -46.730999 | 2025-09-03 00:24:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9e7358bf-096c-38fc-9e87-1d4a1483030a | -6.684 | -48.3927 | 2025-09-03 00:24:00 | METOP-C | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| f8995b3c-db54-3a0f-8010-868be52f7fcd | -6.808 | -52.8181 | 2025-09-03 00:24:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f78a2ac3-853e-325a-a509-d5c0c796a66e | -6.9944 | -43.262699 | 2025-09-03 00:24:00 | METOP-C | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3b2dcb94-a970-30b9-87fd-20d58e7c698a | -8.205 | -44.804401 | 2025-09-03 00:24:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7aa91611-6c42-3043-9a6d-82769bde82f6 | -5.7627 | -45.396999 | 2025-09-03 00:24:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e4166586-d7e3-3b8c-8564-7ed10aec8b83 | -6.7212 | -42.268501 | 2025-09-03 00:24:00 | METOP-C | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 339d53ab-a424-32b1-8a85-929c700eae1c | -9.1899 | -45.1945 | 2025-09-03 00:24:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5b208afb-0b88-35f4-a96d-a11e5140f1c8 | -12.8338 | -48.0224 | 2025-09-03 00:24:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7637b2c0-5c62-3b98-ae67-437f90ea4393 | -3.4088 | -44.265598 | 2025-09-03 00:24:00 | METOP-C | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| afd84d1b-0aa0-3222-9272-2484ebcb30c5 | -13.8648 | -43.4897 | 2025-09-03 00:24:00 | METOP-C | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3353f8d9-8696-3ebc-84a3-e20d744d5575 | -11.5755 | -52.1301 | 2025-09-03 00:24:00 | METOP-C | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 629e4bc6-8a84-3837-8cae-59028889f22b | -5.4207 | -47.113201 | 2025-09-03 00:24:00 | METOP-C | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4f3de50a-1d43-309b-917b-ed4194ef874b | -13.3091 | -46.829399 | 2025-09-03 00:24:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 6b007b77-f0ad-3638-9ce1-a80fd1718e09 | -7.476 | -44.8172 | 2025-09-03 00:24:00 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 9dc86477-d179-3e09-8140-7add1065360e | -6.2584 | -42.628201 | 2025-09-03 00:24:00 | METOP-C | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 369bc7d4-da5e-3aa5-b805-6666b409ecfe | -12.9895 | -48.082901 | 2025-09-03 00:24:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1117efd7-b007-3141-9d45-531aa75d2f47 | -6.599 | -44.096298 | 2025-09-03 00:24:00 | METOP-C | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 59455d77-ad8f-34c7-a169-0a39fd8a9c7b | -11.3801 | -43.579102 | 2025-09-03 00:24:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d8348681-1dc1-3dce-9720-e52e284114ab | -13.6847 | -46.959202 | 2025-09-03 00:24:00 | METOP-C | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 62e5255d-398b-356d-af70-7d72ea17dce5 | -3.23 | -47.128399 | 2025-09-03 00:24:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2bbf14ad-a60a-337a-acce-61c1a1eb1aec | -10.0524 | -48.0807 | 2025-09-03 00:24:00 | METOP-C | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3dcfe7c2-5d31-325e-ad37-e6cb9305054b | -9.1801 | -45.196701 | 2025-09-03 00:24:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c3d7ddfa-1fd9-3c0b-8270-f356b0033576 | -6.7777 | -44.469898 | 2025-09-03 00:24:00 | METOP-C | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 92fd81c0-5e1f-3c95-94f8-e72e072f6df6 | -8.0082 | -50.0905 | 2025-09-03 00:24:00 | METOP-C | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b72fc6e8-4fb1-3a8a-8802-69027aeb4bc8 | -10.1391 | -46.266499 | 2025-09-03 00:24:00 | METOP-C | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| aff0efbb-4b31-348c-8640-5c0c9803c5fc | -6.4604 | -49.518299 | 2025-09-03 00:24:00 | METOP-C | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb8ea7fc-54a0-369c-bbd1-2014d9b4ea8f | -10.7309 | -44.8106 | 2025-09-03 00:24:00 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| faae944f-8cc8-3419-889c-a49a5a8ec9ab | -8.0203 | -44.0863 | 2025-09-03 00:24:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b720d324-53de-3119-9a24-dd5743d491bd | -7.6187 | -46.5424 | 2025-09-03 00:24:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 78f7839d-111a-3c65-86db-95960678f5fb | -13.5062 | -47.035099 | 2025-09-03 00:24:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3cd4471a-e26f-342f-9b58-dd5eb22b8e9a | -7.4938 | -45.348598 | 2025-09-03 00:24:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6c7399de-ca4b-3634-855c-0611ea2bc29d | -9.1915 | -45.2015 | 2025-09-03 00:24:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 747e8533-0a38-334a-8154-ce06a32275bc | -6.2468 | -42.622799 | 2025-09-03 00:24:00 | METOP-C | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3e1faaa1-1b23-3e6b-ba1f-2ef2d8db21f0 | -6.2502 | -45.0933 | 2025-09-03 00:24:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e7553eb1-8293-33ce-9f9f-70533cab9538 | -6.2733 | -44.518902 | 2025-09-03 00:24:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1efcfa7e-82c7-3d02-af21-8726f74c8b52 | -11.9109 | -46.667099 | 2025-09-03 00:24:00 | METOP-C | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 66eae9b5-033c-3473-b730-a651ac60abb9 | -6.971 | -44.368198 | 2025-09-03 00:24:00 | METOP-C | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 42c4888e-c0e7-3364-87eb-d1ba0a7aa1ce | -9.1883 | -45.1875 | 2025-09-03 00:24:00 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 96d10b83-051b-335b-abb2-c19f6c2dda78 | -8.366 | -48.293499 | 2025-09-03 00:24:00 | METOP-C | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 710c7721-25a9-343b-8f49-312268a762b5 | -6.4583 | -49.5084 | 2025-09-03 00:24:00 | METOP-C | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6babbeff-9487-311b-8fbb-5679b2330211 | -7.3094 | -44.2696 | 2025-09-03 00:24:00 | METOP-C | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0e74a262-f169-3f04-aa00-6cadfb3dd420 | -6.6976 | -48.407799 | 2025-09-03 00:24:00 | METOP-C | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| ad841dd2-987d-35fa-8f6f-6f6ee9b82a8b | -10.7425 | -45.276901 | 2025-09-03 00:24:00 | METOP-C | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cd8d4d24-ae31-380d-845c-fd4b5066f72f | -10.9545 | -44.202499 | 2025-09-03 00:24:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2a4f5118-28b0-3d3f-b1b0-3c678de71273 | -9.501 | -48.897499 | 2025-09-03 00:24:00 | METOP-C | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4cae5076-e6f0-3ace-ade6-2d9ce1baec1a | -13.0014 | -48.091 | 2025-09-03 00:24:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dd6b7a29-d5ab-38c5-a516-d4fbf8635c61 | -13.3306 | -46.8339 | 2025-09-03 00:24:00 | METOP-C | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b5d11aec-878a-32de-a3fa-56fef6d9e3fd | -11.0489 | -45.404999 | 2025-09-03 00:24:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README5.md)
