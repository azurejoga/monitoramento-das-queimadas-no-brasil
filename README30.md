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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5133ed51-1cdf-33b7-9fe9-22b42770b6d3 | -5.79369 | -43.76668 | 2026-09-20 04:19:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2fc91f5d-e7a7-342c-85e5-e90642b8aa9e | -6.9344 | -43.10267 | 2026-09-20 04:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0af95615-d201-3546-95e2-226e33fd7711 | -7.42769 | -44.7392 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a348159d-94c7-3d61-bc1b-ad53b8e8984c | -11.48074 | -47.76234 | 2026-09-20 04:19:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 47e61b74-b1be-38ad-a0b6-66aead93de6a | -11.60549 | -47.04505 | 2026-09-20 04:19:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c32f37d-c73f-36f4-8aec-097a57cb57a8 | -7.08164 | -44.01471 | 2026-09-20 04:19:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a59c8ca9-bc8d-36c2-af20-d9ad43e45f5f | -8.18686 | -40.82263 | 2026-09-20 04:19:00 | NPP-375D | ACAUÃ | PIAUÍ | Brasil | 2200053 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d43ad0e1-6321-337f-8c96-e5f52e08e93d | -5.34969 | -44.82388 | 2026-09-20 04:19:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5e7fb63c-c3bf-3b1c-bec3-5a1b6348e760 | -5.75887 | -43.69371 | 2026-09-20 04:19:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e9d15051-aa4c-3532-b17e-6277d7ff5b87 | -5.55115 | -45.54184 | 2026-09-20 04:19:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b3b7c971-4096-300b-8b22-16dc2368a8be | -11.09037 | -48.28506 | 2026-09-20 04:19:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 30b365ca-fde1-3991-9810-734dd91a8ec9 | -11.42488 | -45.4087 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4777d4af-7e13-386d-8a46-1a532a4cf27a | -8.62847 | -47.61656 | 2026-09-20 04:19:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1841060b-58a8-3b0a-ad84-013c846067ea | -11.43347 | -45.42267 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5466e53b-188e-351f-a732-effb70d39a0f | -7.08634 | -44.72857 | 2026-09-20 04:19:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6f9d83a3-15f2-30d7-af5d-3bd4087529cb | -8.50271 | -47.44229 | 2026-09-20 04:19:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9b9df6b5-7b01-31bc-852e-ee6eba72e830 | -6.31518 | -41.75368 | 2026-09-20 04:19:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9a613708-2b3f-38ff-bbbc-10de140bb124 | -9.12609 | -45.72922 | 2026-09-20 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 20.2 |
| f56a7a9d-3757-349d-a076-68938ac49b9c | -4.29485 | -48.62888 | 2026-09-20 04:19:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a888b6d5-0d78-30ca-bbb9-a0530941521f | -5.84287 | -53.51132 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c6a70c7c-29fa-398d-8d8d-33738fefe15e | -8.43873 | -46.84052 | 2026-09-20 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 54600cc3-e55d-3eb9-a5a4-dab8997246aa | -9.03 | -48.76226 | 2026-09-20 04:19:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 44837494-376e-33a5-9180-edf8b6b5b878 | -7.42924 | -44.75219 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4de10f7f-192f-3fd1-92c3-8503bf6352c8 | -5.86644 | -51.57072 | 2026-09-20 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 010921a8-bcf8-320d-9362-a4508fdec4c8 | -9.82795 | -46.44828 | 2026-09-20 04:19:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5fe71389-c530-3ef7-b5d6-da28d639487f | -7.34774 | -44.61358 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 37f83f03-6bc6-38de-a467-7ed0e9379574 | -6.9954 | -42.19835 | 2026-09-20 04:19:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4118381e-ce32-3aee-b32f-4e1e35623af0 | -9.04268 | -48.76912 | 2026-09-20 04:19:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8556f552-62ff-3e39-ba5a-fa312792d5cf | -10.19881 | -44.14471 | 2026-09-20 04:19:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d3e22f18-993b-3cc0-9318-d5d2280246fc | -8.02828 | -49.54673 | 2026-09-20 04:19:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c2832a97-75cd-337b-ba30-78bd9e722a1d | -7.74555 | -46.73844 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bdedf093-1a40-31c4-934a-4d8d6569c7e4 | -7.59412 | -55.70907 | 2026-09-20 04:19:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a752febb-bd6a-3776-a82f-eb60f8ec150f | -6.29904 | -47.61671 | 2026-09-20 04:19:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9e357302-fc08-34af-bd28-ef089b15f7fe | -9.87702 | -45.61461 | 2026-09-20 04:19:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 884dbad2-43c0-319b-99b8-cefac0279cbf | -8.17757 | -54.76165 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9d783a3a-a82f-3e7e-b278-3f12a5569009 | -10.41231 | -48.91283 | 2026-09-20 04:19:00 | NPP-375D | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5ca6a6d1-7e01-37cd-b0c6-d72f8c2f2dc3 | -7.35799 | -44.86816 | 2026-09-20 04:19:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 95699f24-8c07-34cd-9a20-37ddcf8ab890 | -10.29781 | -45.4248 | 2026-09-20 04:19:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| eb773250-3aba-33fd-8304-8841c59065db | -4.84321 | -42.83496 | 2026-09-20 04:19:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e6007067-e5d7-3d46-b22b-6c22865c71b6 | -8.38483 | -45.63012 | 2026-09-20 04:19:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 928efd58-e6d8-3a09-b8e9-41d76334f76d | -11.22453 | -48.35754 | 2026-09-20 04:19:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2139ec5-3ad3-3d08-ba5a-e1ff3caaad0b | -8.76154 | -48.65342 | 2026-09-20 04:19:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f4b22b6f-1486-34fd-af67-c93a5d06d8d8 | -10.32219 | -48.00252 | 2026-09-20 04:19:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 53e85fd1-08c6-3d68-a8e6-1b3b5445c5c1 | -5.82422 | -44.13417 | 2026-09-20 04:19:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7f1e6bae-3957-3533-9b7a-7fa9018c2093 | -11.66003 | -43.43157 | 2026-09-20 04:19:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f4ec9ab3-ae5a-3bba-8905-8cb31f6132ea | -5.76236 | -43.69426 | 2026-09-20 04:19:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 01985151-4c3a-3bec-9ad9-29148b4bed1b | -9.27368 | -48.24144 | 2026-09-20 04:19:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 84fca087-8494-3ae8-b6ee-fbcd8beaf472 | -6.17282 | -47.49101 | 2026-09-20 04:19:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bcb44ad5-4820-314f-a5cd-f648ec16247a | -7.392 | -47.77428 | 2026-09-20 04:19:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 21f84a35-b6f3-3c37-bb8a-5499446f7ef8 | -7.80224 | -44.93671 | 2026-09-20 04:19:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e2fff2d6-0089-3693-be5d-502580559a76 | -8.38289 | -47.19316 | 2026-09-20 04:19:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ea1070b7-2278-3941-ae4d-4343781746f1 | -6.29179 | -47.60678 | 2026-09-20 04:19:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0d45adb0-1927-3dc7-aec7-e1d668ae1c91 | -11.2189 | -48.36467 | 2026-09-20 04:19:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 33d43d16-7319-30cf-b24f-bf73f3ffc2e5 | -10.41533 | -48.33586 | 2026-09-20 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0dd619c4-8af5-37d2-9e6d-911bea3738a3 | -7.50032 | -46.13023 | 2026-09-20 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 02c7960b-f363-37b4-992d-09990674fc38 | -10.18855 | -44.14304 | 2026-09-20 04:19:00 | NPP-375D | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3a25bd8e-ea15-38a0-af22-22f27e6baefe | -10.30381 | -50.25636 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2dc8c93e-fe15-351b-b6a1-44450cf27082 | -5.8529 | -53.5297 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1da0e045-47a7-3906-860b-6dc560dad88c | -7.15485 | -47.46032 | 2026-09-20 04:19:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 42fc41fa-c725-3572-b1c5-f3c08733919d | -11.97726 | -44.99753 | 2026-09-20 04:19:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6a7feff4-d56b-3501-a5c7-8ef0fc8c3f27 | -8.04917 | -46.29443 | 2026-09-20 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f446932d-d848-3ba3-82a0-77643eca2b94 | -5.93239 | -35.6158 | 2026-09-20 04:19:00 | NPP-375D | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c336a015-8799-3aef-b3ae-f155875071d4 | -11.0302 | -48.30651 | 2026-09-20 04:19:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 586e3e54-5cf1-32f9-b4f4-fa194a5b62f1 | -5.93665 | -35.61647 | 2026-09-20 04:19:00 | NPP-375D | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fbd4a8e8-5dcc-31e8-908b-12ac47912ca2 | -2.9729 | -54.76813 | 2026-09-20 04:19:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 605b5cbd-ad44-380c-977e-c8446db57036 | -9.56046 | -46.55904 | 2026-09-20 04:19:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 42335ae0-615d-3697-89f9-2edadf15dc8d | -10.31447 | -50.22496 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| d5a59e94-b001-32ea-91bf-44cf1aa80724 | -10.55063 | -46.74455 | 2026-09-20 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 36dead72-3dd2-3849-a588-8b7b1d325433 | -10.31973 | -50.21039 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 8a809422-af1a-3ae6-a6b7-2433a4c2029b | -5.84602 | -53.5644 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3c5f6efb-2835-333f-abb3-cb3b048254ac | -7.42856 | -44.75629 | 2026-09-20 04:19:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3f77a1af-bfda-3a22-80b8-c791e5b8b658 | -8.17087 | -54.7604 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b24213c4-b3a2-317f-8dfe-0cc8a29d9e3f | -6.9531 | -43.09457 | 2026-09-20 04:19:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d191333-b47f-3a77-946a-f5eae3ef76ba | -5.09379 | -42.66599 | 2026-09-20 04:19:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8ae42ff3-4b0e-36d5-bbbf-16d775839a24 | -6.6136 | -50.06338 | 2026-09-20 04:19:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7183aa0e-0de2-3db3-a495-e05f17572176 | -5.84914 | -53.55077 | 2026-09-20 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e7a20170-2f20-39f6-8352-e7c63d1ff833 | -9.28143 | -48.19629 | 2026-09-20 04:19:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca3faf62-5327-3621-bd7c-8d8794966215 | -10.46313 | -45.09386 | 2026-09-20 04:19:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 57879dd1-9678-33af-97ed-d267a25f3000 | -7.55949 | -45.40976 | 2026-09-20 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 57111162-9ad3-3092-9097-8c37379f5101 | -7.36057 | -44.87383 | 2026-09-20 04:19:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e590c9c-509f-3ce5-b7ae-6b0b5f0b403c | -9.67425 | -54.3233 | 2026-09-20 04:19:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d4153605-dbcf-3611-b1a2-a67e242768af | -10.29738 | -45.42215 | 2026-09-20 04:19:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 33d14e2e-ef25-3a92-9aa5-1936dc3e7593 | -8.38391 | -46.51708 | 2026-09-20 04:19:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 29334ed2-93de-3b45-bfe2-4358a13363a3 | -7.01882 | -45.24707 | 2026-09-20 04:19:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| f24bfeb3-3dfe-3e06-9617-a789d8103a71 | -9.12832 | -45.71587 | 2026-09-20 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f8d957f8-0068-38d4-8d0b-bf539c69d111 | -5.79782 | -43.76335 | 2026-09-20 04:19:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7454340-f1f1-3474-8ea0-f9917b564de8 | -6.35717 | -43.36474 | 2026-09-20 04:19:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f9dcf104-f1eb-3524-b33d-5ec6c74ece00 | -9.27468 | -48.24454 | 2026-09-20 04:19:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2889f776-b8b8-39bc-aca4-9d8c7cc5d80c | -10.5528 | -46.75496 | 2026-09-20 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 226d363e-7c22-3010-b932-9ba099447cd3 | -9.5812 | -55.10257 | 2026-09-20 04:19:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb0a10ce-ff47-3f16-bec8-9206d784febf | -9.12016 | -45.71914 | 2026-09-20 04:19:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 527b676e-2d66-377a-bf97-a8fe04025865 | -6.20238 | -45.32324 | 2026-09-20 04:19:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 49a2dfbb-32e5-3470-94b5-6e72b3fce7de | -11.01024 | -46.52422 | 2026-09-20 04:19:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a5d4c2e8-7f35-3967-9aa8-ff7a22058019 | -8.47868 | -44.51979 | 2026-09-20 04:19:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dfb47915-5fb5-3612-b707-c8d2aec1dd83 | -4.29967 | -48.62965 | 2026-09-20 04:19:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bccecd7b-b821-370e-baa1-4112a220c122 | -8.43757 | -46.87207 | 2026-09-20 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3987a39e-20be-37a8-a34e-1430913842fb | -10.31641 | -50.21421 | 2026-09-20 04:19:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| d8c61025-530a-371d-bbd5-39450d459860 | -6.2025 | -47.52543 | 2026-09-20 04:19:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c63f88ea-5709-32a4-9ed7-a9ffe9d6bb35 | -8.13283 | -46.81068 | 2026-09-20 04:19:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8eabb7a5-8780-3446-8a94-a952cc2a86bd | -7.53016 | -45.88512 | 2026-09-20 04:19:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |


[Clique aqui para ver as próximas entradas](README31.md)
