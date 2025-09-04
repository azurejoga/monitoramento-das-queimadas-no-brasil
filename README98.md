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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cdba9c47-12f2-3c22-b034-41caa73bb8c6 | -4.83828 | -42.73986 | 2025-09-04 12:14:00 | TERRA_M-T | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 2a55e949-54a8-3edc-a4f9-5b478c830c44 | -6.42609 | -43.61896 | 2025-09-04 12:14:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 02950bf2-7c72-33d9-b75b-e0c6c128489d | -7.70347 | -48.75575 | 2025-09-04 12:14:00 | TERRA_M-T | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 158.1 |
| fbd323ed-f253-3688-8102-4812e5563b8d | -8.03067 | -45.38904 | 2025-09-04 12:14:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 86f0ac3a-fca5-380f-8c04-dbdce800d033 | -6.40587 | -38.41063 | 2025-09-04 12:14:00 | TERRA_M-T | LUÍS GOMES | RIO GRANDE DO NORTE | Brasil | 2407005 | 24 | 33 | nan | nan | nan | Caatinga | 21.7 |
| 15bb9b4c-dda1-367a-8036-8a70dec5a20d | -6.3424 | -43.38497 | 2025-09-04 12:14:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| a3f91684-2e70-3b5c-9503-561c1e9502a5 | -5.80004 | -43.62405 | 2025-09-04 12:14:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 8749d905-21de-305e-8587-29b485bd1a5c | -5.73623 | -45.56796 | 2025-09-04 12:14:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 7924a515-41d2-3f07-a1f8-23e966d22d8b | -8.03007 | -44.07236 | 2025-09-04 12:14:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 16.0 |
| c4c49e7c-e423-350c-886c-4f770ba778f2 | -6.37719 | -42.99692 | 2025-09-04 12:14:00 | TERRA_M-T | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 751cdd1d-0d21-364f-9c5b-c5b8f46e3115 | -4.31398 | -40.15633 | 2025-09-04 12:14:00 | TERRA_M-T | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 25.3 |
| 87f27a85-f723-3ca9-8c06-dda9d505fd0a | -8.01485 | -44.77943 | 2025-09-04 12:14:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| f810cb30-c530-370e-900a-f223fe2eb31a | -6.03821 | -46.67172 | 2025-09-04 12:14:00 | TERRA_M-T | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 3aa10868-94e8-3c15-a421-a2fc5758748e | -7.70186 | -48.76634 | 2025-09-04 12:14:00 | TERRA_M-T | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 205.7 |
| 53835196-0782-34b9-adf5-d13b33d79b95 | -7.69715 | -48.73303 | 2025-09-04 12:14:00 | TERRA_M-T | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 04fe4698-bc88-3d7a-a1dd-a4c7927b5abc | -5.98077 | -42.98563 | 2025-09-04 12:14:00 | TERRA_M-T | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 22.2 |
| 80d474b3-e0d7-3e4c-a4a8-e5ef7bda7ee0 | -6.87497 | -44.82583 | 2025-09-04 12:14:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 6ed3d7eb-3478-3d31-b011-7b131f107178 | -4.31627 | -40.14006 | 2025-09-04 12:14:00 | TERRA_M-T | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 45.3 |
| 077f8c3d-4168-3283-b4d2-de6054b17119 | -8.02174 | -45.38781 | 2025-09-04 12:14:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 17.8 |
| b3f499fa-bf8a-3f86-b7c1-10cac7f758fd | -6.91003 | -46.89502 | 2025-09-04 12:14:00 | TERRA_M-T | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 85287c27-1ad9-353e-a012-d3745433dc54 | -6.23253 | -42.71443 | 2025-09-04 12:14:00 | TERRA_M-T | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| d445a153-8d1c-3ce1-a2d2-c3ff22debb19 | -7.91434 | -45.23074 | 2025-09-04 12:14:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 6ac5ba88-b2f3-3a3a-909a-87f46fdd5586 | -5.82974 | -45.37068 | 2025-09-04 12:14:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 0a3258f3-47e1-3a98-a609-f1866ef6d59f | -6.54328 | -43.91756 | 2025-09-04 12:14:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 9fb792de-d576-348e-81b1-7b3a1c08d566 | -6.21837 | -45.0405 | 2025-09-04 12:14:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 2cfcc8de-90f2-3f1f-bd35-182c4f8f4c0d | -5.68699 | -45.59708 | 2025-09-04 12:14:00 | TERRA_M-T | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| fdf3d2f5-8628-358a-953a-226cc80e2806 | -5.88294 | -43.23888 | 2025-09-04 12:14:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 7.8 |
| d81053be-9cd2-368b-aac1-8d6a4d32735a | -6.80125 | -45.34157 | 2025-09-04 12:14:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| b8298c38-f781-353b-bb5d-9dfc9944fbfc | -7.65021 | -44.75219 | 2025-09-04 12:14:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d850ca52-74b9-3417-bb5d-db5f0fcec78a | -5.71913 | -45.17085 | 2025-09-04 12:14:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 6d19bdc0-4f5e-3881-8163-c008948d72c0 | -6.55048 | -43.91427 | 2025-09-04 12:14:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 3807763b-17d6-306e-a1bd-4b4b25d322c6 | -6.79396 | -44.4866 | 2025-09-04 12:14:00 | TERRA_M-T | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| d49208f1-2db7-3cce-af9c-c80538743775 | -6.12823 | -42.94498 | 2025-09-04 12:14:00 | TERRA_M-T | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 17.8 |
| e6f37f63-2219-39a8-bbee-c5dfb9cc66cf | -6.91935 | -45.5522 | 2025-09-04 12:14:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4d36f41c-eff3-3bcb-b2a8-87e6ecfd4eb9 | -6.20788 | -43.33959 | 2025-09-04 12:14:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 6e93bda7-222c-3cd0-a781-f54fc93ebd76 | -8.08304 | -45.34084 | 2025-09-04 12:14:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 40.0 |
| b83354dd-a21e-3393-8927-b583231ab754 | -5.68825 | -45.58826 | 2025-09-04 12:14:00 | TERRA_M-T | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 40902409-301f-3cfe-ac10-47b9e12e7135 | -3.7061 | -44.16167 | 2025-09-04 12:14:00 | TERRA_M-T | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| cff7d09d-b18c-3184-87f6-23b814af6096 | -7.90409 | -45.23864 | 2025-09-04 12:14:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 2fc1f317-b433-3897-990c-2f1809aee228 | -6.12965 | -42.95107 | 2025-09-04 12:14:00 | TERRA_M-T | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 2f310cfd-45d6-3ac2-ad94-f7d2feef4f3a | -6.78612 | -44.08821 | 2025-09-04 12:14:00 | TERRA_M-T | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 4e66c86b-d273-33bd-8fd8-6da37f290e99 | -4.90503 | -41.75576 | 2025-09-04 12:14:00 | TERRA_M-T | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 22.1 |
| dae4e73a-ab82-37e6-a84c-a407fe100500 | -6.8915 | -45.5574 | 2025-09-04 12:14:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 79.0 |
| c696217a-3dc7-3e64-8136-009e608975cd | -5.97396 | -44.74806 | 2025-09-04 12:14:00 | TERRA_M-T | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a07fde71-d957-36fd-858b-8e38d9cadbe0 | -5.9456 | -43.02503 | 2025-09-04 12:14:00 | TERRA_M-T | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 9103efa9-2144-34ef-b85a-17f2991fd2f4 | -8.02047 | -45.39684 | 2025-09-04 12:14:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| d888ad44-3bd3-300d-a95c-1c00d337bff6 | -8.08941 | -45.36007 | 2025-09-04 12:14:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 3319c4b7-036f-39d2-90b3-21ac50d1daf3 | -7.35939 | -44.32938 | 2025-09-04 12:14:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d4f72091-c8d0-3296-baf1-31b64d9109f7 | -6.87125 | -45.5728 | 2025-09-04 12:14:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| af3c0e97-50a3-3c13-8d9a-4f3f586d7a0d | -8.08176 | -45.34983 | 2025-09-04 12:14:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 7a5d56ed-291d-384d-8af4-45576a2fde94 | -5.61184 | -45.02254 | 2025-09-04 12:14:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 5a02caee-4cfe-349b-93ed-dbe2f6d9ab80 | -5.78188 | -45.31284 | 2025-09-04 12:14:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| f1b5a2ed-3729-3e23-ba65-14f3716ef18c | -5.75013 | -45.53392 | 2025-09-04 12:14:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 4c02a859-4fcd-3e18-b859-9b4297b5a6e8 | -5.68446 | -45.6147 | 2025-09-04 12:14:00 | TERRA_M-T | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 769.8 |
| 56175774-3c4e-308f-a599-0b9179679927 | -5.77314 | -44.86505 | 2025-09-04 12:14:00 | TERRA_M-T | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 4f9c0da3-3c06-3677-b546-fd88f8fd8708 | -6.28677 | -43.50468 | 2025-09-04 12:14:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 8cc44e11-6edc-31ea-8644-6384f4c67e61 | -7.39045 | -39.68462 | 2025-09-04 12:14:00 | TERRA_M-T | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 20.3 |
| 0158b74b-7f29-3ba6-9585-a95794f51659 | -5.70898 | -45.17851 | 2025-09-04 12:14:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| c3e857c3-21a0-33a0-a4b5-a6b624e2d2cd | -5.89788 | -42.99083 | 2025-09-04 12:14:00 | TERRA_M-T | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 13.9 |
| 64bf2505-f02e-34f3-acba-0467c6135362 | -5.78315 | -45.30397 | 2025-09-04 12:14:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 041d9e4a-9e20-3581-85ee-827fd2614be5 | -4.90325 | -41.76842 | 2025-09-04 12:14:00 | TERRA_M-T | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 136.6 |
| 342eb345-ad2e-33eb-baf2-93b6655cfcd7 | -8.04982 | -44.13663 | 2025-09-04 12:14:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 091b162d-7467-37a9-b962-755f802336df | -5.6918 | -45.93929 | 2025-09-04 12:14:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| e0d23cc6-0881-314e-be28-f2dffde7ab54 | -7.36074 | -44.31966 | 2025-09-04 12:14:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 20.2 |
| c837b1a3-cab8-3dd6-ade9-9afc4141f48b | -5.541 | -43.77156 | 2025-09-04 12:14:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 78f86f67-d5e6-3954-a35d-e9bda72cd53d | -5.33773 | -49.01084 | 2025-09-04 12:14:00 | TERRA_M-T | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| c1f067fc-ec9d-3807-a1de-1e8595fe70e3 | -7.04725 | -43.25903 | 2025-09-04 12:14:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.3 |
| b779bdcc-3dd5-3523-90e7-9dbd5ae98790 | -6.27307 | -43.32214 | 2025-09-04 12:14:00 | TERRA_M-T | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 6a2c23c2-413f-35ac-8657-95638e13eafe | -4.78796 | -43.81626 | 2025-09-04 12:14:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| b02c0dfc-7554-37c2-8f31-face2077911b | -6.30295 | -44.76551 | 2025-09-04 12:14:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 33e2f6d5-4c14-3abc-97e9-aac51b56a82e | -5.80142 | -49.12818 | 2025-09-04 12:14:00 | TERRA_M-T | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| b1188b56-0d3f-302e-94ec-95f7c4e2539f | -6.83259 | -44.27844 | 2025-09-04 12:14:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 810a4bec-5478-3fe5-88b0-f29195245ae3 | -5.74886 | -45.54274 | 2025-09-04 12:14:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| e765cbaf-b943-3649-9002-8b89af2fe451 | -5.63646 | -43.68068 | 2025-09-04 12:14:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 0f357b23-6898-3e5f-8d48-170d2f460738 | -5.71025 | -45.16963 | 2025-09-04 12:14:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 9dff4069-7577-3b9c-b603-086129f44b40 | -7.19486 | -46.20263 | 2025-09-04 12:14:00 | TERRA_M-T | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 06f54d05-4c84-3e7e-85bc-025b68a13487 | -5.93875 | -51.96593 | 2025-09-04 12:14:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 7613e1f5-fed0-3008-884b-6b8397646758 | -6.83074 | -47.99928 | 2025-09-04 12:14:00 | TERRA_M-T | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Amazônia | 9.7 |
| aa9bb032-1665-333a-902c-7e2108370f04 | -5.98228 | -42.97471 | 2025-09-04 12:14:00 | TERRA_M-T | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| dd4200e4-90b5-3d80-9ab5-1e8a44a534da | -6.81952 | -45.6681 | 2025-09-04 12:14:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| bf728e10-a01f-3f80-981c-af410278fdb3 | -5.88369 | -43.16358 | 2025-09-04 12:14:00 | TERRA_M-T | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 5d5c8f2e-0f3c-3e4c-a971-55584164c290 | -5.78836 | -45.07782 | 2025-09-04 12:14:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 594afd72-b74d-30e4-916e-76047818c9d4 | -7.30392 | -39.6474 | 2025-09-04 12:14:00 | TERRA_M-T | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 124.5 |
| 8169bd01-61d9-351c-87e5-3645d6f866a5 | -6.41252 | -43.26181 | 2025-09-04 12:14:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 557396af-302f-3b00-afbe-eefa91e533bb | -6.37064 | -45.64612 | 2025-09-04 12:14:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 72a537b4-5304-3e3f-83f1-4e481125ea8f | -6.92821 | -45.55343 | 2025-09-04 12:14:00 | TERRA_M-T | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 02529587-1f9a-33c5-b1a9-273887328bcd | -6.21702 | -43.55156 | 2025-09-04 12:14:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| aeb9313e-e4fc-39c1-851a-ee7e4e099783 | -6.34575 | -43.39188 | 2025-09-04 12:14:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 47041f1b-3e11-36fb-9a21-96c1e7f5d30b | -6.65536 | -44.09433 | 2025-09-04 12:14:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 4c7c6fcf-5389-3d39-927b-8b7a192321d3 | -6.54469 | -43.90762 | 2025-09-04 12:14:00 | TERRA_M-T | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 9ac14062-dde0-3612-8163-a8a29bdcea92 | -5.3521 | -45.09477 | 2025-09-04 12:14:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| b877f09a-7bf1-3cc7-853e-ad3018e5980a | -7.94706 | -44.9355 | 2025-09-04 12:14:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 76528b1f-ae08-3638-8c22-f1843eead9c7 | -4.96444 | -43.22115 | 2025-09-04 12:14:00 | TERRA_M-T | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 5edaafd5-9f41-33d5-8d44-05dfdf9a2aee | -6.028 | -46.67943 | 2025-09-04 12:14:00 | TERRA_M-T | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 25.5 |
| d968457a-956b-39bb-b357-bd0907c72750 | -6.3618 | -45.64488 | 2025-09-04 12:14:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 121.0 |
| f3f1f32c-20d9-3fa2-976e-b2542fad552e | -6.25649 | -45.15548 | 2025-09-04 12:14:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 34620c60-4f28-3a34-be54-e7593e681395 | -6.22645 | -43.55302 | 2025-09-04 12:14:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 55.1 |
| 2087193a-6e11-3e22-b0da-a6dfa14a59eb | -6.23736 | -43.40733 | 2025-09-04 12:14:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 0adf597b-1ca5-3e36-9594-451eb3bc93ca | -6.24362 | -42.63472 | 2025-09-04 12:14:00 | TERRA_M-T | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 12.2 |
| 1319beb5-bd20-37e1-bcce-557ee715111c | -4.32328 | -40.14677 | 2025-09-04 12:14:00 | TERRA_M-T | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 60.6 |


[Clique aqui para ver as próximas entradas](README99.md)
