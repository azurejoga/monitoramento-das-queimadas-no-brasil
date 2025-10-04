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
| 1d25b932-8e9c-393a-b83e-6229300e6344 | -7.7218 | -46.30125 | 2025-10-04 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a9dc55ff-79bb-3205-b50a-5df8a5451284 | -10.8367 | -41.27187 | 2025-10-04 03:51:00 | NPP-375D | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 154385c5-4ded-3f7f-ac21-d41a2d22a0f3 | -5.48727 | -44.10449 | 2025-10-04 03:51:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| c4f0cddb-7865-30b0-8c9f-1fb69ec0e11b | -10.61224 | -49.15587 | 2025-10-04 03:51:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 56a09d35-73ae-3ac8-99d9-8d2971660965 | -6.07536 | -42.51114 | 2025-10-04 03:51:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 22.9 |
| c1215556-7ae0-3fd5-91b1-53f665b07a3f | -9.94007 | -50.24159 | 2025-10-04 03:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 70a98d97-6ce2-38fb-9f8d-e468661ba6d9 | -6.34286 | -43.442 | 2025-10-04 03:51:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1d468983-f9b3-3869-a95e-372bce745fc7 | -4.88885 | -45.0628 | 2025-10-04 03:51:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aae3ab97-81ee-39f5-932b-671585aa643c | -7.36902 | -39.17749 | 2025-10-04 03:51:00 | NPP-375D | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 5b9a7693-b796-352e-a919-b4849c64ec15 | -5.87777 | -42.52407 | 2025-10-04 03:51:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 025084fc-d543-3c9f-98d8-d67fed5a7ee0 | -10.74113 | -44.70118 | 2025-10-04 03:51:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1bdef2e2-e928-3b90-92b1-b388f0b9ca89 | -7.04301 | -44.34006 | 2025-10-04 03:51:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 63601166-15d0-3251-8d8e-a3c615499a3e | -6.24581 | -45.34843 | 2025-10-04 03:51:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 063c9285-1435-35d8-8154-9a2cf1c9723b | -11.48115 | -44.97441 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80464ca1-ea3c-3006-bcc2-f99c494119ac | -5.87378 | -44.27468 | 2025-10-04 03:51:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7738dc3e-0553-3503-8a24-ed65bd82913d | -10.57862 | -41.49858 | 2025-10-04 03:51:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 256f4e7a-bcb1-3029-8f60-61dd49c7252e | -8.84826 | -46.79405 | 2025-10-04 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 944601ab-a65a-374f-bc4f-ed5e1a99905e | -11.50685 | -45.01192 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5de6c2d6-6580-3485-a57c-4031d1ad5c1b | -6.37627 | -43.89929 | 2025-10-04 03:51:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 76e5face-aeed-3d97-b2cf-fb71903ca45c | -11.17008 | -47.75167 | 2025-10-04 03:51:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f84ef591-f9d5-3927-a7b8-2c462b832f34 | -7.74074 | -42.59851 | 2025-10-04 03:51:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 1a3a425f-c255-3b99-a470-ec648e8ab1e8 | -8.17439 | -44.13614 | 2025-10-04 03:51:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 88b7c0be-1b23-32c9-b3ea-8897dd12c096 | -7.79288 | -42.56849 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 7f87e08a-c039-398a-a73c-106ad40c06b3 | -6.24942 | -45.33775 | 2025-10-04 03:51:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 27ab1655-e4ee-3be3-bd0a-386a819006cf | -6.99015 | -42.7986 | 2025-10-04 03:51:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| c871c9ea-9e3b-3e06-af59-d312901f7d5c | -8.63144 | -43.98958 | 2025-10-04 03:51:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4109802b-00cf-362e-9959-ee6039fc7b29 | -7.72759 | -42.60022 | 2025-10-04 03:51:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9b8ad82f-16d6-3d48-97b6-a5bd272c7837 | -6.24064 | -45.34769 | 2025-10-04 03:51:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d75985a5-7e97-3952-a842-549b723dfb45 | -6.37737 | -46.51436 | 2025-10-04 03:51:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 454baa6f-c2ff-3141-833e-e324f729b0b6 | -8.05534 | -44.79686 | 2025-10-04 03:51:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0078dba4-8582-38ee-9fbb-9de833f0574c | -6.24139 | -44.22023 | 2025-10-04 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c5c7ae0c-7c96-3f47-94e2-36aac8623033 | -6.06553 | -42.51767 | 2025-10-04 03:51:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9c6e3cd3-f976-396d-a07a-8673db757092 | -5.94062 | -42.89139 | 2025-10-04 03:51:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 11274b69-d4eb-3ee7-ba7a-0311afaeff42 | -8.17519 | -44.13165 | 2025-10-04 03:51:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 46fbe3fa-41f6-378a-8496-fdef1f021d62 | -5.08308 | -44.09196 | 2025-10-04 03:51:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 8ba61530-4651-310c-bd92-bbb891b43b34 | -11.06297 | -47.78666 | 2025-10-04 03:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6e529e50-2133-3b4b-ae1f-d78bc02cbf8d | -7.04446 | -43.22194 | 2025-10-04 03:51:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 55376a64-3981-3f6f-bbee-d5475b13d951 | -11.42817 | -43.48782 | 2025-10-04 03:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c73cf0b2-5de1-30c1-b3e6-a43314e295fa | -6.27522 | -42.45024 | 2025-10-04 03:51:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| edf27bf4-b8b7-3d06-92e2-fff1df00b514 | -5.84931 | -42.79468 | 2025-10-04 03:51:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c493fe32-07d4-3335-8e74-68eb55fdd067 | -7.70176 | -42.57609 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f435bb85-82a3-3758-8125-98d45452e0b1 | -11.48025 | -45.03263 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b0879e7c-e84f-3089-aaa5-ae723ab1e8e8 | -7.0649 | -43.23441 | 2025-10-04 03:51:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5ca81611-c926-39cc-9a75-ec6ab5b89f60 | -5.19685 | -45.07666 | 2025-10-04 03:51:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 22.0 |
| abd7f011-aa44-3ac0-adc4-03f89f3dc614 | -6.67615 | -44.19982 | 2025-10-04 03:51:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 03542547-52d9-3557-90a5-f06ce9da3865 | -6.27035 | -42.45336 | 2025-10-04 03:51:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 0ef1acf2-104c-3e5f-9acb-1d8392cce345 | -6.29823 | -42.49487 | 2025-10-04 03:51:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c0deb1e1-6d91-3f88-a23d-613b65660224 | -6.07894 | -42.5159 | 2025-10-04 03:51:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 2146c3a2-0a47-3e38-b158-18e88828d9a3 | -7.06197 | -43.22522 | 2025-10-04 03:51:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| f94c7f87-355f-3536-841c-efd13bd28411 | -10.32419 | -50.33607 | 2025-10-04 03:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 5f6e3959-c9ab-3263-af14-5ab095239278 | -6.67056 | -44.20397 | 2025-10-04 03:51:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b6081c3d-852b-3a62-9704-f5cf22e9b395 | -6.076 | -42.50724 | 2025-10-04 03:51:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 22.9 |
| 4976b01f-422b-3a8b-b022-b2ce41744ab4 | -5.1436 | -44.80761 | 2025-10-04 03:51:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fba2e1e1-c0e2-35d8-ac0e-4fc67b8ca58c | -9.76422 | -48.58846 | 2025-10-04 03:51:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9ab4a835-8dae-3314-80c4-5d4556d9a65a | -5.97843 | -44.09714 | 2025-10-04 03:51:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cae35bc4-fdc0-3d86-a5fe-3a1e3915c177 | -5.69675 | -42.84599 | 2025-10-04 03:51:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| a1d10c44-aec6-375b-8cce-2b2ce9b632d9 | -6.05412 | -42.5074 | 2025-10-04 03:51:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a65a3046-2fd2-3a92-bfe8-b2898e5a6c2a | -10.32194 | -50.34746 | 2025-10-04 03:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| a9c6b293-cf0e-38f2-a14a-21ebe5bae205 | -5.26246 | -37.92067 | 2025-10-04 03:51:00 | NPP-375D | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a53714a3-80d1-3124-893f-bce4b53765d1 | -9.9106 | -43.72017 | 2025-10-04 03:51:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a3131c88-fc6d-344f-986b-ab7252fee123 | -7.80081 | -42.54656 | 2025-10-04 03:51:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 4be4b004-d003-3a95-bc95-218f15c4c119 | -9.66337 | -42.93338 | 2025-10-04 03:51:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d5f73378-6c5e-39d0-b89b-19a9a0ec2813 | -4.7029 | -45.60555 | 2025-10-04 03:51:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1a358621-a84a-3d43-bbea-6610828b4c8d | -5.85775 | -42.20873 | 2025-10-04 03:51:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8b0e9a8a-564f-3e5c-bd4c-c888be1976ac | -6.26551 | -42.45638 | 2025-10-04 03:51:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c26eb636-e29f-3585-b307-63fe1c67eca1 | -11.4914 | -44.99286 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d3729520-be87-39f1-9e3c-99ea7ba99de2 | -8.5205 | -50.03166 | 2025-10-04 03:51:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17b6ec66-98c6-37ca-902f-4c8dd73ffb2c | -5.83568 | -42.87471 | 2025-10-04 03:51:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 53b326f0-0f8c-3d67-8d60-9a4cd7074268 | -11.46286 | -45.14656 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b56bd3d1-7b82-36a3-99db-11763ebba0f5 | -11.48131 | -45.02165 | 2025-10-04 03:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f7709f3a-59e9-3e87-820d-aabf2323cd6b | -5.26237 | -39.26249 | 2025-10-04 03:51:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c6a2f921-df2b-3810-b691-855efaff4ddf | -8.98974 | -47.48777 | 2025-10-04 03:51:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6beda1dd-e9bc-34bc-b4f2-68688d8547eb | -10.72436 | -47.88599 | 2025-10-04 03:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dba193ae-5286-34e5-b94b-663f98ab4607 | -6.99477 | -42.33755 | 2025-10-04 03:51:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| df10429f-2c7b-3212-9c2b-50a16ce1528a | -5.20618 | -44.35484 | 2025-10-04 03:51:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e2686e38-89ce-3939-8fc0-495db1401af0 | -6.59412 | -44.62254 | 2025-10-04 03:51:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 520191f8-5752-3d51-8d07-74102bd35f6b | -5.68729 | -42.84878 | 2025-10-04 03:51:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| f19c85b9-2e49-3224-99d5-2cacf81a2d5c | -10.32171 | -50.3354 | 2025-10-04 03:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a0c2b60c-7cf1-3850-9550-164f89b757fe | -10.32827 | -50.33674 | 2025-10-04 03:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 0f956123-a44b-3cc8-b278-1418c91c2c67 | -5.2442 | -45.54881 | 2025-10-04 03:51:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ae1cca0b-cdac-347c-a5e3-ddfdf4c45d18 | -7.73906 | -46.26675 | 2025-10-04 03:51:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1896efb5-0133-3423-8d40-b7b5c2df2754 | -8.22375 | -46.80513 | 2025-10-04 03:51:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 62a81cb1-3498-341c-a1a0-2a3082c12003 | -4.43242 | -43.24189 | 2025-10-04 03:51:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f3e62b3e-b806-3d55-934d-dbfc65fcbf60 | -8.20116 | -46.99561 | 2025-10-04 03:51:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 71012dc1-ec42-306f-b515-d026bae4ae9b | -6.87861 | -44.49911 | 2025-10-04 03:51:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| caa5237b-d144-305a-9afb-39af03d2cce2 | -17.98503 | -45.00768 | 2025-10-04 03:53:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ce5d5122-ca19-3e16-b830-051fcc227bf3 | -17.08091 | -46.23608 | 2025-10-04 03:53:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4d64d3b9-8fb9-3262-a5cb-f71e95c6e951 | -14.63004 | -48.25932 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 144e273d-4c69-3af9-b20b-3e8d021c77c3 | -12.07741 | -47.98919 | 2025-10-04 03:53:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 03b4b38d-5cbf-3dfb-a939-e359fb79724b | -13.30159 | -47.58887 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f64614de-8714-30bf-947a-d3340eff9362 | -13.99857 | -48.20067 | 2025-10-04 03:53:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 575093af-32f9-3c20-a0a4-ba998a76a88d | -13.24273 | -48.49107 | 2025-10-04 03:53:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 60a1c3ee-4cd1-344b-a363-4e2d942ac0e9 | -15.7935 | -46.26298 | 2025-10-04 03:53:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 615d779a-6ac2-3895-b810-dd559bc49b14 | -13.67579 | -47.30714 | 2025-10-04 03:53:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9796a30c-6e5f-3403-960b-72f762b2d916 | -11.559 | -47.67626 | 2025-10-04 03:53:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 938a3023-f2df-3af9-a574-7ec3f30c7d2f | -14.74277 | -48.14133 | 2025-10-04 03:53:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5fd31fc9-2293-3354-a10f-838ed01b39ff | -13.3888 | -47.55728 | 2025-10-04 03:53:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5c7a7ca2-4b60-3892-a1c0-14a633b59cff | -14.86962 | -48.13052 | 2025-10-04 03:53:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ab7e4e6-49fc-36b8-b124-d68aefa4115b | -14.20862 | -46.07714 | 2025-10-04 03:53:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 65f96abd-0b7a-31ca-b1db-3dbb00e26f37 | -13.35428 | -47.23721 | 2025-10-04 03:53:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README33.md)
