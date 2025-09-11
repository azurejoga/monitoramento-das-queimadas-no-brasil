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

## Dados Diários - Página 104

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5cf0617b-6cf1-3b9c-b88f-126ffd22226c | -15.80275 | -52.22702 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| babfebcc-c45a-3099-be4c-321ef41c0287 | -8.87215 | -49.55727 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6d4f9f8e-6bbd-368b-8d03-afb5194f6a03 | -10.01903 | -51.71145 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be84b611-7e07-3944-9024-ae6a8f59fd0b | -15.24427 | -53.83827 | 2025-09-11 04:46:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9d4b7a56-0c2d-385f-bbb1-9c4db691029e | -14.88896 | -55.83875 | 2025-09-11 04:46:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 878328b2-6b11-3410-aef6-4efe0025effc | -11.65701 | -46.90742 | 2025-09-11 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3a780256-7109-39e2-8eb7-7692e92d8348 | -12.82337 | -52.94024 | 2025-09-11 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6f71d8a9-ac20-35d1-9f89-5b3a6b1fe1a6 | -10.13575 | -47.89334 | 2025-09-11 04:46:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d57488b-e133-38f6-9343-848ce7ce451f | -15.16119 | -52.43108 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 151bff88-27d5-3511-afab-59e786bae6d7 | -12.17787 | -53.88148 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21f662d8-0363-3a6e-8bd7-1f899cc66f49 | -15.13406 | -52.43013 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b078f34f-6df0-3a8d-b79e-fd2a83931b6a | -10.20278 | -51.68655 | 2025-09-11 04:46:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ed6f2efe-b305-3c23-88b6-10ba6145e748 | -15.79998 | -52.24522 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1cacfae4-3c38-3ae8-a016-3488116be1cf | -9.1561 | -60.25807 | 2025-09-11 04:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7b0638b-61aa-38b8-a95f-0093f2014486 | -11.99263 | -47.59205 | 2025-09-11 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| abf16460-7c4c-3be0-b350-d7a805225b5a | -10.66954 | -48.62595 | 2025-09-11 04:46:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c63aab92-260c-3118-8962-d3790f8e3d64 | -11.59596 | -52.21988 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e5df24d-9f27-315f-8ad2-1da10d747f03 | -9.07008 | -49.84325 | 2025-09-11 04:46:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d7ca5628-a1e4-3b4d-91d1-8ba7105f5011 | -10.20885 | -51.69109 | 2025-09-11 04:46:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53710f7e-e453-38a1-b641-c49323242314 | -12.39361 | -54.16819 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 566fe62f-981b-346d-b111-5414a77851a4 | -11.70083 | -48.25953 | 2025-09-11 04:46:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8dcaa882-c810-3902-89c6-21cdacc960ac | -12.95176 | -54.74079 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f97a43fb-574c-3f84-9a7e-676d580b6f64 | -11.20982 | -54.98923 | 2025-09-11 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5d03ee91-0d28-3b1b-a4bf-2ad9e6c040d7 | -14.55961 | -54.52345 | 2025-09-11 04:46:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 04469bad-9a6b-3522-8583-c4fdcd427019 | -15.90936 | -50.19282 | 2025-09-11 04:46:00 | NOAA-20 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ff82baaa-7c37-35c0-9272-b28edd617ea6 | -10.53988 | -51.50744 | 2025-09-11 04:46:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2ebb53f7-4ba6-30c6-9cd7-c0276213aba1 | -12.93022 | -54.78477 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7b058567-525b-3797-9d14-298ff660ca10 | -8.08681 | -54.74511 | 2025-09-11 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 70b94b22-02ee-38d2-9bc7-b64734aa1bf1 | -11.36042 | -46.52985 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 17625b47-9c56-399c-967b-ac4661f3bc41 | -9.9985 | -51.71146 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3e8eb4db-9759-31ed-b6b6-a82a3baf8a66 | -9.01028 | -49.52377 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 230d95e9-d48d-3e82-b251-030d53f6c5c8 | -12.84434 | -52.95823 | 2025-09-11 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 284acce8-a3f3-3099-aea4-ab25a332c206 | -15.67553 | -47.02861 | 2025-09-11 04:46:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 15.8 |
| d9cb5e43-61ae-3f6d-8f1a-6a1affc2869f | -11.87521 | -58.82176 | 2025-09-11 04:46:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 50d9ab79-3b8b-3ea8-9256-98d8f092c878 | -11.13905 | -52.05996 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| afbaa9fb-ab1c-3dd0-b3ca-612dd58cac90 | -15.80035 | -52.22663 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0bab4fa4-d70e-3e84-aa71-f6557d0b40f3 | -11.13132 | -52.02278 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a01d9d1e-8456-3c12-9762-a24513fcafde | -9.05803 | -50.49249 | 2025-09-11 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 022a926e-bef6-3bb2-91de-5ef99d567a9a | -15.12751 | -47.03184 | 2025-09-11 04:46:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 40ed23b3-b193-3dc0-aaee-08f4f85be143 | -9.79951 | -51.0943 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b8caae93-c277-3fc7-92f5-6fda9f51ab51 | -12.0758 | -50.99211 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cef59890-b655-36be-8b6e-639efe5f2fb1 | -10.54264 | -51.51151 | 2025-09-11 04:46:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7a8ee556-816f-36e4-8040-34aff3ed3dd7 | -11.47073 | -43.64453 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d0e845f6-e86e-3e95-b1ca-3a15244f86d0 | -15.21557 | -44.05368 | 2025-09-11 04:46:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d60713e7-ba65-350b-8ea5-7d1c52a7a2fb | -12.9248 | -54.79588 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b280e461-e11b-31a0-95b6-02e916de072c | -11.94351 | -46.64149 | 2025-09-11 04:46:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df378431-9f0f-3e14-aa4a-421bd718c724 | -15.79699 | -52.24845 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dead955c-903b-3de5-b848-777da9672d73 | -9.98967 | -51.7029 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8d85ece9-bb2f-3224-b2bf-18d3694a1a9a | -12.97377 | -48.03756 | 2025-09-11 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60efabe8-422b-3edf-b2e4-d935ca35e027 | -13.84266 | -47.34729 | 2025-09-11 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f31db467-dc76-358d-b1e2-c38338f02599 | -12.90721 | -47.99613 | 2025-09-11 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f51e2244-aea0-3ccd-9955-9ed4c829a2bf | -15.60455 | -52.7458 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0cad9b10-3b1b-35c8-9052-230c74ad7175 | -12.92415 | -54.79977 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d90818be-80bb-3989-883a-c7fef6700d21 | -9.01936 | -49.76317 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 4b5fbc5f-2028-30dd-8e7c-1df756532505 | -11.71852 | -50.63347 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 1dac4af8-2047-398e-8b8a-204428fa4c9f | -13.86151 | -47.36255 | 2025-09-11 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2c04015c-d283-3892-9a93-61594fc3982b | -11.19851 | -48.39893 | 2025-09-11 04:46:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cf46ed0b-a20a-35cc-b876-962dcc8f7bf7 | -9.98581 | -51.70586 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2de028bf-cd6b-3501-b515-c01ada61583d | -16.06034 | -49.96692 | 2025-09-11 04:46:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 17e01415-d013-3a3b-bcb3-4a0f622bdd21 | -9.59007 | -48.0662 | 2025-09-11 04:46:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5a130935-1810-3dff-a1cb-4476e51ebb99 | -9.4596 | -46.7428 | 2025-09-11 04:46:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 86118306-6038-3da8-a7b6-a0046f659081 | -15.24095 | -53.8377 | 2025-09-11 04:46:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 42ea2393-fecf-325c-8951-3cb0a82ac3f1 | -14.36224 | -47.29858 | 2025-09-11 04:46:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 490de8e7-0f42-327d-b605-8dc36a563a9b | -15.12521 | -52.42127 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 77313cae-dc4c-3985-9586-3dbe282e48c3 | -15.17503 | -52.4297 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 243a9b89-ad96-30f7-b9da-844780d160a1 | -11.1258 | -52.01471 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b0f0f123-cf24-3b5a-8d1b-fc64cb07e442 | -9.98857 | -51.70988 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d29bdaeb-79ad-3f83-882f-a5e95d4c9781 | -9.02004 | -49.52913 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f6eca030-bffa-3759-869d-f7b1546cc7e4 | -14.56138 | -48.76809 | 2025-09-11 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c713db55-4c20-3319-9075-45cfde5b7e5b | -11.36195 | -46.54976 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 387f1e4b-6209-3121-a3d4-d476269f11ee | -9.02053 | -49.7786 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9c5b2f93-c35a-36b3-9eeb-b57bc7783992 | -15.14071 | -52.4313 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 32f4bb9e-e28d-392e-9c22-89cf671232b5 | -15.66394 | -53.89056 | 2025-09-11 04:46:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 867d5685-d93f-3994-a361-eba93065ff2f | -10.56774 | -52.0215 | 2025-09-11 04:46:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0536f9a-6747-392f-95b8-1ac718625d4c | -9.97422 | -51.69328 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cbe38ad5-997c-3ca0-b085-363e601a533e | -10.00127 | -51.71549 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a47a0b11-b2b0-3006-a7f3-80209feb6b6a | -9.59662 | -48.06082 | 2025-09-11 04:46:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 51a1c3e0-725a-3a12-af98-7871e68c9929 | -12.13924 | -44.85785 | 2025-09-11 04:46:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6157fb17-cc2a-3060-8f77-b4fbb02201ee | -11.15285 | -52.03704 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea5bfe98-c04a-39a7-a3f6-b4ea9b0b3c2f | -11.60369 | -52.21394 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 718b1ade-a92d-3a03-aba3-4c637a15d962 | -9.01946 | -49.53291 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4e47ed2-e66e-31c2-862e-038840351f74 | -9.5985 | -55.01234 | 2025-09-11 04:46:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d0e44d30-6987-395d-9fa1-47ca7554b9ac | -15.52684 | -48.55871 | 2025-09-11 04:46:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0cd39d74-faa8-3b64-8fe6-a974b5f9a6f3 | -10.37765 | -48.83615 | 2025-09-11 04:46:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1a10ad5b-dc16-35d8-81e5-3e88297d8a6f | -12.86098 | -52.9392 | 2025-09-11 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 50a640f8-f01c-39cd-8bf9-50b282853e3b | -13.32694 | -46.37266 | 2025-09-11 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9e665c89-6513-3ebb-aa80-25ebe07ffa7f | -11.48291 | -43.63076 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d15dab79-c84f-3040-8781-7fbecf851f57 | -12.95803 | -54.74583 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89bc056f-0e51-3bf6-ba9c-fb094b2f0eee | -16.28912 | -45.6886 | 2025-09-11 04:46:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| de48f932-1f59-3160-a019-e79bf1f4f678 | -14.28833 | -54.74477 | 2025-09-11 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ea770ca6-fdbd-3a47-ba5a-f3c196743f74 | -16.06335 | -49.97185 | 2025-09-11 04:46:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2d30e4fd-0d70-37c0-9dd2-2cb0dd673e46 | -10.44344 | -47.76888 | 2025-09-11 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0a3ee60-15e7-3e5a-8ec3-ad8041c1d918 | -9.91697 | -49.86652 | 2025-09-11 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 95d9a573-f927-3d87-b6e0-e58b298cf7bb | -12.38218 | -54.17388 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c34f0ece-5b15-3459-948d-fb896cc757b5 | -9.59443 | -48.06226 | 2025-09-11 04:46:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8ced37b5-cb0c-3328-8e7b-3f9808e05d6c | -13.2053 | -48.37413 | 2025-09-11 04:46:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6ddb8ece-e03c-3cca-a362-f21f80608d98 | -15.80553 | -52.23122 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a08d93c7-2617-3bbe-b2ff-d880db59b4e2 | -9.02338 | -49.78285 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1eeb5ebd-768e-3f79-9585-5d3b3623abad | -9.76895 | -51.0969 | 2025-09-11 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a762e5eb-044e-3865-a1de-94d615438ae3 | -10.55334 | -49.89149 | 2025-09-11 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README105.md)
