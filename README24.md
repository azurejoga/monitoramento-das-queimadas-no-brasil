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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e97546b5-e27b-3be9-a01f-be2ea57c3536 | -11.4648 | -44.56133 | 2026-08-12 04:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 87bc1c0e-3425-3f59-b9d6-e93f9b547343 | -13.53559 | -46.27861 | 2026-08-12 04:51:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 52fb2fe8-99ad-3814-93aa-1d28073f9608 | -14.52037 | -49.30257 | 2026-08-12 04:51:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| de34cfd3-6125-3a71-94e6-0dcdacad008d | -13.30032 | -49.69735 | 2026-08-12 04:51:00 | NPP-375D | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 672b0fe6-603b-397a-99bc-d6291163d517 | -16.67489 | -45.03384 | 2026-08-12 04:51:00 | NPP-375D | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7237a490-480a-3504-b747-3208a3dd3508 | -11.94648 | -46.32634 | 2026-08-12 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6e47ea8b-d87c-3355-9758-a5c7905de1b6 | -15.5228 | -45.85963 | 2026-08-12 04:51:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 36ea4cb0-8bff-3823-9158-7edd37481b3c | -14.3991 | -52.07133 | 2026-08-12 04:51:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 908bd507-f772-387b-91ac-f8b121150ed8 | -12.35122 | -48.2046 | 2026-08-12 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| afe660e0-49a5-3730-969a-8ad17cf6296c | -8.96135 | -60.53854 | 2026-08-12 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 46f35aa2-7b60-323d-90e4-df6b5dc7580d | -8.94491 | -60.53119 | 2026-08-12 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eb4e3952-eb85-3a68-8492-508cdb579a05 | -14.44068 | -52.25929 | 2026-08-12 04:51:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 39be0e2d-bfed-3809-89e3-758dff176b9b | -16.34527 | -49.46434 | 2026-08-12 04:51:00 | NPP-375D | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 971e0d76-3390-321a-9ea7-802973c85706 | -11.98444 | -46.36769 | 2026-08-12 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 6d8c1c65-7497-30e7-915d-294ba1b042f6 | -16.3412 | -49.46776 | 2026-08-12 04:51:00 | NPP-375D | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 046d4ff1-0a3d-3364-9e8a-aad4a711e26a | -11.61083 | -54.65901 | 2026-08-12 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9359e299-ade9-3223-870a-a026132956a6 | -17.14529 | -44.80304 | 2026-08-12 04:51:00 | NPP-375D | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8e86da8c-63bb-31c1-b49b-97326a3f0419 | -12.16616 | -50.12775 | 2026-08-12 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7fbc9ce0-2f77-3c65-980a-8733a4278166 | -9.6747 | -48.16033 | 2026-08-12 04:51:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c5db5554-812d-3c34-8517-5e995a6b74a8 | -14.51804 | -49.29441 | 2026-08-12 04:51:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1ccfa7a0-d926-3476-8c31-d25062dea466 | -8.94911 | -60.54043 | 2026-08-12 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5c5a7d42-46db-3bbb-b1a3-18d365fa574f | -10.70815 | -47.90094 | 2026-08-12 04:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 26cd24f8-8273-36ce-bee1-7a9a647ef7e9 | -8.94518 | -60.49821 | 2026-08-12 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5cd9c775-90b1-37f1-b28a-de09fd116c52 | -16.34178 | -49.46378 | 2026-08-12 04:51:00 | NPP-375D | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9769d652-e632-35a5-b3b6-cd23ecd676c2 | -13.88822 | -53.81708 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 900d08da-55b8-3815-9d26-bc9c15b08c68 | -15.05981 | -45.32378 | 2026-08-12 04:51:00 | NPP-375D | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 23b5342d-8ebe-3507-a5cd-10dbf0803a16 | -15.28265 | -48.91358 | 2026-08-12 04:51:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d4d2529e-2724-3fef-8a02-9113cb78d5f1 | -11.61161 | -54.65444 | 2026-08-12 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7adfe8b3-daae-3f76-a2bb-643915f7dd7d | -11.82587 | -51.84886 | 2026-08-12 04:51:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 02f50883-4227-3b61-b448-a9cd729959da | -14.25839 | -49.65789 | 2026-08-12 04:51:00 | NPP-375D | CAMPOS VERDES | GOIÁS | Brasil | 5204953 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a9607d0-f8c2-34b3-9fb3-dfbdd32b02be | -11.98766 | -46.37295 | 2026-08-12 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| c46ab4f9-cd45-340a-ad87-ec8e255ab36b | -16.26189 | -49.42026 | 2026-08-12 04:51:00 | NPP-375D | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9bf9e2e2-9a61-3c4d-a3a4-a31669bc0102 | -12.72569 | -48.44449 | 2026-08-12 04:51:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cffde7cd-ca1a-33f8-b4e0-8f5b90de9346 | -13.83952 | -53.80549 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6aa7af17-d716-3907-8332-1e17dddd8747 | -10.36686 | -46.3782 | 2026-08-12 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ddcc519f-6b65-385f-a41f-b3246e3e77cf | -10.27407 | -48.25135 | 2026-08-12 04:51:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d31d570-0a4b-30d8-ae0b-b78dd5626d53 | -8.95408 | -60.54562 | 2026-08-12 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6602b7f1-926b-326b-9309-5b51263e49fd | -11.96866 | -46.39447 | 2026-08-12 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fa9e8eaa-56b4-3aa7-a3ed-95e96931a1b8 | -14.30291 | -54.01421 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2577ed67-4a7e-397e-a430-32965e65043c | -14.9796 | -46.60352 | 2026-08-12 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e1cab228-5643-3c78-afa7-1f24bef22502 | -11.78277 | -51.86008 | 2026-08-12 04:51:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2dd8abe3-02f8-3ad2-9f95-7c13d9199906 | -13.9014 | -53.8032 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 22576947-b5cf-3fdb-a31f-33d9a6a03514 | -10.7087 | -47.90244 | 2026-08-12 04:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ca661a0-f4ab-307e-b570-cfab54c3d2a9 | -11.9838 | -46.37214 | 2026-08-12 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 1604b0c8-b6bf-3fa4-8c55-51454eb0f9f7 | -14.53781 | -50.33802 | 2026-08-12 04:51:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a23935be-2326-3be3-bc2c-0cae5399250f | -14.03411 | -53.59915 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 32bf98c6-e22d-3490-b612-32f5c4f3a9ff | -14.03308 | -53.5953 | 2026-08-12 04:51:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d6977154-871a-313b-8da4-e1dd577f1fdd | -16.10242 | -49.88565 | 2026-08-12 04:51:00 | NPP-375D | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 99c705fb-c1be-3903-9491-148465f8cbfb | -10.34015 | -48.29605 | 2026-08-12 04:51:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d23cd919-42df-3a36-aedf-ade4d753d301 | -8.89346 | -60.58138 | 2026-08-12 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7492cdc6-91fd-389f-ba2b-cbfb30b0d754 | -12.82271 | -49.69847 | 2026-08-12 04:51:00 | NPP-375D | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b31d020d-585a-315f-a4f8-22f645b02a10 | -12.31587 | -49.79499 | 2026-08-12 04:51:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0bf2ba23-5061-3ace-b7df-633795834432 | -8.95036 | -60.5655 | 2026-08-12 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2456cfb8-655f-375e-b4fd-ca156b8cfd41 | -10.36375 | -46.37287 | 2026-08-12 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2a4efd93-842b-3723-a60e-9287349d1b99 | -7.42015 | -60.00333 | 2026-08-12 04:51:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 59dde20d-929c-385d-92ad-e41d447aaace | -13.60347 | -46.23812 | 2026-08-12 04:51:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ea336e70-9fd1-3ac6-817b-e1af44543eb4 | -14.51456 | -49.29397 | 2026-08-12 04:51:00 | NPP-375D | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33e60af7-4b1e-3db5-9719-3b400c8699ec | -8.95609 | -60.56665 | 2026-08-12 04:51:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 214e19a6-3642-3444-b514-3062c04d7c2a | -14.98362 | -46.60399 | 2026-08-12 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bb3c810d-a19d-3113-b56a-871c7f6be123 | -11.94952 | -46.36123 | 2026-08-12 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2df9781a-9f91-3139-a607-aebb4be5d30f | -13.53164 | -46.28455 | 2026-08-12 04:51:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 82bf5dfe-ee4e-3dfa-8369-4330e26cef48 | -10.09664 | -46.23093 | 2026-08-12 04:51:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8f7a495e-7471-3ca3-b90d-2bf86b448e33 | -11.93315 | -47.35574 | 2026-08-12 04:51:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6471e82c-467f-358f-95d3-f4c9ea875901 | -11.59879 | -54.66161 | 2026-08-12 04:51:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd917b95-9b87-33ad-9290-af50cdc299f1 | -14.98362 | -46.59685 | 2026-08-12 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d5f772b5-b5fd-3d9b-97da-8e3e9816e689 | -15.55976 | -49.99695 | 2026-08-12 04:51:00 | NPP-375D | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f337148f-0dc8-30b3-a847-56dd0a8dbd83 | -11.98312 | -46.37686 | 2026-08-12 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 0dddf13f-f1ee-35d0-b3d5-1d1363ea9893 | -18.47817 | -51.69573 | 2026-08-12 04:53:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 270c8fdc-230c-3b4c-94eb-ea624b8597f1 | -17.13124 | -51.68518 | 2026-08-12 04:53:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 97297bf2-390c-3b89-ab5b-a74e68573904 | -16.7387 | -49.35759 | 2026-08-12 04:53:00 | NPP-375D | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f1be0345-e052-378e-9473-732fd2061b17 | -22.26506 | -48.65987 | 2026-08-12 04:53:00 | NPP-375D | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| b17d9950-2efb-32ce-af9f-2f7d7459a852 | -21.49752 | -48.63912 | 2026-08-12 04:53:00 | NPP-375D | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 688c77df-7a2c-32c5-bdae-0b4485b5d9d1 | -18.94384 | -48.34921 | 2026-08-12 04:53:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3b2eec82-c077-34f2-abcb-7e13c0fd43ce | -18.72217 | -47.06432 | 2026-08-12 04:53:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 869e2a49-bb78-361e-9739-8e90a65d262f | -20.96817 | -47.41613 | 2026-08-12 04:53:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 442d01b3-6dc1-3075-869b-d151cd8b8bf1 | -18.91901 | -47.03693 | 2026-08-12 04:53:00 | NPP-375D | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fa129c75-90ee-3650-a54f-77b8ba82c1a5 | -21.16045 | -48.63471 | 2026-08-12 04:53:00 | NPP-375D | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 13cdb9c6-30d5-33ba-9514-3759f04bff09 | -21.15661 | -48.63409 | 2026-08-12 04:53:00 | NPP-375D | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ed321669-3698-3a34-bcb8-34bee6c3ccc1 | -21.30851 | -46.73122 | 2026-08-12 04:53:00 | NPP-375D | GUAXUPÉ | MINAS GERAIS | Brasil | 3128709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 7a7716b3-beef-3faf-9e50-c99a58f0f0c1 | -18.48151 | -51.69628 | 2026-08-12 04:53:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f79bad6d-addd-3f53-909b-9464f6663457 | -18.96788 | -49.49921 | 2026-08-12 04:53:00 | NPP-375D | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d923e3af-9b18-3192-91c6-0a34315b5e1c | -20.96405 | -47.41549 | 2026-08-12 04:53:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 55135f00-c324-3862-be5d-06dfc864b521 | -18.94421 | -48.35231 | 2026-08-12 04:53:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4a55c95f-2375-3333-975d-9bf2393a52d7 | -21.14321 | -50.46519 | 2026-08-12 04:53:00 | NPP-375D | ARAÇATUBA | SÃO PAULO | Brasil | 3502804 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b9dd901a-2c7b-3de1-a29d-4c72ebfe4bdb | -21.15882 | -48.63812 | 2026-08-12 04:53:00 | NPP-375D | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 86ba1842-e2b9-3e0c-8d6b-f2fc78a66731 | -18.96726 | -49.50349 | 2026-08-12 04:53:00 | NPP-375D | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3dd65b85-e000-386a-8813-42b1e32f52ce | -21.21834 | -47.58511 | 2026-08-12 04:53:00 | NPP-375D | SERRANA | SÃO PAULO | Brasil | 3551504 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e3797aaa-2a94-3025-a99f-afcbd0dfa5b9 | -17.46307 | -48.90322 | 2026-08-12 04:53:00 | NPP-375D | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 15e9c824-1111-3626-b471-3e2f478200f9 | -17.81259 | -44.38335 | 2026-08-12 04:53:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 778cc1d1-8321-38e8-934c-672f2a405452 | -18.99909 | -45.7287 | 2026-08-12 04:53:00 | NPP-375D | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2fd07de9-88b1-38e0-9ec3-9ca75445f23a | -18.48428 | -51.70052 | 2026-08-12 04:53:00 | NPP-375D | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b28d1376-0892-3f0b-8e26-77d179b7dee2 | -18.183 | -45.26242 | 2026-08-12 04:53:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 49dbdbac-a383-3c73-903b-8ec69e792524 | -19.99772 | -49.67841 | 2026-08-12 04:53:00 | NPP-375D | RIOLÂNDIA | SÃO PAULO | Brasil | 3544202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3fe21caf-9b3e-37c1-bdcf-f7c6beafcbf8 | -18.67141 | -47.2022 | 2026-08-12 04:53:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 033f98e1-5340-3ea3-babd-a0ac84788481 | -22.26896 | -48.66044 | 2026-08-12 04:53:00 | NPP-375D | ITAPUÍ | SÃO PAULO | Brasil | 3522901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fdf01734-5cc6-3816-a686-f5b0a394b5aa | -23.06062 | -51.07718 | 2026-08-12 04:55:00 | NPP-375D | SERTANÓPOLIS | PARANÁ | Brasil | 4126504 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| fceff3ee-76ee-3814-a2c8-8b6451e20236 | -15.3023 | -48.8595 | 2026-08-12 05:00:00 | GOES-19 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 53.6 |
| e090566d-9d0b-3bd8-9c8f-c9aea9c2a74d | -11.9911 | -46.3844 | 2026-08-12 05:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 57.8 |
| f31c98c4-e78c-33df-bc3b-926cc9fd91be | -11.9539 | -46.3217 | 2026-08-12 05:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 59.5 |
| c55a66f4-c0e4-3ac2-8dc0-e63e4654bbac | -11.9535 | -46.3444 | 2026-08-12 05:00:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |


[Clique aqui para ver as próximas entradas](README25.md)
