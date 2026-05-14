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
| 90c515b2-3d63-313b-8c90-70ca967023cf | -8.54644 | -45.98193 | 2026-05-14 04:36:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2b168ff0-d240-3980-9237-943e867cf9da | -8.09819 | -44.17773 | 2026-05-14 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d4258f81-d207-3d17-ae54-58dc9fb35449 | -11.97256 | -43.84206 | 2026-05-14 04:36:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 27c6e760-1dcd-371b-ac47-b562f5459c0b | -8.27308 | -48.24565 | 2026-05-14 04:36:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 16ae9f1c-98f9-35b3-976f-0fb1dad0bf49 | -10.40092 | -46.64385 | 2026-05-14 04:36:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e01c3e12-d537-33e5-a6f1-f2ce0dcf487b | -11.96959 | -46.78853 | 2026-05-14 04:36:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b6debb5c-42ff-3d42-8b17-01eaa6318670 | -11.9353 | -43.36668 | 2026-05-14 04:36:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 422cfdce-6b64-3ce1-acf8-a1ee237e9ea6 | -11.2036 | -46.91646 | 2026-05-14 04:36:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 95c4d831-6e76-3080-bae6-67c09a1cf114 | -9.30623 | -45.4847 | 2026-05-14 04:36:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| efcb5a03-1b50-30a1-a118-95e296ef88ee | -12.05558 | -45.28284 | 2026-05-14 04:36:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 103bee86-3b2f-3cd6-97e7-8f5a85fd09a0 | -11.7375 | -44.52407 | 2026-05-14 04:36:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9df58a31-34a3-346b-9e27-8e90b8b96e5c | -11.63353 | -54.15759 | 2026-05-14 04:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 749956db-dd13-393d-bdbd-3d7fb37af7c6 | -8.26912 | -48.24872 | 2026-05-14 04:36:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a28b28ba-e980-3373-83b9-e3b5e2339170 | -9.75971 | -55.62475 | 2026-05-14 04:36:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 40346dab-9dc8-3b43-87c8-92c72b0a7789 | -12.11272 | -43.64536 | 2026-05-14 04:36:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| df168bac-9167-3ca9-be6d-4e98cf7f80da | -9.29657 | -45.47944 | 2026-05-14 04:36:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9840fcc9-c238-3ef9-b05c-9813044f7dce | -8.53919 | -45.98441 | 2026-05-14 04:36:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a3949b4a-844f-3551-9da0-9905d5c02941 | -11.92537 | -43.92844 | 2026-05-14 04:36:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ac914ed4-5a5c-3365-bf74-9ae306174a4e | -9.29373 | -45.47522 | 2026-05-14 04:36:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3d2fe841-7f26-31ed-b3ff-997ec682bcd2 | -10.66463 | -49.71069 | 2026-05-14 04:36:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68f80c5d-d7c8-30b3-8c6c-538dc77abaff | -10.48519 | -49.35848 | 2026-05-14 04:36:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4be2e156-c701-3c3a-9a4c-26bdc22a9062 | -8.07507 | -43.74115 | 2026-05-14 04:36:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 175c815a-e970-31c7-87c1-83e78ba0f87b | -10.55302 | -42.44794 | 2026-05-14 04:36:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ca002a3b-bb8c-3a99-ad85-27113d5a5e8d | -9.56291 | -44.58179 | 2026-05-14 04:36:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 019990bc-2e12-3eae-a9b6-90540dac2111 | -11.93461 | -43.37164 | 2026-05-14 04:36:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc50ff36-c455-3660-87b4-bcce04dbf372 | -10.55755 | -42.44498 | 2026-05-14 04:36:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 24c14c53-f9cd-3b73-b189-72ed017790a4 | -9.29998 | -45.47996 | 2026-05-14 04:36:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| abd6e66a-c4bc-39fc-8bfb-ad75ed5b3956 | -10.66812 | -49.71128 | 2026-05-14 04:36:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 922aa241-2f82-3a0b-9dde-7fadccb3ab31 | -11.97253 | -43.83936 | 2026-05-14 04:36:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 97903056-afaa-3361-b2e0-f34ff1316350 | -9.46464 | -40.34269 | 2026-05-14 04:36:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 63441dc2-2380-395b-8bff-0159c2baf5b2 | -9.46531 | -40.33803 | 2026-05-14 04:36:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 9867c29e-78d6-3efc-a26f-359439e74ab6 | -10.39703 | -46.64684 | 2026-05-14 04:36:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 21507f4a-d58a-326c-8b9d-b50f9e80bf97 | -9.56704 | -44.57839 | 2026-05-14 04:36:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bc260798-5596-32ef-9ae1-41790e0c9bb3 | -11.98636 | -46.7912 | 2026-05-14 04:36:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9bb44d02-b613-3e62-bb19-312cd1d24777 | -8.10174 | -44.17828 | 2026-05-14 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 40ba92cc-c6c9-3d09-8df1-f58d8edf69fa | -8.11175 | -44.18389 | 2026-05-14 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1454bf02-9298-3302-99a7-8ff8ee2d8766 | -9.29714 | -45.47575 | 2026-05-14 04:36:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 43fe4a3b-665c-3d15-8627-6cf59782679e | -9.56351 | -44.57784 | 2026-05-14 04:36:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 662d7857-2ff1-33f0-ad91-8fa8eaf6286d | -11.1769 | -55.92408 | 2026-05-14 04:36:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e845f175-c0c7-3e43-bd25-104c13c87a85 | -11.93773 | -43.37026 | 2026-05-14 04:36:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a367ccbc-60d4-3f36-8bd6-7cac7f2053b1 | -12.74831 | -45.95088 | 2026-05-14 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bec2bb89-e875-3920-9516-e62be9277790 | -8.53974 | -45.98087 | 2026-05-14 04:36:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b31cda08-15a0-3552-8751-d9f441bfb9ca | -11.42347 | -47.08941 | 2026-05-14 04:36:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 929c50fb-6b28-368b-aa99-2441570d961b | -11.76189 | -47.06353 | 2026-05-14 04:36:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 12aadd2a-eabf-32d9-8003-70165939973d | -11.92912 | -43.92901 | 2026-05-14 04:36:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fb6bcbed-f081-3194-ba3c-7755fc57c815 | -11.09005 | -45.93031 | 2026-05-14 04:36:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 40469efe-2694-3e74-920a-14d57d97eb5a | -10.48863 | -49.35905 | 2026-05-14 04:36:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7ce20461-bd11-39c9-9ee5-445b7807eb20 | -9.47008 | -40.33542 | 2026-05-14 04:36:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| ee6bc65f-7673-35a1-9e84-9344671f7270 | -12.21351 | -46.57975 | 2026-05-14 04:36:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a9652adb-edcd-35f3-9e16-015915f6708a | -10.66747 | -49.71516 | 2026-05-14 04:36:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 27339278-2851-37b3-9087-a423d8556dfc | -11.30869 | -54.03762 | 2026-05-14 04:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d02ec67b-2b72-3480-bc68-9b345e870a03 | -11.80012 | -43.61909 | 2026-05-14 04:36:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 31b295ab-3460-35e8-9383-44a21b0cc05d | -11.3131 | -54.03845 | 2026-05-14 04:36:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0494659f-1ae4-3cd0-ad1b-b4819f858490 | -8.54309 | -45.9814 | 2026-05-14 04:36:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e4c6c98-dd85-34ab-9dea-a6996acc0901 | -13.95844 | -46.03356 | 2026-05-14 04:38:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c3c290de-d084-3d6b-94db-6310cf36e328 | -11.93255 | -54.10283 | 2026-05-14 04:38:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b3f76a6f-e0c1-38c8-8d25-b37bca6013d0 | -15.89794 | -43.21651 | 2026-05-14 04:38:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c221081e-2eae-35ae-8e19-79d7a48f7f15 | -14.30531 | -49.24933 | 2026-05-14 04:38:00 | NPP-375D | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a032889d-8cad-3a47-97d8-169bfe2ae308 | -16.7672 | -45.82077 | 2026-05-14 04:38:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5e56f0a2-2dde-31b4-9568-660c55ed72ee | -19.19594 | -49.12865 | 2026-05-14 04:38:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6b99eccb-b2af-3301-9aa8-a11f70224ed3 | -14.12252 | -45.29111 | 2026-05-14 04:38:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 332592b2-f0ab-3e3c-b1f9-fc8da588e288 | -19.19985 | -49.12556 | 2026-05-14 04:38:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5988d232-2d0d-3d3c-a133-a5d83d2f3ec3 | -11.73537 | -54.2434 | 2026-05-14 04:38:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5391a345-2945-322a-9b4e-10decabd5723 | -14.10758 | -45.29308 | 2026-05-14 04:38:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d93a26e0-7e18-3719-875f-3e639d69d18e | -11.74061 | -54.23985 | 2026-05-14 04:38:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 20815322-9832-36e2-a313-35b1259d97fb | -13.68779 | -44.29214 | 2026-05-14 04:38:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e3f6b107-4a7c-3863-be3f-cbb831e53dbb | -15.42466 | -56.31392 | 2026-05-14 04:38:00 | NPP-375D | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 15ad7805-7551-31cb-aa80-48ce1e09392e | -15.42388 | -56.31541 | 2026-05-14 04:38:00 | NPP-375D | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a72030b5-4e54-35c5-8cb7-4016143962d1 | -19.19261 | -49.12807 | 2026-05-14 04:38:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 95eec30f-5bc5-3d1d-ad90-44465a2d0d5f | -15.05436 | -42.95302 | 2026-05-14 04:38:00 | NPP-375D | MAMONAS | MINAS GERAIS | Brasil | 3139250 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6e2c4be9-6c4e-3ecd-9276-86ae2fae91e3 | -11.73618 | -54.23895 | 2026-05-14 04:38:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8061599d-b99a-3455-be66-98c99bcbd25a | -13.48382 | -47.4043 | 2026-05-14 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 97d0375e-296f-312c-96db-99c7f6f7c839 | -15.05488 | -42.94917 | 2026-05-14 04:38:00 | NPP-375D | MAMONAS | MINAS GERAIS | Brasil | 3139250 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ba4fb516-08dc-31ca-b397-c3688691955e | -13.47157 | -47.39497 | 2026-05-14 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d4ceda9d-a0b0-3ae1-a1fc-3ee6b532f080 | -11.74584 | -54.23632 | 2026-05-14 04:38:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a8926e31-b348-39ca-b515-c0d92a8bd533 | -16.7636 | -45.82026 | 2026-05-14 04:38:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 11fae6ef-1165-3a9f-8789-437ca1a7ad36 | -11.93324 | -54.0968 | 2026-05-14 04:38:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 346df40e-6cc2-3388-bdbc-f625433d8e09 | -11.93333 | -54.09846 | 2026-05-14 04:38:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c4d1f02a-f356-33f2-9e69-951e33e9ea96 | -12.45909 | -54.45115 | 2026-05-14 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ce659e7d-a2b8-325b-b28a-7dea9d2b42e3 | -12.54134 | -54.6188 | 2026-05-14 04:38:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f09ea36f-3c80-362f-b5f8-68d872ae12d5 | -14.11894 | -45.29057 | 2026-05-14 04:38:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 74441b2f-b727-3f25-be22-85c1ca9f73af | -11.93244 | -54.10115 | 2026-05-14 04:38:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c0d17a3-0975-379f-a7b1-7d141e28027a | -14.62735 | -48.01936 | 2026-05-14 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 817c0cc5-c1a3-3c62-aa0a-fa7cd80819b1 | -15.41991 | -56.31286 | 2026-05-14 04:38:00 | NPP-375D | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b82cc028-ae8b-3674-9dbc-4e44b8372aa2 | -14.65219 | -49.75578 | 2026-05-14 04:38:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eec5f16d-513b-319e-93c4-39220053abf8 | -14.11116 | -45.29363 | 2026-05-14 04:38:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0da2a3b-54ac-359e-9e3b-a760acc85194 | -21.55112 | -48.59115 | 2026-05-14 04:40:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9b915a8d-e489-39ea-9a95-37ab1f6a4bb6 | -21.55967 | -47.03216 | 2026-05-14 04:40:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fb822ff1-816f-3942-b795-efe81d29fb74 | -21.56325 | -47.03274 | 2026-05-14 04:40:00 | NPP-375D | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 16c6b9e8-df44-39df-8e84-61e210d9a0c1 | -25.01201 | -53.40107 | 2026-05-14 04:40:00 | NPP-375D | CASCAVEL | PARANÁ | Brasil | 4104808 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| af757991-dfcd-325a-970c-b4bdc952a00e | -29.04711 | -52.27677 | 2026-05-14 04:42:00 | NPP-375D | SÃO JOSÉ DO HERVAL | RIO GRANDE DO SUL | Brasil | 4318465 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 78db3b98-02bc-364e-801d-afc312a0e100 | -8.75261 | -50.23702 | 2026-05-14 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d20f3fb1-502c-37d3-afaf-d89b03508c88 | -8.11007 | -44.18122 | 2026-05-14 04:53:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a57b2dbb-484b-311a-9699-1d44e83be75f | -8.09971 | -44.17979 | 2026-05-14 04:53:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 53b2175f-1cf4-3fd7-bd72-824ee0026367 | -8.75201 | -50.24107 | 2026-05-14 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 84219223-131a-3304-9ef8-d176ef8de4bc | -9.46476 | -40.33947 | 2026-05-14 04:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 9.2 |
| febe25bd-9a1f-39ef-ad5d-6b4ab1225dd0 | -9.56513 | -44.57833 | 2026-05-14 04:53:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 178f204d-3ffd-32b2-a6ba-25865c7ffc90 | -8.10489 | -44.18051 | 2026-05-14 04:53:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b67ba655-88f6-3dd0-924e-329e235d0139 | -8.54504 | -45.98446 | 2026-05-14 04:53:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 93cfedd7-3e99-3fba-9d66-1962625c42d0 | -9.55999 | -44.57753 | 2026-05-14 04:53:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README5.md)
